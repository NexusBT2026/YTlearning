# Story 1-3: BMAD Loop Setup

## 📺 Episode Overview

**Title:** BMAD Loop Setup — Completing the Installation with bmad-loop-setup

**Duration:** ~20-21 minutes  
**Difficulty:** Intermediate

This episode teaches you how to activate and use BMAD's Loop Orchestrator. You'll learn how to run BMAD skills from VS Code Agent Chat, understand the deferred work log, and get BMAD fully operational in your project.

---

## 🎯 Learning Objectives

After watching this episode, you'll:

- ✅ Understand what the BMAD Loop does
- ✅ Know that BMAD skills run in VS Code Agent Chat (not terminal)
- ✅ Navigate the `./_bmad/` folder structure
- ✅ Run BMAD skills from VS Code Agent Chat
- ✅ Use BMAD agents in Copilot Chat
- ✅ Understand the sprint status log (`sprint-status.yaml`)
- ✅ Generate workflow outputs
- ✅ Test your Python environment with `uv run`

---

## 📂 Folder Structure

```
1-3-bmad-loop-setup/
├── script/
│   └── script.md           ← Full video script & transcript
├── code/
│   └── explore_loop.py     ← Interactive BMAD explorer tool
├── assets/
│   └── (placeholder for images/diagrams)
└── README.md               ← This file
```

---

## 🔄 What is the BMAD Loop?

The **BMAD Loop** is BMAD's automation orchestrator. Think of it as a project manager built into your IDE.

### What it does:

1. **Reads your code** — Understands what you've built
2. **Runs workflows** — Guides you through Planning, Design, Development, Review, Verify
3. **Tracks progress** — Keeps a sprint status log (`sprint-status.yaml`)
4. **Adapts to changes** — Adjusts as your project evolves

### Why it matters:

Without structure, AI can be chaotic. The Loop gives you **structured guidance** so you can build confidently without losing context or forgetting important steps.

---

## 🤖 Agent Chat vs Terminal Commands

**BMAD skills run ONLY in VS Code Agent Chat. Terminal commands DO NOT WORK.**

### Agent Chat
```
Press Ctrl+Shift+P
        ↓
Search "BMAD: Launch Agent"
        ↓
Type in chat: "use the bmad-loop-setup skill"
        ↓
BMAD executes the skill
```

**How to use:**
1. Open VS Code in your BMAD project
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type: `BMAD: Launch Agent`
4. Pick any agent (they all share the same Loop)
5. In the chat, type: `use the bmad-loop-setup skill`

**Skills available:**
- `use the bmad-loop-setup skill` — Activate the Loop
- `use the bmad-help skill` — Get guidance and available workflows
- `use the bmad-plan skill` — Run planning workflow
- `use the bmad-design skill` — Run design workflow

### Terminal Commands (Testing Only)
```bash
# ONLY for testing your Python environment
uv run workflow_test.py
```

**Important:** Do NOT try `uv run bmad plan` or similar. These commands do not exist and will fail with "program not found".

---

## 📁 BMAD Folder Structure Explained

When you installed BMAD with `npx bmad-method install`, it created this structure:

```
your-project/
├── _bmad/                      ← BMAD core (don't edit directly)
│   ├── config.toml             ← Main configuration
│   ├── config.user.toml        ← Your custom settings
│   ├── core/                   ← Core workflows (Planning, Design, etc.)
│   │   ├── config.yaml
│   │   ├── workflows/
│   │   └── agents/
│   ├── bmb/                    ← BMAD Builder (custom agents)
│   ├── tea/                    ← Test Architect module
│   ├── custom/                 ← Your extensions
│   └── scripts/                ← Helper scripts
│
├── _bmad-output/               ← All workflow outputs go here
│   ├── planning-artifacts/
│   │   ├── product-brief.md
│   │   ├── prfaq.md
│   │   └── prd.md
│   ├── implementation-artifacts/
│   ├── sprint-status.yaml      ← Progress tracking
│   └── ...
│
└── your-code/                  ← Your Python files
    ├── main.py
    ├── modules/
    └── ...
```

### Key Folders:

- **`_bmad/`** — BMAD installation (read-only, customizable)
- **`_bmad-output/`** — All workflow outputs and tracking
- **`sprint-status.yaml`** — Your project's progress log

---

## 💻 Running Workflows in VS Code Agent Chat

### Step 1: Open the Agent

Press `Ctrl+Shift+P` and search for `BMAD: Launch Agent`

You'll see options like:
- Chat: Open Chat (bmad-agent-analyst)
- Chat: Open Chat (bmad-agent-architect)
- Chat: Open Chat (bmad-agent-builder)
- Chat: Open Chat (bmad-agent-dev)
- Chat: Open Chat (bmad-agent-pm)

Pick any one. They all connect to the same BMAD Loop.

### Step 2: Run a Skill

In the chat box, type the skill name:

```
use the bmad-loop-setup skill
```

Press Enter. BMAD will execute it.

### Step 3: Check the Outputs

