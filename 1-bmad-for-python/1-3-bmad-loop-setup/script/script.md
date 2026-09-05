# BMAD Loop Setup — Full Video Script

**Video Title:** BMAD Loop Setup — Completing the Installation with bmad-loop-setup

**Duration:** ~20-21 minutes  
**Target Audience:** Python developers with BMAD installed

---

## 🎯 INTRO

"Welcome back! In the last video we installed the BMAD Method inside a fresh Python project.
Today we're completing the setup by running the bmad-loop-setup skill — and I'll show you exactly where to run it, because BMAD skills do not run in the terminal.
They run inside the BMAD Agent Chat in VS Code."

---

## SECTION 1 — Where BMAD Skills Must Be Executed

"Before we start, this is important:
BMAD skills like bmad-loop-setup, bmad-help, or bmad-builder do not run in PowerShell, CMD, or Bash.
If you try them in the terminal, you'll get an error."

"BMAD skills run inside the BMAD Agent Chat in VS Code.
So let me show you how to open the agent."

---

## SECTION 2 — Opening the BMAD Agent in VS Code

"Open VS Code in your BMAD project folder.
Then press Ctrl + Shift + P to open the Command Palette."

"Search for:
`BMAD: Launch Agent`

or pick any agent like:
- `Chat: Open Chat (bmad-agent-analyst)`
- `Chat: Open Chat (bmad-agent-architect)`
- `Chat: Open Chat (bmad-agent-builder)`
- `Chat: Open Chat (bmad-agent-dev)`
- `Chat: Open Chat (bmad-agent-pm)`

All BMAD agents share the same loop, so it doesn't matter which one you open."

---

## SECTION 3 — Running the bmad-loop-setup Skill

"Now that the agent chat is open, we can run the setup skill."

In the BMAD Agent Chat (NOT the terminal):

```
use the bmad-loop-setup skill
```

"This installs the Loop Orchestrator, configures project hooks, and activates BMAD's automation engine.
Once this finishes, BMAD becomes fully operational."

---

## SECTION 4 — Testing the Loop with a Python Workflow

"Now that the loop is active, let's test it with a simple Python workflow."

Create a file: `workflow_test.py`

```python
def main():
    print("BMAD Loop test successful!")

if __name__ == "__main__":
    main()
```

"BMAD prefers running Python scripts using uv run, so let's do that."

Terminal:

```bash
uv run workflow_test.py
```

"This confirms that our environment, BMAD installation, and loop setup are all working together."

---

## SECTION 5 — Running a BMAD Automation Skill (optional but recommended)

"Let's trigger a simple BMAD automation skill to confirm the loop is active."

In the BMAD Agent Chat:

```
use the bmad-help skill
```

"If the loop is installed correctly, BMAD will respond with guidance, available workflows, and next steps."

---

## SECTION 6 — Recap & Next Video

"Quick recap:
We opened the BMAD Agent, ran the loop setup skill, activated the automation engine, tested Python workflows with uv, and confirmed BMAD is ready to run AI-driven development tasks."

"In the next video, we'll explore BMAD workflows for Python — planning, architecture, debugging, and development using AI agents."

"If this helped you, leave a like and subscribe. And tell me in the comments what BMAD topic you want next."

---

## 📌 Timestamps

- 00:00 – Intro
- 00:30 – Where BMAD skills must be executed
- 00:55 – Opening the BMAD Agent in VS Code
- 01:25 – Running the bmad-loop-setup skill
- 17:25 – Testing the loop with a Python workflow
- 18:52 – Running uv + BMAD automation
- 20:04 – Recap & next video

---

## Resources & Links

- Official BMAD GitHub: [BMAD GitHub](https://github.com/bmad-code-org/BMAD-METHOD)
- **GitHub Repository:** [YTlearning GitHub Repository](https://github.com/NexusBT2026/YTlearning.git)
- **YouTube Channel:** [YTlearning YouTube Channel](https://www.youtube.com/channel/UCClukBkgrmBj7svPIrMqvDg)
- **Next Episode:** Story 1-4 (BMAD Workflow for Python)

---

## Requirements:
- BMAD installed (Story 1-1 and 1-2)
- Node.js installed
- Python 3.10 installed
- Conda installed

---

![BMAD Loop Setup Phase](../assets/BMAD_Loop_Setup.png)
