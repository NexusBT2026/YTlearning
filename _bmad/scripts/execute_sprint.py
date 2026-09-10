#!/usr/bin/env python3
"""
Story Execution Engine - Generate individual execution reports per story
"""

import os
import yaml
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple

class ScriptFormatter:
    """
    Apply platform-aware formatting to script files.
    Automatically detects and formats bash/powershell commands with alternatives.
    """
    
    PLATFORM_PATTERNS = {
        'mkdir_linux': {
            'pattern': r'^(mkdir\s+[\w\-./]+)$',
            'os': 'linux',
            'prefix': '📁 Linux / macOS / WSL:',
            'command': lambda m: m.group(1)
        },
        'mkdir_windows': {
            'pattern': r'^(mkdir\s+[\w\-./]+)$',
            'os': 'windows',
            'prefix': '🪟 Windows PowerShell:',
            'alternatives': [
                ('New-Item -ItemType Directory -Path {folder}', 'Full command'),
                ('md {folder}', 'Short alias'),
                ('if (!(Test-Path "{folder}")) {{ md {folder} }}', 'Safe - no error if exists'),
                ('mkdir {folder}', 'Or in CMD'),
            ]
        },
        'cat_linux': {
            'pattern': r'^(cat\s+[\w\-./]+\.(?:py|md|txt|yaml|json))$',
            'os': 'linux',
            'prefix': '📋 Linux / macOS / WSL:',
            'command': lambda m: m.group(1)
        },
        'cat_windows': {
            'pattern': r'^(cat\s+[\w\-./]+\.(?:py|md|txt|yaml|json))$',
            'os': 'windows',
            'prefix': '🪟 Windows PowerShell:',
            'alternatives': [
                ('Get-Content {file}', 'PowerShell'),
                ('type {file}', 'Or in CMD'),
            ]
        },
        'ls_linux': {
            'pattern': r'^(ls\s+[\w\-./]*)$',
            'os': 'linux',
            'prefix': '📁 Linux / macOS / WSL:',
            'command': lambda m: m.group(1)
        },
        'ls_windows': {
            'pattern': r'^(ls\s+[\w\-./]*)$',
            'os': 'windows',
            'prefix': '📁 Windows PowerShell:',
            'alternatives': [
                ('Get-ChildItem', 'PowerShell (dir alias also works)'),
                ('dir', 'Or in CMD'),
            ]
        },
        'pip_install': {
            'pattern': r'^(pip\s+install\s+.+)$',
            'os': 'universal',
            'prefix': '📦 All platforms:',
            'command': lambda m: m.group(1).replace('pip', 'pip3'),
            'note': '(use pip3 on Linux/macOS, or uv for better performance)'
        },
        'conda_activate': {
            'pattern': r'^(conda\s+(?:activate|deactivate).*)$',
            'os': 'universal',
            'prefix': '📦 All platforms:',
            'command': lambda m: m.group(1)
        },
    }
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
    
    def format_script_file(self, script_path: Path) -> bool:
        """
        Read script file, apply platform-aware formatting, write back.
        Returns True if changes made, False if no changes.
        """
        if not script_path.exists():
            return False
        
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            formatted = self.format_content(content)
            
            if formatted != content:
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(formatted)
                return True
            return False
        except Exception as e:
            print(f"⚠️ Error formatting {script_path}: {e}")
            return False
    
    def format_content(self, content: str) -> str:
        """
        Expand command code blocks to multi-OS format.
        Strategy: 
        1. Single-command blocks: Expand directly to multi-OS format
        2. Version-check blocks (node -v, python --version, etc.): Split and expand each
        3. Sequence blocks (conda create + activate): Keep as-is
        4. Other multi-command: Keep as-is
        """
        lines = content.split('\n')
        output = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            # Check for bare text commands (corrupted remnants)
            if (stripped and not stripped.startswith('#') and 
                not stripped.startswith('-') and not stripped.startswith('>') and
                not stripped.startswith('"') and not stripped.startswith("'") and
                not stripped.startswith('```') and not stripped.startswith('*') and
                not stripped.startswith('|')):
                
                # Bare conda activate
                if 'conda activate' in stripped and stripped.count(' ') < 4:
                    m = re.search(r'conda activate\s+([\w\-]+)', stripped)
                    if m and stripped == m.group(0):
                        expanded = self._format_conda_activate(m.group(1), 0)
                        output.extend(expanded.split('\n'))
                        i += 1
                        continue
                
                # Bare node -v
                elif 'node -v' in stripped and stripped.count(' ') <= 1:
                    if stripped == 'node -v':
                        expanded = self._format_node_version(0)
                        output.extend(expanded.split('\n'))
                        i += 1
                        continue
                
                # Bare python --version
                elif 'python --version' in stripped and stripped.count(' ') <= 2:
                    if 'python' in stripped and '--version' in stripped:
                        expanded = self._format_python_version(0)
                        output.extend(expanded.split('\n'))
                        i += 1
                        continue
                
                # Bare uv --version
                elif 'uv --version' in stripped and stripped.count(' ') <= 2:
                    if stripped == 'uv --version':
                        expanded = self._format_python_version(0)
                        output.extend(expanded.split('\n'))
                        i += 1
                        continue
            
            # Check for code fence
            if stripped.startswith('```'):
                fence_start = lines[i]
                i += 1
                code_block = []
                
                # Read code block
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_block.append(lines[i])
                    i += 1
                
                if i < len(lines):
                    fence_end = lines[i]
                    i += 1
                else:
                    fence_end = '```'
                
                # Get non-empty, non-comment lines
                command_lines = [line for line in code_block if line.strip() and not line.strip().startswith('#')]
                
                # CASE 1: Empty or comment-only block
                if not command_lines:
                    output.append(fence_start)
                    output.extend(code_block)
                    output.append(fence_end)
                    continue
                
                # CASE 2: Single command line - expand it
                if len(command_lines) == 1:
                    code_line = command_lines[0].strip()
                    expanded = self._try_expand_command(code_line)
                    if expanded:
                        output.extend(expanded.split('\n'))
                    else:
                        output.append(fence_start)
                        output.extend(code_block)
                        output.append(fence_end)
                    continue
                
                # CASE 3: Check if it's a version-check block (node -v, python --version, uv --version)
                if self._is_version_check_block(command_lines):
                    # Expand each check command separately
                    for cmd_line in command_lines:
                        expanded = self._try_expand_command(cmd_line.strip())
                        if expanded:
                            output.extend(expanded.split('\n'))
                        else:
                            # Fallback to keeping as plain block if can't expand
                            output.append(fence_start)
                            output.append(cmd_line)
                            output.append(fence_end)
                    continue
                
                # CASE 4: Multi-command block - leave as-is
                # (Don't expand to avoid duplication and corruption)
                output.append(fence_start)
                output.extend(code_block)
                output.append(fence_end)
                continue
            
            # Not a code fence or bare command, keep line as-is
            output.append(line)
            i += 1
        
        return '\n'.join(output)
    
    def _is_version_check_block(self, command_lines: list) -> bool:
        """Check if block contains only version/check commands (node -v, python --version, uv --version)."""
        check_commands = ['node -v', 'node --version', 'python --version', 'python3 --version', 'uv --version', 'npm --version']
        cmds = [line.strip() for line in command_lines]
        
        # All commands must be version checks
        for cmd in cmds:
            if not any(check in cmd for check in check_commands):
                return False
        
        # And we must have exactly the expected number of commands (no duplicates)
        return len(cmds) <= 3  # max 3 independent checks
    
    def _try_expand_command(self, cmd_line: str) -> str:
        """Try to expand a single command line to multi-OS format. Returns expanded format or None."""
        # pip/uv install
        if 'pip install' in cmd_line:
            m = re.search(r'pip(?:3)?\s+install\s+([\w\-]+)', cmd_line)
            if m:
                return self._format_install_multiplatform(m.group(1), 0)
        elif 'uv add' in cmd_line:
            m = re.search(r'uv add\s+([\w\-]+)', cmd_line)
            if m:
                return self._format_install_multiplatform(m.group(1), 0)
        
        # conda create
        elif 'conda create' in cmd_line:
            m = re.search(r'conda create\s+-n\s+([\w\-]+)\s+python=([\d.]+)', cmd_line)
            if m:
                return self._format_conda_create(m.group(1), m.group(2), 0)
        
        # conda activate
        elif 'conda activate' in cmd_line:
            m = re.search(r'conda activate\s+([\w\-]+)', cmd_line)
            if m:
                return self._format_conda_activate(m.group(1), 0)
        
        # node -v
        elif 'node -v' in cmd_line or 'node --version' in cmd_line:
            return self._format_node_version(0)
        
        # uv --version (MUST come before python to avoid matching python)
        elif 'uv --version' in cmd_line:
            return self._format_uv_version(0)
        
        # python --version
        elif 'python --version' in cmd_line or 'python3 --version' in cmd_line:
            return self._format_python_version(0)
        
        # npx commands
        elif 'npx ' in cmd_line:
            m = re.search(r'npx\s+(.+)', cmd_line)
            if m:
                return self._format_npx(m.group(1), 0)
        
        return ""
    
    def _is_single_command_line(self, line: str) -> bool:
        """
        Check if this line looks like a single bare command (not inside code fence).
        Returns True for lines like: "pip install web3" or "node -v" (no ``` markers)
        """
        stripped = line.strip()
        
        # Skip empty lines, code fences, headers, or already formatted
        if not stripped or stripped.startswith('```') or stripped.startswith('####') or stripped.startswith('#'):
            return False
        
        # Check for actual commands
        commands = [
            'pip install', 'pip3 install', 'uv add',
            'conda activate',
            'node -v', 'node --version',
            'python --version', 'python3 --version', 'py --version',
            'npx ',
            'code .',
            'which ', 'Get-Command '
        ]
        
        return any(cmd in stripped for cmd in commands)
    
    def _format_single_command(self, line: str) -> str:
        """
        Format a single bare command line to multi-OS format.
        Returns single line if no match, or multi-line formatted string.
        """
        stripped = line.strip()
        
        # Conda activation
        if 'conda activate' in stripped:
            match = re.search(r'conda activate\s+([\w\-]+)', stripped)
            if match:
                return self._format_conda_activate(match.group(1), 0)
        
        # Node version
        if stripped in ('node -v', 'node --version'):
            return self._format_node_version(0)
        
        # Python version
        if ('python' in stripped and '--version' in stripped):
            return self._format_python_version(0)
        
        # npx commands
        if stripped.startswith('npx '):
            match = re.search(r'npx\s+(.+?)(?:\s*$|\s*#)', stripped)
            if match:
                return self._format_npx(match.group(1), 0)
        
        # VS Code launch
        if stripped == 'code .':
            return self._format_code_launch(0)
        
        # pip/uv install
        if 'pip install' in stripped or 'uv add' in stripped:
            package = self._extract_package(stripped)
            if package:
                return self._format_install_multiplatform(package, 0)
        
        # which/Get-Command
        if stripped.startswith('which '):
            cmd_name = stripped.replace('which ', '', 1).strip()
            if cmd_name:
                return self._format_which_check(cmd_name, 0)
        
        # No match - return original
        return line
    
    def _try_format_line(self, line: str) -> str:
        """
        Try to format a single line with platform-aware alternatives.
        Returns formatted version or original if no match.
        """
        stripped = line.strip()
        
        # Skip already formatted lines
        if stripped.startswith('####'):
            return line
        
        # conda activate detection
        if 'conda activate' in stripped and ';' not in stripped:
            match = re.search(r'conda activate\s+([\w\-]+)', stripped)
            if match:
                env_name = match.group(1)
                return self._format_conda_activate(env_name, line.count(' ') - len(line.lstrip()))
        
        # node -v / version checks
        if stripped == 'node -v' or stripped == 'node --version':
            return self._format_node_version(line.count(' ') - len(line.lstrip()))
        
        # python --version / python3 --version
        if 'python' in stripped and '--version' in stripped and ';' not in stripped:
            return self._format_python_version(line.count(' ') - len(line.lstrip()))
        
        # npx commands
        if stripped.startswith('npx ') and not 'Get-Command' in stripped:
            match = re.search(r'npx\s+(.+?)(?:\s*$|\s*#)', stripped)
            if match:
                cmd = match.group(1)
                return self._format_npx(cmd, line.count(' ') - len(line.lstrip()))
        
        # code . (VS Code launch)
        if stripped == 'code .':
            return self._format_code_launch(line.count(' ') - len(line.lstrip()))
        
        # which / Get-Command checks
        if stripped.startswith('which ') or (stripped.startswith('Get-Command') and 'Where-Object' not in stripped):
            cmd_name = stripped.replace('which ', '', 1).replace('Get-Command ', '', 1).strip()
            if cmd_name:
                return self._format_which_check(cmd_name, line.count(' ') - len(line.lstrip()))
        
        # pip/uv install detection - expand to full multi-OS format
        if ('pip install' in stripped or 'uv add' in stripped) and ';' not in stripped and not stripped.startswith('####'):
            package = self._extract_package(stripped)
            if package:
                return self._format_install_multiplatform(package, line.count(' ') - len(line.lstrip()))
        
        # mkdir detection
        if 'mkdir' in stripped and ';' not in stripped and 'New-Item' not in stripped and not stripped.startswith('####'):
            folder = self._extract_folder(stripped)
            if folder:
                return self._format_mkdir(folder, line.count(' ') - len(line.lstrip()))
        
        # cat/file viewing detection
        if stripped.startswith('cat ') and ';' not in stripped and not stripped.startswith('####'):
            file_path = stripped.replace('cat ', '', 1).strip()
            if file_path:
                return self._format_cat(file_path, line.count(' ') - len(line.lstrip()))
        
        # ls/listing detection  
        if stripped.startswith('ls ') and ';' not in stripped and not stripped.startswith('####'):
            return self._format_ls(stripped.replace('ls ', '', 1).strip(), line.count(' ') - len(line.lstrip()))
        
        return line
    
    def _extract_folder(self, line: str) -> str:
        """Extract folder name from mkdir command."""
        match = re.search(r'mkdir\s+([\w\-./]+)', line)
        if match:
            return match.group(1)
        return ""
    
    def _extract_package(self, line: str) -> str:
        """Extract package name(s) from pip/uv install command."""
        # Handle: pip install web3, pip install web3 rich, uv add web3, etc.
        if 'pip install' in line:
            match = re.search(r'pip install\s+(.+?)(?:\s*$|\s*#)', line)
            if match:
                return match.group(1).strip()
        elif 'uv add' in line:
            match = re.search(r'uv add\s+(.+?)(?:\s*$|\s*#)', line)
            if match:
                return match.group(1).strip()
        return ""
    
    def _format_mkdir(self, folder: str, indent: int) -> str:
        """Format mkdir with platform alternatives."""
        ind = ' ' * indent
        result = []
        
        result.append(f"{ind}📁 Linux / macOS / WSL: `mkdir {folder}; cd {folder}`")
        result.append(f"{ind}🪟 Windows PowerShell (full): `New-Item -ItemType Directory -Path {folder}; cd {folder}`")
        result.append(f"{ind}📄 Or shorter: `md {folder}; cd {folder}`")
        result.append(f"{ind}📄 Or safe: `if (!(Test-Path \"{folder}\")) {{ md {folder} }}; cd {folder}`")
        result.append(f"{ind}📄 Windows CMD: `mkdir {folder}; cd {folder}`")
        
        return '\n'.join(result)
    
    def _format_install(self, packages: str, indent: int) -> str:
        """Format pip/uv install with cross-platform alternatives."""
        ind = ' ' * indent
        result = []
        
        result.append(f"{ind}📦 Linux / macOS / WSL (standard): `pip install {packages}`")
        result.append(f"{ind}📄 Or if pip3 required: `pip3 install {packages}`")
        result.append(f"{ind}📄 Or fallback: `python -m pip install {packages}`")
        result.append(f"{ind}🪟 Windows PowerShell: `pip install {packages}` (or `python -m pip install {packages}` if pip missing)")
        result.append(f"{ind}⚡ Recommended (all platforms): `uv add {packages}`")
        
        return '\n'.join(result)
    
    def _format_install_multiplatform(self, packages: str, indent: int) -> str:
        """
        Format pip/uv install with full multi-OS structure - multiple fallback options per platform.
        Expands to Linux/macOS/WSL section + Windows PowerShell section + Windows CMD section.
        """
        ind = ' ' * indent
        result = []
        
        # Linux / macOS / WSL section
        result.append(f"#### 🐧 Linux / macOS / WSL")
        result.append(f"")
        result.append(f"##### ✔ Standard (most common)")
        result.append(f"```bash")
        result.append(f"pip install {packages}")
        result.append(f"```")
        result.append(f"")
        result.append(f"##### ✔ If pip is mapped to Python 2 (older systems)")
        result.append(f"```bash")
        result.append(f"pip3 install {packages}")
        result.append(f"```")
        result.append(f"")
        result.append(f"##### ✔ If pip/pip3 are missing but python works")
        result.append(f"```bash")
        result.append(f"python -m pip install {packages}")
        result.append(f"```")
        result.append(f"")
        result.append(f"##### ✔ If Python is installed as `python` (macOS Homebrew)")
        result.append(f"```bash")
        result.append(f"python -m pip install {packages}")
        result.append(f"```")
        result.append(f"")
        
        # Windows PowerShell section
        result.append(f"#### 🪟 Windows PowerShell")
        result.append(f"")
        result.append(f"##### ✔ Standard (recommended)")
        result.append(f"```powershell")
        result.append(f"pip install {packages}")
        result.append(f"```")
        result.append(f"")
        result.append(f"##### ✔ If pip is not found but Python works")
        result.append(f"```powershell")
        result.append(f"python -m pip install {packages}")
        result.append(f"```")
        result.append(f"")
        result.append(f"##### ✔ If Python is installed from Microsoft Store")
        result.append(f"```powershell")
        result.append(f"py -m pip install {packages}")
        result.append(f"```")
        result.append(f"")
        result.append(f"##### ✔ If pip is broken (rare)")
        result.append(f"```powershell")
        result.append(f"python -m ensurepip --upgrade")
        result.append(f"python -m pip install {packages}")
        result.append(f"```")
        result.append(f"")
        
        # Windows CMD section
        result.append(f"#### 🪟 Windows CMD (legacy)")
        result.append(f"")
        result.append(f"##### ✔ CMD version")
        result.append(f"```cmd")
        result.append(f"pip install {packages}")
        result.append(f"```")
        result.append(f"")
        result.append(f"##### ✔ CMD fallback")
        result.append(f"```cmd")
        result.append(f"py -m pip install {packages}")
        result.append(f"```")
        
        return '\n'.join(result)
    
    def _format_cat(self, file_path: str, indent: int) -> str:
        """Format cat with platform alternatives."""
        ind = ' ' * indent
        result = []
        
        result.append(f"{ind}📋 Linux / macOS / WSL: `cat {file_path}`")
        result.append(f"{ind}🪟 Windows PowerShell: `Get-Content {file_path}`")
        result.append(f"{ind}📄 Or in CMD: `type {file_path}`")
        
        return '\n'.join(result)
    
    def _format_ls(self, path: str, indent: int) -> str:
        """Format ls with platform alternatives."""
        ind = ' ' * indent
        result = []
        
        path_str = path if path else '.'
        result.append(f"{ind}📁 Linux / macOS / WSL: `ls {path_str}`")
        result.append(f"{ind}📁 Windows PowerShell: `Get-ChildItem {path_str}` (or `dir`)")
        
        return '\n'.join(result)
    
    def _format_conda_create(self, env_name: str, python_version: str, indent: int) -> str:
        """Format conda create with minimal options for different systems."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("```bash")
        result.append(f"conda create -n {env_name} python={python_version}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("```powershell")
        result.append(f"conda create -n {env_name} python={python_version}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("```cmd")
        result.append(f"conda create -n {env_name} python={python_version}")
        result.append("```")
        
        return '\n'.join(result)
    
    def _format_conda_activate(self, env_name: str, indent: int) -> str:
        """Format conda activate with minimal fallback for different systems."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("```bash")
        result.append(f"conda activate {env_name}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("```powershell")
        result.append(f"conda activate {env_name}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("```cmd")
        result.append(f"conda activate {env_name}")
        result.append("```")
        
        return '\n'.join(result)
    
    def _format_node_version(self, indent: int) -> str:
        """Format node version check with minimal alternatives."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("```bash")
        result.append("node -v")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("```powershell")
        result.append("node -v")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("```cmd")
        result.append("node -v")
        result.append("```")
        
        return '\n'.join(result)
    
    def _format_python_version(self, indent: int) -> str:
        """Format python version check with minimal fallback options."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("```bash")
        result.append("python --version")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("```powershell")
        result.append("python --version")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("```cmd")
        result.append("python --version")
        result.append("```")
        
        return '\n'.join(result)
    
    def _format_uv_version(self, indent: int) -> str:
        """Format uv version check with minimal fallback options."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("```bash")
        result.append("uv --version")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("```powershell")
        result.append("uv --version")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("```cmd")
        result.append("uv --version")
        result.append("```")
        
        return '\n'.join(result)
    
    def _format_npx(self, command: str, indent: int) -> str:
        """Format npx commands with minimal fallback alternatives."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("```bash")
        result.append(f"npx {command}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("```powershell")
        result.append(f"npx {command}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("```cmd")
        result.append(f"npx {command}")
        result.append("```")
        
        return '\n'.join(result)
    
    def _format_code_launch(self, indent: int) -> str:
        """Format VS Code launch command with fallback options."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("")
        result.append("##### ✔ Standard")
        result.append("```bash")
        result.append("code .")
        result.append("```")
        result.append("")
        result.append("##### ✔ If code not in PATH")
        result.append("```bash")
        result.append("/usr/bin/code .")
        result.append("```")
        result.append("")
        result.append("##### ✔ macOS alternative")
        result.append("```bash")
        result.append("open -a \"Visual Studio Code\" .")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("")
        result.append("##### ✔ Standard")
        result.append("```powershell")
        result.append("code .")
        result.append("```")
        result.append("")
        result.append("##### ✔ If code not found (full path)")
        result.append("```powershell")
        result.append("& \"C:\\Users\\$env:USERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" .")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("")
        result.append("##### ✔ CMD version")
        result.append("```cmd")
        result.append("code .")
        result.append("```")
        result.append("")
        result.append("##### ✔ Fallback (full path)")
        result.append("```cmd")
        result.append("\"C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" .")
        result.append("```")
        
        return '\n'.join(result)
    
    def _format_which_check(self, command: str, indent: int) -> str:
        """Format command existence checks with platform alternatives."""
        result = []
        
        result.append("#### 🐧 Linux / macOS / WSL")
        result.append("")
        result.append("##### ✔ Check if command exists")
        result.append("```bash")
        result.append(f"which {command}")
        result.append("```")
        result.append("")
        result.append("##### ✔ Alternative with full output")
        result.append("```bash")
        result.append(f"command -v {command}")
        result.append("type {command}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows PowerShell")
        result.append("")
        result.append("##### ✔ Check if command exists")
        result.append("```powershell")
        result.append(f"Get-Command {command}")
        result.append("```")
        result.append("")
        result.append("##### ✔ Alternative - find in PATH")
        result.append("```powershell")
        result.append(f"where.exe {command}")
        result.append("```")
        result.append("")
        
        result.append("#### 🪟 Windows CMD")
        result.append("")
        result.append("##### ✔ CMD version")
        result.append("```cmd")
        result.append(f"where {command}")
        result.append("```")
        
        return '\n'.join(result)


class StoryExecutor:
    def __init__(self, project_root: str, story_id: str):
        self.project_root = Path(project_root)
        self.story_id = story_id
        self.sprint_status_file = self.project_root / "_bmad-output" / "implementation-artifacts" / "sprint-status.yaml"
        self.stories_dir = self.project_root / "_bmad-output" / "implementation-artifacts" / "stories"
        self.execution_artifacts_dir = self.project_root / "_bmad-output" / "execution-artifacts"
        self.execution_artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        self.series_map = {
            '1': '1-bmad-for-python',
            '2': '2-real-projects',
            '3': '3-crypto',
            '4': '4-tutorials',
            '5': '5-shorts',
        }
        
        self.story_data = None
        self.episodes_dir = None
        self.story_report = {}
        
    def load_story_data(self) -> bool:
        """Load story metadata from sprint-status.yaml development_status"""
        try:
            with open(self.sprint_status_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                dev_status = data.get('development_status', {})
                
                # Find story in development_status
                if self.story_id in dev_status:
                    self.story_data = dev_status[self.story_id]
                    if not isinstance(self.story_data, dict):
                        self.story_data = {'status': self.story_data}
                else:
                    print(f"❌ Story '{self.story_id}' not found in development_status")
                    return False
                
                # Set episodes directory based on story prefix
                series_num = self.story_id.split('-')[0]
                if series_num in self.series_map:
                    self.episodes_dir = self.project_root / self.series_map[series_num]
                else:
                    self.episodes_dir = self.project_root / "1-bmad-for-python"
                
                return True
        except Exception as e:
            print(f"❌ Error loading story data: {e}")
            return False
    
    def validate_story(self) -> Dict[str, Any]:
        """Validate story has all required components"""
        story_file = self.stories_dir / f"{self.story_id}.md"
        episode_folder = self.episodes_dir / self.story_id
        
        validation = {
            'story_id': self.story_id,
            'status': 'ready',
            'checks': {
                'story_file_exists': story_file.exists(),
                'episode_folder_exists': episode_folder.exists(),
                'script_exists': (episode_folder / 'script' / 'script.md').exists(),
                'code_exists': (episode_folder / 'code').exists() and any((episode_folder / 'code').iterdir()),
                'readme_exists': (episode_folder / 'README.md').exists(),
                'assets_exists': (episode_folder / 'assets' / 'ASSETS.md').exists(),
            }
        }
        
        if not all(validation['checks'].values()):
            validation['status'] = 'at-risk'
            validation['missing'] = [k for k, v in validation['checks'].items() if not v]
        
        return validation
    
    def extract_story_metadata(self) -> Dict[str, Any]:
        """Extract metadata from story markdown file"""
        story_file = self.stories_dir / f"{self.story_id}.md"
        metadata = {
            'story_id': self.story_id,
            'title': 'Unknown',
            'duration_estimate': 'Unknown',
        }
        
        try:
            with open(story_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
                # Extract title from frontmatter
                if 'title:' in content:
                    lines = content.split('\n')
                    for line in lines:
                        if line.startswith('title:'):
                            metadata['title'] = line.replace('title:', '').strip().strip('"').strip("'")
                            break
                
                # Extract duration from frontmatter
                if 'duration:' in content:
                    lines = content.split('\n')
                    for line in lines:
                        if line.startswith('duration:'):
                            metadata['duration_estimate'] = line.replace('duration:', '').strip().strip('"').strip("'")
                            break
        except Exception as e:
            print(f"⚠️ Error extracting metadata for {self.story_id}: {e}")
        
        return metadata
    
    def extract_assets_requirements(self) -> List[str]:
        """Extract asset requirements from ASSETS.md"""
        assets_file = self.episodes_dir / self.story_id / "assets" / "ASSETS.md"
        requirements = []
        
        try:
            if assets_file.exists():
                with open(assets_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.split('\n')
                    for line in lines:
                        if line.strip().startswith('- [ ]'):
                            item = line.replace('- [ ]', '').strip()
                            requirements.append(item)
        except Exception as e:
            print(f"⚠️ Error extracting assets for {self.story_id}: {e}")
        
        return requirements
    
    def build_production_checklist(self, metadata: Dict[str, Any]) -> List[str]:
        """Build production checklist for this story"""
        checklist = [
            "Script memorization or teleprompter setup",
            "Recording environment (quiet, well-lit)",
            "Camera/audio equipment test",
            f"Runtime: {metadata.get('duration_estimate', 'Unknown')}",
            "Code environment ready",
            "Demo execution verified",
            "Screen capture points identified",
            "Thumbnail design created",
            "YouTube description prepared",
            "Quality check: Audio clear",
            "Quality check: Video smooth",
            "Quality check: All demo code works"
        ]
        return checklist
    
    def execute_story(self) -> bool:
        """Execute individual story processing"""
        print(f"\n🚀 Processing Story: {self.story_id}")
        
        # Load story data
        if not self.load_story_data():
            return False
        
        # Format script with platform-aware alternatives
        script_path = self.episodes_dir / self.story_id / 'script' / 'script.md'
        formatter = ScriptFormatter(str(self.project_root))
        if script_path.exists():
            if formatter.format_script_file(script_path):
                print(f"   ✅ Script formatted with platform-aware instructions")
            else:
                print(f"   ℹ️ Script already well-formatted")
        
        # Validate story
        validation = self.validate_story()
        metadata = self.extract_story_metadata()
        assets = self.extract_assets_requirements()
        checklist = self.build_production_checklist(metadata)
        
        # Build story report
        self.story_report = {
            'story_id': self.story_id,
            'title': metadata['title'],
            'duration_estimate': metadata['duration_estimate'],
            'script_ready': validation['checks']['script_exists'],
            'code_ready': validation['checks']['code_exists'],
            'readme_ready': validation['checks']['readme_exists'],
            'assets_ready': validation['checks']['assets_exists'],
            'validation_status': validation['status'],
            'asset_requirements': assets,
            'production_checklist': checklist,
            'generated_at': datetime.now().isoformat(),
        }
        
        # Print validation results
        if validation['status'] == 'ready':
            print(f"   ✅ Status: READY")
        else:
            print(f"   ⚠️ Status: AT-RISK - Missing: {', '.join(validation.get('missing', []))}")
        
        print(f"   ⏱️ Duration: {metadata['duration_estimate']}")
        print(f"   📝 Script: {'✅' if validation['checks']['script_exists'] else '❌'}")
        print(f"   💻 Code: {'✅' if validation['checks']['code_exists'] else '❌'}")
        print(f"   📋 Assets: {'✅' if validation['checks']['assets_exists'] else '❌'}")
        
        return True
    
    def save_execution_report(self) -> bool:
        """Save execution report to YAML file"""
        try:
            report_file = self.execution_artifacts_dir / f"story-{self.story_id}-execution-report.yaml"
            with open(report_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.story_report, f, default_flow_style=False, sort_keys=False)
            print(f"\n✅ Report saved: {report_file.name}")
            return True
        except Exception as e:
            print(f"❌ Error saving report: {e}")
            return False
    
    def generate_production_checklist(self) -> bool:
        """Generate markdown production checklist"""
        try:
            checklist_content = f"""# {self.story_report['title']} ({self.story_id}) — Production Checklist

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Duration**: {self.story_report['duration_estimate']}  
**Status**: {self.story_report['validation_status'].upper()}

---

## Pre-Production Checklist

"""
            for item in self.story_report['production_checklist']:
                checklist_content += f"- [ ] {item}\n"
            
            checklist_content += "\n---\n\n## Asset Requirements\n\n"
            for asset in self.story_report['asset_requirements']:
                checklist_content += f"- [ ] {asset}\n"
            
            checklist_content += """\n---

## Recording Checklist

- [ ] Script finalized
- [ ] Recording environment prepared
- [ ] Audio/video levels tested
- [ ] Screen recording setup verified
- [ ] Demo code ready to execute
- [ ] All code examples work

## Post-Production Checklist

- [ ] Video edited
- [ ] Captions added
- [ ] Thumbnail created
- [ ] Title and description written
- [ ] Tags/keywords added
- [ ] Playlist assignment set

## Quality Gate

- [ ] Audio quality acceptable
- [ ] Video quality acceptable
- [ ] All demos executed successfully
- [ ] No copyright issues
- [ ] Ready to upload

"""
            
            checklist_file = self.execution_artifacts_dir / f"story-{self.story_id}-production-checklist.md"
            with open(checklist_file, 'w', encoding='utf-8') as f:
                f.write(checklist_content)
            
            print(f"✅ Checklist saved: {checklist_file.name}")
            return True
        except Exception as e:
            print(f"❌ Error generating checklist: {e}")
            return False

class EpicExecutor:
    """Execute full epic processing - all stories in one report"""
    def __init__(self, project_root: str, epic_num: str):
        self.project_root = Path(project_root)
        self.epic_num = epic_num
        self.epic_id = f"epic-{epic_num}"
        self.sprint_status_file = self.project_root / "_bmad-output" / "implementation-artifacts" / "sprint-status.yaml"
        self.stories_dir = self.project_root / "_bmad-output" / "implementation-artifacts" / "stories"
        self.execution_artifacts_dir = self.project_root / "_bmad-output" / "execution-artifacts"
        self.execution_artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        self.series_map = {
            '1': '1-bmad-for-python',
            '2': '2-real-projects',
            '3': '3-crypto',
            '4': '4-tutorials',
            '5': '5-shorts',
        }
        
        self.epic_data = {}
        self.story_ids = []
        self.episodes_dir = None
        self.execution_report = {}
    
    def load_epic_data(self) -> bool:
        """Load all stories for this epic from sprint-status.yaml"""
        try:
            with open(self.sprint_status_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                dev_status = data.get('development_status', {})
                
                # Check if epic exists
                if self.epic_id not in dev_status:
                    print(f"❌ Epic '{self.epic_id}' not found in development_status")
                    return False
                
                self.epic_data = dev_status.get(self.epic_id, {})
                
                # Collect all stories for this epic
                for key in dev_status.keys():
                    if isinstance(key, str) and key.startswith(f"{self.epic_num}-") and not key.startswith('epic-'):
                        self.story_ids.append(key)
                
                self.story_ids.sort()
                
                # Set episodes directory
                if self.epic_num in self.series_map:
                    self.episodes_dir = self.project_root / self.series_map[self.epic_num]
                else:
                    self.episodes_dir = self.project_root / "1-bmad-for-python"
                
                return len(self.story_ids) > 0
        except Exception as e:
            print(f"❌ Error loading epic data: {e}")
            return False
    
    def validate_story(self, story_id: str) -> Dict[str, Any]:
        """Validate story components"""
        story_file = self.stories_dir / f"{story_id}.md"
        episode_folder = self.episodes_dir / story_id
        
        return {
            'story_id': story_id,
            'script_ready': (episode_folder / 'script' / 'script.md').exists(),
            'code_ready': (episode_folder / 'code').exists() and any((episode_folder / 'code').iterdir()),
            'readme_ready': (episode_folder / 'README.md').exists(),
            'assets_ready': (episode_folder / 'assets' / 'ASSETS.md').exists(),
        }
    
    def extract_story_metadata(self, story_id: str) -> Dict[str, Any]:
        """Extract metadata from story file"""
        story_file = self.stories_dir / f"{story_id}.md"
        metadata = {
            'title': 'Unknown',
            'duration_estimate': 'Unknown',
        }
        
        try:
            with open(story_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
                if 'title:' in content:
                    for line in content.split('\n'):
                        if line.startswith('title:'):
                            metadata['title'] = line.replace('title:', '').strip().strip('"').strip("'")
                            break
                
                if 'duration:' in content:
                    for line in content.split('\n'):
                        if line.startswith('duration:'):
                            metadata['duration_estimate'] = line.replace('duration:', '').strip().strip('"').strip("'")
                            break
        except Exception as e:
            print(f"⚠️ Error extracting metadata for {story_id}: {e}")
        
        return metadata
    
    def execute_epic(self) -> bool:
        """Execute full epic processing"""
        print(f"\n🚀 Executing Epic {self.epic_num}...\n")
        
        if not self.load_epic_data():
            return False
        
        print(f"✅ Epic: Epic {self.epic_num}")
        print(f"✅ Stories: {len(self.story_ids)}\n")
        
        # Build report
        self.execution_report = {
            'epic_id': self.epic_num,
            'epic_name': f'Epic {self.epic_num}',
            'generated_at': datetime.now().isoformat(),
            'stories': {},
            'summary': {
                'total_stories': len(self.story_ids),
                'ready_count': 0,
                'at_risk_count': 0,
            }
        }
        
        formatter = ScriptFormatter(str(self.project_root))
        
        # Process each story
        for story_id in self.story_ids:
            print(f"📖 Processing: {story_id}")
            
            # Format script
            script_path = self.episodes_dir / story_id / 'script' / 'script.md'
            if script_path.exists():
                if formatter.format_script_file(script_path):
                    print(f"   ✅ Script formatted")
            
            validation = self.validate_story(story_id)
            metadata = self.extract_story_metadata(story_id)
            
            checks_passed = all([
                validation['script_ready'],
                validation['code_ready'],
                validation['readme_ready'],
                validation['assets_ready']
            ])
            
            status = 'ready' if checks_passed else 'at-risk'
            
            story_report = {
                'title': metadata['title'],
                'duration': metadata['duration_estimate'],
                'status': status,
                'components': {
                    'script': validation['script_ready'],
                    'code': validation['code_ready'],
                    'readme': validation['readme_ready'],
                    'assets': validation['assets_ready'],
                }
            }
            
            self.execution_report['stories'][story_id] = story_report
            
            if checks_passed:
                self.execution_report['summary']['ready_count'] += 1
                print(f"   ✅ READY")
            else:
                self.execution_report['summary']['at_risk_count'] += 1
                print(f"   ⚠️ AT-RISK")
            
            print(f"   ⏱️  {metadata['duration_estimate']}\n")
        
        return True
    
    def save_execution_report(self) -> bool:
        """Save epic execution report"""
        try:
            report_file = self.execution_artifacts_dir / f"epic-{self.epic_num}-execution-report.yaml"
            with open(report_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.execution_report, f, default_flow_style=False, sort_keys=False)
            print(f"✅ Report saved: {report_file.name}")
            return True
        except Exception as e:
            print(f"❌ Error saving report: {e}")
            return False
    
    def generate_production_checklist(self) -> bool:
        """Generate epic production checklist"""
        try:
            checklist_content = f"""# Epic {self.epic_num} — Production Checklist

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

- **Total Stories**: {self.execution_report['summary']['total_stories']}
- **Ready**: {self.execution_report['summary']['ready_count']}
- **At-Risk**: {self.execution_report['summary']['at_risk_count']}

---

## Stories

"""
            
            for story_id, story in self.execution_report['stories'].items():
                script_check = 'YES' if story['components']['script'] else 'NO'
                code_check = 'YES' if story['components']['code'] else 'NO'
                readme_check = 'YES' if story['components']['readme'] else 'NO'
                assets_check = 'YES' if story['components']['assets'] else 'NO'
                
                checklist_content += f"""### {story['title']} ({story_id})

**Duration**: {story['duration']}  
**Status**: {story['status'].upper()}

- Script: {script_check}
- Code: {code_check}
- README: {readme_check}
- Assets: {assets_check}

"""
            
            checklist_file = self.execution_artifacts_dir / f"epic-{self.epic_num}-production-checklist.md"
            with open(checklist_file, 'w', encoding='utf-8') as f:
                f.write(checklist_content)
            
            print(f"✅ Checklist saved: {checklist_file.name}")
            return True
        except Exception as e:
            print(f"❌ Error generating checklist: {e}")
            return False

def lookup_full_story_id(project_root: str, abbreviated_id: str) -> str:
    """
    Look up full story ID from abbreviated form.
    
    Input: "1-1" or "5-1"
    Output: "1-1-what-is-bmad" or "5-1-vs-code-hack-auto-activate"
    """
    try:
        stories_dir = Path(project_root) / "_bmad-output" / "implementation-artifacts" / "stories"
        if not stories_dir.exists():
            return  ""
        
        # Look for files matching pattern: {abbreviated_id}-*.md
        pattern = f"{abbreviated_id}-*.md"
        files = list(stories_dir.glob(pattern))
        
        if files:
            # Return the first match (should only be one)
            filename = files[0].stem
            return filename
        
        return  ""
    except Exception:
        return  "" 

def main():
    """Main execution - supports story (full or abbreviated) and epic modes"""
    if len(sys.argv) < 2:
        print("Usage: python execute_sprint.py <identifier>")
        print("\nStory mode (individual report):")
        print("  python execute_sprint.py 1-1")
        print("  python execute_sprint.py 1-1-what-is-bmad")
        print("  python execute_sprint.py 5-1")
        print("\nEpic mode (full epic report):")
        print("  python execute_sprint.py 1")
        print("  python execute_sprint.py epic-1")
        print("  python execute_sprint.py sprint-1")
        print("  python execute_sprint.py 5")
        return 1
    
    identifier = sys.argv[1]
    project_root = os.getcwd()
    
    # Handle sprint-N format (backward compatibility) → convert to epic mode
    if identifier.startswith('sprint-'):
        identifier = identifier.replace('sprint-', '')
    
    # Detect mode: story vs epic
    # Story abbreviated: N-N (e.g., 1-1, 5-1)
    # Story full: N-N-name (e.g., 1-1-what-is-bmad, 5-1-vs-code-hack)
    # Epic: N or epic-N (e.g., 1, 5, epic-1, epic-5)
    
    parts = identifier.split('-')
    
    # Check if it's story mode (abbreviated or full)
    is_abbreviated_story = (len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit())
    is_full_story = (len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit())
    
    if is_abbreviated_story:
        # Abbreviated story mode: look up full ID
        full_story_id = lookup_full_story_id(project_root, identifier)
        if full_story_id:
            identifier = full_story_id
            executor = StoryExecutor(project_root, identifier)
            if executor.execute_story():
                executor.save_execution_report()
                executor.generate_production_checklist()
                print("\n" + "="*60)
                print(f"✅ STORY EXECUTION COMPLETE: {identifier}")
                print("="*60)
                return 0
            else:
                print("\n" + "="*60)
                print(f"❌ STORY EXECUTION FAILED")
                print("="*60)
                return 1
        else:
            print(f"❌ Story not found: {identifier}")
            return 1
    
    elif is_full_story:
        # Full story mode
        executor = StoryExecutor(project_root, identifier)
        if executor.execute_story():
            executor.save_execution_report()
            executor.generate_production_checklist()
            print("\n" + "="*60)
            print(f"✅ STORY EXECUTION COMPLETE: {identifier}")
            print("="*60)
            return 0
        else:
            print("\n" + "="*60)
            print(f"❌ STORY EXECUTION FAILED")
            print("="*60)
            return 1
    else:
        # Epic mode
        epic_num = identifier.replace('epic-', '')
        executor = EpicExecutor(project_root, epic_num)
        if executor.execute_epic():
            executor.save_execution_report()
            executor.generate_production_checklist()
            print("\n" + "="*60)
            print(f"✅ EPIC EXECUTION COMPLETE: Epic {epic_num}")
            print("="*60)
            return 0
        else:
            print("\n" + "="*60)
            print(f"❌ EPIC EXECUTION FAILED")
            print("="*60)
            return 1

if __name__ == "__main__":
    sys.exit(main())
