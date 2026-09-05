#!/usr/bin/env python3
"""
Story 1-2: BMAD Setup
Setup verification script for a BMAD + Python project.

This script confirms that all prerequisites are installed and properly configured.
Run this after completing the setup steps in the video.
"""

import subprocess
import sys
from pathlib import Path

def check_command(cmd: str, args: list = None) -> tuple[bool, str]: # type: ignore
    """Check if a command exists and return its version output."""
    if args is None:
        args = ["--version"]
    
    try:
        result = subprocess.run(
            [cmd] + args,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0, result.stdout.strip() or result.stderr.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, "Not found or timed out"

def main():
    """Check all BMAD prerequisites."""
    print("=" * 70)
    print("🔍 BMAD + Python Setup Verification")
    print("=" * 70)
    print()
    
    all_good = True
    
    # Check Node.js
    print("1️⃣  Checking Node.js...")
    node_ok, node_version = check_command("node")
    if node_ok:
        # Extract version number
        version_line = node_version.split('\n')[0]
        print(f"   ✅ Node.js installed: {version_line}")
    else:
        print(f"   ❌ Node.js not found. Install from https://nodejs.org/")
        all_good = False
    print()
    
    # Check Python
    print("2️⃣  Checking Python...")
    python_ok, python_version = check_command("python", ["--version"])
    if python_ok:
        print(f"   ✅ Python installed: {python_version}")
        # Check if Python 3.10+
        if "3.10" in python_version or "3.11" in python_version or "3.12" in python_version:
            print("   ✅ Python version is 3.10 or higher")
        else:
            print("   ⚠️  Warning: Python should be 3.10 or higher")
    else:
        print(f"   ❌ Python not found")
        all_good = False
    print()
    
    # Check uv (Python package manager)
    print("3️⃣  Checking uv (Python package manager)...")
    uv_ok, uv_version = check_command("uv", ["--version"])
    if uv_ok:
        print(f"   ✅ uv installed: {uv_version}")
    else:
        print(f"   ❌ uv not found. Install with: pip install uv")
        all_good = False
    print()
    
    # Check BMAD installation
    print("4️⃣  Checking BMAD installation...")
    bmad_config = Path("./_bmad")
    if bmad_config.exists():
        print(f"   ✅ BMAD folder detected at: {bmad_config.absolute()}")
    else:
        print(f"   ℹ️  BMAD folder not found. Run: npx bmad-method install")
    print()
    
    # Summary
    print("=" * 70)
    if all_good:
        print("✅ All prerequisites are installed!")
        print()
        print("Next steps:")
        print("1. If BMAD is not installed, run: npx bmad-method install")
        print("2. Watch Story 1-2 (BMAD Setup) on YouTube for the full walkthrough")
        print("3. Continue to Story 1-3 (BMAD Loop Setup)")
    else:
        print("⚠️  Some prerequisites are missing. Please install them:")
        print()
        if not node_ok:
            print("   • Node.js: https://nodejs.org/ (v20.12+)")
        if not python_ok:
            print("   • Python: https://www.python.org/ (v3.10+)")
        if not uv_ok:
            print("   • uv: pip install uv")
    print("=" * 70)

if __name__ == "__main__":
    main()
