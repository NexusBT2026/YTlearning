#!/usr/bin/env python3
"""
Story 1-11: How to Use bmad-execute-sprint Skill
Shows the workflow for executing any sprint with BMAD

This is how you would run the execution for Sprint 2, Sprint 3, or any sprint.
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Main entry point for sprint execution workflow."""
    
    print("🤖 BMAD Sprint Execution Workflow\n")
    print("=" * 60)
    
    # Step 1: What sprint to execute?
    print("\nStep 1: Choose which sprint to execute")
    print("-" * 60)
    print("Options:")
    print("  sprint-1  : BMAD Foundation (Stories 1-1 to 1-3)")
    print("  sprint-2  : Planning Phase (Stories 1-4 to 1-6)")
    print("  sprint-3  : Design Phase (Stories 1-7 to 1-9)")
    print("  sprint-4  : ... (continue pattern for Sprints 4-8)")
    print()
    
    sprint_choice = input("Enter sprint to execute (e.g., sprint-2): ").strip()
    
    if not sprint_choice.startswith("sprint-"):
        print("❌ Invalid sprint name. Must be 'sprint-N'")
        return
    
    # Step 2: Run bmad-execute-sprint
    print(f"\nStep 2: Executing {sprint_choice} with bmad-execute-sprint")
    print("-" * 60)
    print(f"Running command: python _bmad/scripts/execute_sprint.py {sprint_choice}\n")
    
    try:
        # Run the execute_sprint.py script
        result = subprocess.run(
            ["python", "_bmad/scripts/execute_sprint.py", sprint_choice],
            capture_output=False,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print("\n✅ Sprint execution completed successfully")
            print("\nGenerated artifacts:")
            print(f"  • {sprint_choice}-execution-report.yaml")
            print(f"  • {sprint_choice}-production-checklist.md")
        else:
            print("\n❌ Sprint execution failed")
            return
    
    except Exception as e:
        print(f"\n❌ Error running sprint execution: {e}")
        return
    
    # Step 3: Validate results
    print("\nStep 3: Understanding the execution report")
    print("-" * 60)
    print("The YAML report shows:")
    print("  • Status of each story (ready / at-risk)")
    print("  • Which components exist (script, code, assets)")
    print("  • Overall sprint status")
    print()
    
    # Step 4: Next steps
    print("Step 4: Next steps")
    print("-" * 60)
    print("If status = READY-FOR-PRODUCTION:")
    print("  → All stories are ready to record")
    print("  → Use sprint-{N}-production-checklist.md as recording guide")
    print()
    print("If status = AT-RISK:")
    print("  → Some stories are missing components")
    print("  → Review the report to see what's missing")
    print("  → Use bmad-quick-dev skill to create missing files")
    print()
    
    print("=" * 60)
    print(f"✅ {sprint_choice} execution workflow complete!")
    print()


if __name__ == "__main__":
    main()
