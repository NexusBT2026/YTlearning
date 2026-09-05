# Understanding the BMAD Loop — Deep Dive

This guide provides additional context and explanation for users who want to understand the BMAD Loop in more depth.

---

## What is the BMAD Loop?

The **BMAD Loop** is the automation engine that runs inside your VS Code editor. It's the orchestrator that transforms BMAD from a passive framework into an active development assistant.

Think of it as a project manager that:
- Understands your codebase
- Guides you through structured workflows
- Tracks your progress
- Adapts to changes
- Keeps everything organized

---

## How Does It Work?

### The 3-Part System

**1. BMAD Agent Chat** (Interactive)
- Runs inside VS Code
- You type commands to BMAD agents
- Get real-time responses and guidance
- Great for brainstorming and decision-making

**2. BMAD Skills** (Automation)
- Self-contained workflows
- Run when you invoke them
- Examples: `bmad-loop-setup`, `bmad-help`, `bmad-plan`, `bmad-design`, `bmad-dev`
- Each skill produces outputs and updates your tracking files

**3. Sprint Status Log** (Tracking)
- File: `_bmad-output\implementation-artifacts\sprint-status.yaml`
- Records every plan, design, and development decision
- Helps you track progress across sprints
- Created automatically when you run BMAD skills

### The Flow

```
You open Agent Chat (Ctrl+Shift+P)
        ↓
You run a skill ("use the bmad-loop-setup skill")
        ↓
BMAD executes the skill inside your project
        ↓
Outputs are saved to _bmad-output/
        ↓
Deferred work log is updated with progress
        ↓
You continue building with BMAD guidance
```

---

## Why Does It Matter?

### Without BMAD Loop
- You manually create requirements
- You manually track what's done vs. what's blocked
- You manually coordinate between planning/design/dev
- Team memory lives only in your head
- Progress tracking is scattered across files

### With BMAD Loop
- BMAD prompts guide you through each phase
- All decisions are documented in one log
- Progress is tracked automatically
- Team memory is preserved in the deferred work log
- You can return to your project 6 months later and know exactly where you left off

---

## Key Concepts

### BMAD Skills ≠ Terminal Commands

**This DOES NOT work:**
```bash
uv run bmad plan              # ❌ No 'bmad' binary
uv run bmad-method plan       # ❌ Also not a valid command
```

**This DOES work:**
```
1. Press Ctrl+Shift+P
2. Search: "BMAD: Launch Agent"
3. Type in chat: "use the bmad-loop-setup skill"
4. BMAD executes it inside the agent
```

**For CLI help only (not regular workflow):**
```bash
npx bmad-method --help        # ✅ Check CLI version/help
uv run bmad-method --help     # ✅ Alternative
```

Why the difference?
- BMAD skills need to interact with your VS Code workspace
- They need access to your project files in real-time
- They need to write outputs and update tracking files
- Terminal is just for running Python scripts with `uv run`
- The BMAD CLI (`bmad-method`) is for help/debugging only

### BMAD Loop vs. Other Agents

**BMAD Agent (Chat)** = One-way help
- You ask a question
- Agent gives advice
- No persistent tracking

**BMAD Loop** = Full orchestrator
- Skills automatically track progress
- Deferred work log is updated
- Next time you open your project, BMAD knows where you left off
- Like having a memory of your entire development journey

---

## Common Questions

### Q: Can I run BMAD commands in PowerShell or Bash?

**A:** No. BMAD skills only run in VS Code Agent Chat. If you try them in terminal, you'll get "program not found" error.

The only terminal command you use is `uv run workflow_test.py` to test your Python environment.

### Q: What's the difference between bmad-loop-setup and bmad-help?

**A:** 
- **bmad-loop-setup**: One-time skill that activates the Loop Orchestrator. Run it once per project.
- **bmad-help**: Shows you available workflows and next steps. Run anytime you need guidance.

### Q: Where are my outputs saved?

**A:** Everything goes to `_bmad-output/` folder:
- `sprint-status.yaml` — Your progress log
- `product-brief.md` — Generated during planning
- `architecture.md` — Generated during design
- Other workflow outputs

### Q: Can I edit the deferred work log manually?

**A:** You can read it anytime with:

**Windows PowerShell:**
```powershell
Get-Content _bmad-output\implementation-artifacts\sprint-status.yaml
```

**Linux/macOS/WSL:**
```bash
cat _bmad-output/implementation-artifacts/sprint-status.yaml
```

Or just open it in VS Code's file explorer. Don't manually edit it unless you know what you're doing — let BMAD skills manage it.

### Q: What happens if I run bmad-loop-setup twice?

**A:** It's safe. BMAD will recognize the Loop is already active and won't duplicate things. But you only need to run it once per project.

### Q: Why do I need uv run for Python scripts?

**A:** Because your Python environment is in Conda. `uv run` activates the correct environment and runs your script in that context. It's safer and more consistent than bare `python`.

---

## Next Steps

After running `bmad-loop-setup`:

1. **Open deferred work log** (in VS Code file explorer)
2. **Run bmad-help** (in Agent Chat) to see available workflows
3. **Run bmad-plan** (in Agent Chat) to start planning your project
4. **Run bmad-design** (in Agent Chat) to create architecture
5. **Run bmad-dev** (in Agent Chat) to start development

Each step builds on the previous one, with the deferred work log tracking everything.

---

## Troubleshooting

### Problem: "BMAD: Launch Agent" doesn't appear in Command Palette

**Solution:** Make sure you have:
- VS Code open in your BMAD project folder
- GitHub Copilot extension installed
- BMAD installed (check if `_bmad/` folder exists)

### Problem: Agent Chat opens but skills don't work

**Solution:** 
- Make sure you're typing: `use the [skill-name] skill`
- Example: `use the bmad-loop-setup skill`
- Not: `bmad-loop-setup` or `run bmad-loop-setup`

### Problem: Can't find deferred work log

**Solution:**
- It's only created after running a BMAD skill
- Location: `_bmad-output/implementation-artifacts/sprint-status.yaml`
- If it doesn't exist, run `bmad-help` first to create it

### Problem: My terminal keeps saying "program not found"

**Solution:** You're trying to run BMAD in terminal. Don't. Use VS Code Agent Chat instead.

---

## Learning Resources

- **Video 1-1**: BMAD Introduction
- **Video 1-2**: BMAD Installation  
- **Video 1-3**: BMAD Loop Setup (this one)
- **Video 1-4**: First BMAD Workflow

Each video builds on the previous. Make sure you've completed 1-2 before starting 1-3.