After the skill completes:
1. Look in VS Code's file explorer
2. Navigate to `_bmad-output/`
3. You'll see generated files there

### Available Skills

```
use the bmad-loop-setup skill    ← Run once to activate the Loop
use the bmad-help skill          ← See available workflows
use the bmad-plan skill          ← Planning workflow
use the bmad-design skill        ← Design workflow
use the bmad-dev skill           ← Development workflow
```

### Viewing Your Outputs

In VS Code:
1. Open file explorer (Ctrl+Shift+E)
2. Navigate to `_bmad-output/`
3. Click on any file to view it

Files you'll see:
- `sprint-status.yaml` — Your progress log
- `product-brief.md` — Generated after planning
- Other workflow artifacts

---

## 🧠 Using Copilot Chat (Optional)

After activating the Loop, you can also use BMAD agents in Copilot Chat for interactive guidance:

**Open Copilot Chat:**
```
Windows/Linux: Ctrl + Shift + I
Mac: Cmd + Shift + I
```

**Available agents:**
- `@bmad-agent-pm` — Product Manager
- `@bmad-agent-architect` — System Architect
- `@bmad-agent-dev` — Developer
- `@bmad-agent-ux` — UX Designer

**Example:**
```
@bmad-agent-pm Help me define requirements for my project
```

The agents provide interactive guidance, but BMAD skills (which automate workflows) run in Agent Chat instead.

---

## 📊 Understanding the Sprint Status Log

The file `_bmad-output/sprint-status.yaml` tracks your entire project:

```yaml
project_name: Python YouTube Series
last_updated: 2026-08-01
status: planning

sprints:
  sprint_1:
    name: "BMAD Foundation"
    stories:
      - 1-1-what-is-bmad
      - 1-2-bmad-setup
      - 1-3-bmad-loop-setup

development_status:
  1-1-what-is-bmad:
    status: ready-for-dev
    assigned_to: ~
    started: ~
    completed: ~
    
  1-2-bmad-setup:
    status: ready-for-dev
    assigned_to: ~
    started: ~
    completed: ~
```

**Check your progress:**
```bash
cat _bmad-output/sprint-status.yaml
```

**What the statuses mean:**
- ⏳ `backlog` — Not started yet
- 🔵 `ready-for-dev` — Ready to begin
- 🟡 `in-progress` — Currently being worked on
- 🟠 `review` — Waiting for review
- ✅ `done` — Complete

---

## 🚀 Running Your First BMAD Skill

### Step 1: Open Agent Chat

Press `Ctrl+Shift+P` and search: `BMAD: Launch Agent`

### Step 2: Run the Setup Skill

Type in the chat:
```
use the bmad-loop-setup skill
```

### Step 3: Wait for Completion

BMAD will:
1. Install the Loop Orchestrator
2. Configure project hooks
3. Activate the automation engine
4. Create `_bmad-output/sprint-status.yaml`

You'll see a success message in the chat.

### Step 4: Check Your Outputs

In VS Code file explorer:
1. Open `_bmad-output/` folder
2. You'll see:
   - `sprint-status.yaml` — Your progress log
   - Other workflow files

That's it! The Loop is now active. 🎉

---

## 🧪 Interactive Explorer Tool

We've included a Python script to explore your BMAD installation:

```bash
python code/explore_loop.py
```

**What it does:**
1. Lists available BMAD modules
2. Shows available workflows
3. Displays common terminal commands
4. Shows available AI agents
5. Displays your deferred work log
6. Provides an interactive menu

Run it to get familiar with what's available in your BMAD setup.

---

## 📖 Full Video Transcript

See `script/script.md` for the complete video script with detailed explanations and timestamps.

---

## 🎯 Available BMAD Skills

Run any of these in Agent Chat by typing:

### Loop Setup
```
use the bmad-loop-setup skill
```
- Activates the Loop Orchestrator (run once per project)
- Creates deferred work log

### Getting Help
```
use the bmad-help skill
```
- Shows available workflows
- Provides guidance
- Explains next steps

### Planning
```
use the bmad-plan skill
```
- Generates Product Brief
- Generates PRFAQ (press release FAQ)
- Generates PRD (requirements)

### Design
```
use the bmad-design skill
```
- Generates architecture document
- System design specifications
- API specifications

### Development
```
use the bmad-dev skill
```
- Executes story implementation
- Generates code
- Sets up testing

All outputs go to `_bmad-output/` and are tracked in `sprint-status.yaml`

---

## 🔗 Quick Reference

### Opening BMAD Agent Chat
```
Ctrl+Shift+P  →  Search "BMAD: Launch Agent"  →  Pick any agent
```

### Running Skills (in Agent Chat)
```
use the bmad-loop-setup skill
use the bmad-help skill
use the bmad-plan skill
use the bmad-design skill
```

### Viewing Outputs
```
VS Code → File Explorer → _bmad-output/
```

### Checking Progress
```
VS Code → File Explorer → _bmad-output/ → sprint-status.yaml
```

### Testing Python Environment
```bash
# Only this terminal command works
uv run workflow_test.py
```

