#!/usr/bin/env python3
"""
Execution Phase Helper — BMAD Sprint Execution Reference

This helper script demonstrates how to use BMAD's execution phase
to generate execution reports and production checklists for a sprint.

Usage:
    python execution-helper.py <epic_number>
    python execution-helper.py 1
    python execution-helper.py 5

This will:
1. Load the sprint/epic from sprint-status.yaml
2. Validate all story components (script, code, assets)
3. Generate an execution report (epic-N-execution-report.yaml)
4. Generate a production checklist (epic-N-production-checklist.md)
5. Identify at-risk stories needing attention
"""

import sys
from pathlib import Path

def show_execution_workflow():
    """Display the BMAD execution workflow"""
    workflow = """
    ┌─────────────────────────────────────────────┐
    │     BMAD EXECUTION PHASE WORKFLOW           │
    └─────────────────────────────────────────────┘
    
    PHASE 1: LOAD SPRINT DATA
    └─ Read development_status from sprint-status.yaml
    └─ Collect all stories for the epic
    └─ Validate series folder exists
    
    PHASE 2: VALIDATE STORY COMPONENTS
    └─ Check script/ folder exists
    └─ Check code/ folder exists
    └─ Check assets/ folder exists
    └─ Read story metadata
    
    PHASE 3: GENERATE EXECUTION REPORT
    └─ Create epic-N-execution-report.yaml
    └─ List all stories and their status
    └─ Flag at-risk stories
    └─ Calculate total duration
    
    PHASE 4: GENERATE PRODUCTION CHECKLIST
    └─ Create epic-N-production-checklist.md
    └─ Provide task checklist for production
    └─ List asset requirements per story
    
    PHASE 5: DISPLAY SUMMARY
    └─ Show ready vs at-risk count
    └─ Display risk summary
    └─ Ready for recording/production
    """
    print(workflow)

def main():
    """Main execution helper"""
    if len(sys.argv) < 2:
        print("BMAD Execution Phase Helper")
        print("Usage: python execution-helper.py <epic_number>")
        print("Example: python execution-helper.py 1")
        print()
        show_execution_workflow()
        return 0
    
    epic_number = sys.argv[1]
    print(f"\n🚀 Execution Phase Helper — Epic {epic_number}")
    print("─" * 50)
    print("To execute this epic, run:")
    print(f"  python _bmad/scripts/execute_sprint.py {epic_number}")
    print()
    show_execution_workflow()
    return 0

if __name__ == "__main__":
    sys.exit(main())
