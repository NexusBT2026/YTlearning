#!/usr/bin/env python3
"""
Story 1-11: Example Output from bmad-execute-sprint
Shows what Sprint 2 execution output looks like

This is real output from running: python _bmad/scripts/execute_sprint.py sprint-2
"""

# ==============================================================================
# CONSOLE OUTPUT WHEN EXECUTING SPRINT 2
# ==============================================================================

output = """
🚀 Executing sprint-2...

✅ Sprint: BMAD Series (Episodes 4–6)
✅ Stories: 3

📖 Processing: 1-4-product-brief
   ✅ Status: READY
   ⏱️ Duration: 20-30 minutes
   📝 Script: ✅
   💻 Code: ✅
   📋 Assets: ✅

📖 Processing: 1-5-prfaq-prd
   ✅ Status: READY
   ⏱️ Duration: 40-50 minutes
   📝 Script: ✅
   💻 Code: ✅
   📋 Assets: ✅

📖 Processing: 1-6-architecture
   ✅ Status: READY
   ⏱️ Duration: 25-35 minutes
   📝 Script: ✅
   💻 Code: ✅
   📋 Assets: ✅

✅ Execution report saved: C:\\...\\execution-artifacts\\sprint-2-execution-report.yaml
✅ Production checklist saved: C:\\...\\execution-artifacts\\sprint-2-production-checklist.md

============================================================
SPRINT EXECUTION REPORT
============================================================

📌 Sprint: BMAD Series (Episodes 4–6)
🎯 Focus: Completing the planning phase episodes
📊 Stories: 3 total
   ✅ Ready: 3
   ⚠️ At-Risk: 0
⏱️ Total Duration: 85-115 minutes
🚦 Status: READY-FOR-PRODUCTION
✅ Outcome: All stories ready to record immediately

📋 Story Details:

  • Product Brief (1-4)
    Duration: 20-30 minutes
    Status: ready
    Components: ✅ Script ✅ Code ✅ Assets

  • PRFAQ + PRD (1-5)
    Duration: 40-50 minutes
    Status: ready
    Components: ✅ Script ✅ Code ✅ Assets

  • Architecture (1-6)
    Duration: 25-35 minutes
    Status: ready
    Components: ✅ Script ✅ Code ✅ Assets

============================================================
📁 Execution Artifacts Generated:
   • sprint-2-execution-report.yaml (machine-readable)
   • sprint-2-production-checklist.md (human-readable)
============================================================
"""

# ==============================================================================
# WHAT THE OUTPUT MEANS
# ==============================================================================

interpretation = """
When you see this output, here's what it means:

✅ READY = Story has all required files:
   • script/script.md exists
   • code/ folder has examples
   • assets/ASSETS.md exists
   • README.md has learning guide

⚠️ AT-RISK = Story is missing components

🚦 Status: READY-FOR-PRODUCTION means:
   → All stories pass validation
   → All stories have complete content
   → Videos are ready to record

Next steps:
1. Read the production checklist (sprint-2-production-checklist.md)
2. Follow the recording guide
3. Record all 3 episodes
4. Upload to YouTube
5. Update sprint-status.yaml with 'done' status
"""

# ==============================================================================
# HOW TO USE THESE ARTIFACTS
# ==============================================================================

artifacts_usage = """
Two files are created by bmad-execute-sprint:

1. sprint-2-execution-report.yaml
   - Machine-readable format
   - Used by BMAD tools for validation
   - Contains detailed component breakdown
   - Shows pass/fail for each quality gate

2. sprint-2-production-checklist.md
   - Human-readable format
   - Use this as your recording guide
   - Contains timestamps for each episode
   - Lists production requirements
   - Provides recording tips

HOW TO USE THEM:
1. Open sprint-2-production-checklist.md in VS Code
2. Use it as a checklist while recording
3. Reference the timings for each episode
4. Check off items as you complete them
5. When all items are ✅, upload to YouTube
"""

# ==============================================================================
# APPLYING THE SAME PATTERN TO SPRINT 3
# ==============================================================================

sprint3_pattern = """
To execute Sprint 3, you would:

1. Open BMAD Agent Chat (Ctrl + Shift + P → BMAD: Launch Agent)

2. Type: "use the bmad-execute-sprint skill to execute sprint-3"

3. BMAD will populate Sprint 3 stories:
   - Story 1-7: Epics & Stories
   - Story 1-8: Design System
   - Story 1-9: UX Prototyping

4. Same output as Sprint 2:
   ✅ Sprint 3: status = READY-FOR-PRODUCTION
   ✅ All 3 stories READY
   ✅ Production checklist generated

5. Follow the same recording workflow

The pattern repeats identically for Sprints 4, 5, 6, 7, and 8.
"""

# ==============================================================================
# POSSIBLE ERROR SCENARIOS
# ==============================================================================

error_scenarios = """
If you see: ⚠️ AT-RISK

Possible reasons:
1. Episode folder doesn't exist
   → Create it manually or use bmad-quick-dev

2. Script file missing
   → Use bmad-create-story or bmad-dev-story to generate

3. Code examples missing
   → Add example files to code/ folder

4. README missing
   → Use bmad-dev-story to create comprehensive README

5. Assets checklist incomplete
   → Update assets/ASSETS.md with production requirements

How to fix:
→ Use the BMAD Agent Chat
→ Type: "create the missing content for story 1-4"
→ BMAD will populate the missing files
→ Run bmad-execute-sprint again to validate
"""

# ==============================================================================
# KEY TAKEAWAY
# ==============================================================================

key_takeaway = """
The bmad-execute-sprint skill is the core of BMAD's execution engine.

It:
1. Analyzes sprint structure
2. Validates content completeness
3. Identifies at-risk stories
4. Generates production artifacts
5. Creates human-readable checklists

Once you understand how to run bmad-execute-sprint for one sprint,
you can apply it to every sprint in your project.

This is why Sprint 2 execution (this video) is the final setup episode.
After this, you have everything you need to execute all remaining sprints.
"""

if __name__ == "__main__":
    print(output)
    print("\n" + "="*80 + "\n")
    print(interpretation)