### ⚠️ Commands That DON'T Work
```bash
# These WILL FAIL - Don't use them
uv run bmad --help          # ❌ Program not found (No 'bmad' binary (it's called 'bmad-method'))
uv run bmad plan            # ❌ Program not found
uv run bmad design          # ❌ Program not found
uv run bmad dev             # ❌ Program not found
```

**For BMAD skills:** Use VS Code Agent Chat instead (Ctrl+Shift+P)

**For BMAD CLI help/debugging:** Use `bmad-method` (see section below)

### ✅ BMAD CLI Commands (For Help & Debugging)

If you need help with BMAD itself or want to check the CLI, the correct binary is `bmad-method`:

```bash
# ✅ All of these work:
npx bmad-method --help              # Recommended - installs and runs
npm exec bmad-method --help         # Alternative if npx fails
uv run bmad-method --help           # Using uv
bmad-method --help                  # If installed globally
```

**Why `bmad` doesn't work:** The binary is named `bmad-method`, not `bmad`. This is the JavaScript CLI executable.

**Important:** CLI help is for reference only. Day-to-day BMAD work happens in Agent Chat.

---

## 🚨 Troubleshooting

### "BMAD: Launch Agent" doesn't appear in Command Palette

**Check:**
- VS Code is open in your project folder
- GitHub Copilot extension is installed
- BMAD is installed (check if `_bmad/` folder exists)

### Terminal says: "error: Failed to spawn: `bmad`: program not found"

**This is expected.** There is no `bmad` binary — it's called `bmad-method`.

**For BMAD skills:** Use VS Code Agent Chat instead (Ctrl+Shift+P → BMAD: Launch Agent)

**For CLI help:** Use `npx bmad-method --help` or `uv run bmad-method --help`

### Deferred work log not found

**This is normal.** The log is created when you run your first BMAD skill.

**Solution:** Run `use the bmad-loop-setup skill` in Agent Chat. Then check `_bmad-output/sprint-status.yaml`

### "Can't find @bmad-agent-pm in Copilot Chat"

**Solution:**
- Restart VS Code
- Make sure GitHub Copilot extension is installed
- Verify BMAD is installed with `ls _bmad/`

### Nothing happens when I run a skill

**Check:**
- You're typing the exact command: `use the [skill-name] skill`
- Example: `use the bmad-help skill` (not `bmad-help` or `run bmad-help`)
- You're in the Agent Chat window (not terminal)
- You pressed Enter

### I want to check Python is installed

**Use:**
```bash
uv run workflow_test.py
```

This confirms your Python environment, uv, and Node.js are working.

### I want to check the BMAD CLI version

**Use:**
```bash
npx bmad-method --version
```

Or:
```bash
uv run bmad-method --version
```

Note: The binary is `bmad-method`, not `bmad`.

---

## 🎬 Video Information

**YouTube Link:** [YouTube Link](https://www.youtube.com/watch?v=mNyn5rOIQ_E)²
**Published:** 2026-08-01
**Status:** ✅ Published

### Timestamps
00:00 – Intro
00:30 – Where BMAD skills must be executed
00:55 – Opening the BMAD Agent in VS Code
01:25 – Running the bmad-loop-setup skill
17:25 – Testing the loop with a Python workflow
18:52 – Running uv + BMAD automation
20:04 – Recap & next video

---

## 🚀 What's Next?

### Story 1-4: Product Brief Deep Dive
In the next episode, you'll learn:
- What a Product Brief is and why it matters
- How to write one that guides your entire project
- Using BMAD's Product Brief template
- Connecting Product Brief to your actual code

---

## ✅ Checklist for Completion

- [ ] Watch the full video
- [ ] Read `script/script.md`
- [ ] Run `python code/explore_loop.py`
- [ ] Run BMAD skills in Agent Chat
- [ ] View `_bmad-output/product-brief.md`
- [ ] Check `_bmad-output/sprint-status.yaml`
- [ ] Try using `@bmad-agent-pm` in Copilot Chat
- [ ] Ready for Story 1-4

---

## 💬 Key Concepts

- **BMAD Loop** = Automation orchestrator that runs in VS Code Agent Chat
- **BMAD Skills** = Workflows you run by typing commands in Agent Chat
- **Agent Chat** = VS Code Copilot Chat where BMAD runs (Ctrl+Shift+P)
- **Sprint Status Log** = Your project's progress tracker (`_bmad-output/sprint-status.yaml`)
- **Modules** = BMAD extensions (core, tea, bmb, custom)
- **Terminal** = Only for testing with `uv run workflow_test.py`

### Important
- ❌ BMAD skills do NOT work in terminal
- ✅ BMAD skills run in VS Code Agent Chat
- ✅ Commands like `uv run bmad plan` will fail with "program not found"
- ✅ Use `Ctrl+Shift+P` to open Agent Chat and run skills

---

**Ready to plan your first project? Watch Story 1-4 next!** 🎬

---

*Last Updated: 2026-08-01*  
*Status: ✅ Ready for Publishing*
