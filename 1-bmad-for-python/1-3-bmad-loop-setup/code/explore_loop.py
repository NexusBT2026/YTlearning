#!/usr/bin/env python3
"""
Story 1-3: BMAD Loop Setup
Utility script to help understand and interact with BMAD workflows.

This script provides quick commands to explore BMAD and run common workflows.
"""

import subprocess
import sys
from pathlib import Path
import json

def run_command(cmd: str) -> tuple[bool, str]:
    """Run a shell command and return success status and output."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)

def check_bmad_installed() -> bool:
    """Check if BMAD is installed in this project."""
    return Path("_bmad").exists()

def list_bmad_modules() -> None:
    """List available BMAD modules."""
    print("\n📦 Available BMAD Modules:")
    print("=" * 50)
    
    bmad_path = Path("_bmad")
    if not bmad_path.exists():
        print("❌ BMAD not installed. Run: npx bmad-method install")
        return
    
    modules = [d for d in bmad_path.iterdir() if d.is_dir() and not d.name.startswith("_")]
    
    module_info = {
        "core": "Core BMAD workflows (Planning, Design, Dev, Review, Verify)",
        "bmb": "BMAD Builder - Create custom agents and skills",
        "tea": "Test Architect - Quality assurance and testing workflows",
        "bmm": "BMAD Master Module - Advanced workflows",
        "custom": "Your custom extensions and modifications",
    }
    
    for module in sorted(modules):
        desc = module_info.get(module.name, "Custom module")
        config_file = module / "config.yaml"
        status = "✅" if config_file.exists() else "⚠️"
        print(f"{status} {module.name:15} - {desc}")
    
    print("=" * 50)

def list_workflows() -> None:
    """List available BMAD workflows from all modules (recursive search)."""
    print("\n🔄 Available BMAD Workflows:")
    print("=" * 50)
    
    # Search for workflows recursively in all BMAD modules
    bmad_path = Path("_bmad")
    workflows = {}
    
    for module_dir in bmad_path.iterdir():
        if not module_dir.is_dir() or module_dir.name.startswith("_"):
            continue
        
        workflow_path = module_dir / "workflows"
        if workflow_path.exists():
            # Recursively find all workflow markdown files
            for workflow_file in workflow_path.glob("**/*.md"):
                # Build relative path from _bmad for display
                rel_path = workflow_file.relative_to(bmad_path)
                workflows[str(rel_path.with_suffix(""))] = workflow_file
    
    workflow_descriptions = {
        "gds/workflows/1-preproduction/research/workflow-market-research": "Market research and competitive analysis",
        "gds/workflows/1-preproduction/research/workflow-technical-research": "Technical research and technology evaluation",
        "tea/workflows/testarch/README": "Test architecture guide",
    }
    
    if workflows:
        for name in sorted(workflows.keys()):
            desc = workflow_descriptions.get(name, "BMAD workflow")
            print(f"  📋 {name}")
            print(f"     └─ {desc}")
    else:
        print("ℹ️  No workflows found yet")
        print("   Workflows are located in: _bmad/[module]/workflows/")
    
    print("=" * 50)

def show_deferred_work() -> None:
    """Show the sprint status log."""
    print("\n📝 Sprint Status Log:")
    print("=" * 50)
    
    dw_file = Path("_bmad-output/implementation-artifacts/sprint-status.yaml")
    if dw_file.exists():
        print(f"✅ Found at: {dw_file.absolute()}")
        print()
        print("Preview (first 30 lines):")
        print("-" * 50)
        with open(dw_file, 'r') as f:
            lines = f.readlines()[:30]
            for line in lines:
                print(line.rstrip())
        if len(lines) > 30:
            print("... (more content)")
    else:
        print("ℹ️  No sprint status log yet")
        print()
        print("BMAD workflows create the sprint status log inside VS Code.")
        print("It will be saved to: _bmad-output/implementation-artifacts/sprint-status.yaml")
        print()
        print("To generate one:")
        print("  1. Press Ctrl + Shift + P in VS Code")
        print("  2. Search: 'BMAD: Launch Agent'")
        print("  3. Run a skill like 'bmad-help' or 'bmad-loop-setup'")
        print()
        print("After running BMAD workflows, come back to this menu to view the log.")
    
    print("=" * 50)

def show_commands() -> None:
    """Show how to run BMAD skills and commands."""
    print("\n💻 BMAD Skills (Run in Agent Chat, NOT terminal):")
    print("=" * 50)
    
    skills = {
        "use the bmad-loop-setup skill": "Activate the Loop Orchestrator (run once)",
        "use the bmad-help skill": "Get guidance and available workflows",
        "use the bmad-plan skill": "Run the Planning workflow",
        "use the bmad-design skill": "Run the Design workflow",
        "use the bmad-dev skill": "Run the Development workflow",
    }
    
    print("\n📝 To run these:")
    print("  1. Press Ctrl+Shift+P in VS Code")
    print("  2. Search: 'BMAD: Launch Agent'")
    print("  3. Type in chat: 'use the [skill-name] skill'")
    print("  4. Press Enter")
    
    print("\n🎯 Available Skills:")
    for cmd, desc in skills.items():
        print(f"\n  {cmd}")
        print(f"  → {desc}")
    
    print("\n" + "=" * 50)
    print("\n⚠️  Commands That DON'T Work (Don't use these):")
    print("  ❌ uv run bmad --help")
    print("  ❌ uv run bmad plan")
    print("  ❌ uv run bmad design")
    print("  These are fake commands and will fail.")
    
    print("\n" + "=" * 50)
    print("\n✅ For BMAD CLI Help Only (Not regular workflow):")
    print("  npx bmad-method --help")
    print("  uv run bmad-method --help")
    print("  (The binary is called 'bmad-method', not 'bmad')")
    print("\n" + "=" * 50)

def show_agents() -> None:
    """Show available BMAD agents for AI IDE."""
    print("\n🤖 BMAD Agents for AI IDE (Copilot, Cursor, etc.):")
    print("=" * 50)
    
    agents = {
        "@bmad-agent-pm": "Product Manager - Requirements and planning",
        "@bmad-agent-architect": "Architect - System design and architecture",
        "@bmad-agent-dev": "Developer - Code implementation",
        "@bmad-agent-ux": "UX Designer - User experience design",
        "@bmad-tea": "Test Architect - Quality and testing",
        "@bmad-analyst": "Business Analyst - Requirements analysis",
    }
    
    for agent, desc in agents.items():
        print(f"\n  {agent}")
        print(f"  → {desc}")
    
    print("\n" + "=" * 50)
    print("Usage: Type @agent-name in Copilot Chat, then ask your question")
    print("=" * 50)

def main():
    """Main menu for BMAD Loop helper."""
    print("\n" + "=" * 70)
    print("🚀 BMAD Loop Setup Assistant")
    print("=" * 70)
    
    # Check BMAD installation
    if not check_bmad_installed():
        print("\n❌ BMAD is not installed!")
        print("\nTo install BMAD, run:")
        print("  npx bmad-method install")
        print("\nThen come back to this script.")
        sys.exit(1)
    
    print("\n✅ BMAD is installed and ready to use!")
    
    # Show menu
    while True:
        print("\n" + "=" * 70)
        print("What would you like to explore?")
        print("=" * 70)
        print("\n1. List BMAD modules")
        print("2. List available workflows")
        print("3. Show common terminal commands")
        print("4. Show available AI agents")
        print("5. View deferred work log")
        print("6. Exit")
        print()
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            list_bmad_modules()
        elif choice == "2":
            list_workflows()
        elif choice == "3":
            show_commands()
        elif choice == "4":
            show_agents()
        elif choice == "5":
            show_deferred_work()
        elif choice == "6":
            print("\n✅ Thank you for exploring BMAD!")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
