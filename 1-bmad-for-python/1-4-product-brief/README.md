# Story 1-4: Product Brief — Creating Your Project Vision

## 📺 Episode Overview

**Title:** BMAD Planning Phase — Creating the Product Brief (First Required Step)

**Duration:** 13-14 minutes  
**Difficulty:** Beginner  
**Prerequisites:** Stories 1-1, 1-2, 1-3

This episode teaches you how to create a Product Brief — the foundation of the entire BMAD planning workflow. You'll learn what a brief is, why it matters, and how to answer the 8 key questions that guide your entire project.

---

## 🎯 Learning Objectives

After watching this episode, you'll:

- ✅ Understand what a Product Brief is and why it's the first BMAD planning step
- ✅ Know the 8 questions BMAD asks to create a comprehensive brief
- ✅ See how to answer each question with real project examples
- ✅ Understand what a completed Product Brief looks like
- ✅ Know how the brief flows into PRFAQ, PRD, and Architecture
- ✅ Be able to create your own Product Brief for any project
- ✅ Run the `bmad-product-brief` skill in VS Code Agent Chat

---

## 📂 Folder Structure

```
1-4-product-brief/
├── script/
│   └── script.md           ← Full video script & transcript
├── code/
│   ├── brief-template.md   ← Blank template for your own project
│   └── brief-example.md    ← Completed example (Python YouTube Series)
├── assets/
│   └── (placeholder for images/diagrams)
└── README.md               ← This file
```

---

## 📋 What is a Product Brief?

A **Product Brief** is a short (1-2 page) document that captures your project's vision, audience, and scope.

### What it contains:

1. **What** — Project name and high-level vision
2. **Who** — Target audience and users
3. **Why** — The problem you're solving
4. **How** — Your high-level solution approach
5. **Features** — Key capabilities and features
6. **Scope** — What's explicitly NOT included
7. **Success** — How you'll measure success
8. **Purpose** — Why this project exists and matters

### Why it matters:

- **Foundation** — Everything else in BMAD builds on this brief
- **Alignment** — Ensures your team is solving the right problem for the right people
- **Scope control** — Prevents scope creep by defining boundaries
- **Quick reference** — Teams can refer to it throughout development
- **Validation** — Before investing in PRD/Architecture, test the idea with PRFAQ (next episode)

---

## 🤖 Running the Product Brief Skill

**BMAD skills run ONLY in VS Code Agent Chat. Do NOT use terminal.**

### How to use the `bmad-product-brief` skill:

1. **Open Agent Chat:**
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type: `BMAD: Launch Agent`
   - Pick any agent (they all share the same Loop)

2. **Run the skill:**
   - In the chat, type exactly:
   ```
   use the bmad-product-brief skill
   ```

3. **Answer the questions:**
   - BMAD will ask 8 questions one at a time
   - Type your answer for each question
   - Your answers guide the brief generation

4. **Review the output:**
   - BMAD creates: `_bmad-output/planning-artifacts/product-brief/brief.md`
   - Open it in VS Code to review

---

## ❓ The 8 Product Brief Questions

When you run the `bmad-product-brief` skill, BMAD asks these questions:

### Question 1: What is the name of the project?
**Purpose:** Establish the project identity  
**Example:** "Python YouTube Series — Real Projects for Beginners"

### Question 2: Who is this project for?
**Purpose:** Define your target audience  
**Example:** "Beginners and intermediate developers who want to learn Python through real, practical projects instead of basic tutorials"

### Question 3: What problem does this project solve?
**Purpose:** Justify why your project matters  
**Example:** "Most Python tutorials only teach syntax and simple examples. Beginners struggle to build real projects and understand how Python is used in actual development"

### Question 4: What does the product do in one sentence?
**Purpose:** Capture the solution simply  
**Example:** "A practical Python video series that teaches real development through mini-projects, APIs, websockets, ML basics, and useful tools"

### Question 5: What are the key features?
**Purpose:** Define core capabilities  
**Example:** "Realistic mini-projects, API usage, websocket clients, ML basics, logging, error-handling, and beginner-friendly explanations"

### Question 6: What is out of scope for version 1?
**Purpose:** Set boundaries and prevent scope creep  
**Example:** "No advanced machine learning, no private trading systems, and no paid or proprietary code"

### Question 7: What are the success criteria?
**Purpose:** Define how you'll measure success  
**Example:** "Viewers can build real Python projects, understand how to structure code, and gain confidence to create their own tools"

### Question 8: Why does this project exist?
**Purpose:** Capture the deeper motivation  
**Example:** "To help beginners learn Python the way real developers use it — through practical, useful projects instead of basic syntax tutorials"

---

## 📁 BMAD Planning Workflow

The Product Brief is the first step in BMAD's planning sequence:

```
Product Brief (You are here - Story 1-4)
    ↓
PRFAQ (Story 1-5) — Stress-test with press release + FAQ
    ↓
PRD (Story 1-5) — Detailed requirements
    ↓
Architecture (Story 1-6) — Technical design decisions
    ↓
Epics & Stories (Story 1-7) — Break down into implementation
    ↓
Implementation Readiness (Story 1-8) — Final validation
    ↓
Sprint Planning (Story 1-9) — Build schedule
    ↓
Sprint Execution (Stories 1-10, 1-11) — Build and iterate
```

Each step builds on the previous one.

---

## 💻 Agent Chat vs Terminal Commands

**IMPORTANT:** BMAD skills run ONLY in VS Code Agent Chat. Do NOT use terminal.

### ✅ What Works: Agent Chat
```
Press Ctrl+Shift+P
        ↓
Search "BMAD: Launch Agent"
        ↓
Type: "use the bmad-product-brief skill"
        ↓
BMAD executes the skill
```

### ❌ What Doesn't Work: Terminal Commands
```bash
# These will all FAIL with "program not found"
uv run bmad brief               # ❌ No such command
bmad-product-brief              # ❌ No such command
uv run bmad plan                # ❌ No such command
```

**Terminal is ONLY for testing:**
```bash
# This works - testing your Python environment
uv run workflow_test.py
```

---

## 🔧 How to Use This Episode

1. **Watch the full video**
   - Follow along as we create a Product Brief for the Python YouTube Series

2. **Download the template**
   - Get `code/brief-template.md` from this episode folder
   - This is a blank template you can adapt for your own project

3. **Run the skill yourself**
   - Open VS Code Agent Chat
   - Run `use the bmad-product-brief skill`
   - Answer the 8 questions for YOUR project

4. **Compare to the example**
   - Look at `code/brief-example.md` from this episode
   - See how a completed brief looks
   - Use it as inspiration for your own answers

5. **Review your generated brief**
   - BMAD creates the brief in `_bmad-output/planning-artifacts/product-brief/`
   - This becomes the foundation for your next planning phase

6. **Move to Story 1-5**
   - With your brief complete, you're ready for PRFAQ + PRD

---

## 📊 Understanding Your Generated Brief

After running the `bmad-product-brief` skill, BMAD creates a markdown file that:

- **Captures your vision** — One clear statement of what you're building
- **Defines your audience** — Specific groups of people who will use it
- **Identifies the problem** — What pain point you're solving
- **Shows your solution** — High-level approach without implementation details
- **Lists key features** — What makes your project unique
- **Sets boundaries** — What's explicitly NOT included
- **Establishes success** — How you'll know you succeeded
- **Connects to next steps** — Links to PRFAQ, PRD, and Architecture

This document becomes a reference point throughout your entire project.

---

## 🔄 Product Brief Concepts

### Brief vs PRD

- **Brief** = Short vision statement (1-2 pages, answers "why should we build this?")
- **PRD** = Detailed requirements (5-10 pages, answers "what exactly are we building?")

Use Brief first to validate the idea is worth pursuing. Then use PRD for detailed planning.

### Brief vs PRFAQ

- **Brief** = Internal planning document (what your team needs to know)
- **PRFAQ** = Press Release + FAQ (what customers would see and hear)

PRFAQ helps you stress-test your idea before committing to detailed PRD.

### The BMAD Flow

1. **Brief** (this episode) — Define your vision
2. **PRFAQ** (next episode) — Stress-test the vision
3. **PRD** (next episode) — Detail the requirements
4. **Architecture** — Design the technical solution
5. **Epics & Stories** — Break into implementable work
6. **Execution** — Build it

Each step validates and refines the previous step.

---

## 💬 Key Concepts

- **Product Brief** = Short document capturing project vision, audience, problem, solution
- **BMAD Planning** = Sequential process: Brief → PRFAQ → PRD → Architecture → Epics
- **Agent Chat** = VS Code interface where BMAD skills run (Ctrl+Shift+P)
- **Scope Boundaries** = Explicitly defining what's NOT included (prevents scope creep)
- **Success Criteria** = How you'll measure whether the project succeeded
- **Vision Statement** = One-sentence description of what you're building and why it matters



---

## ❓ FAQ

**Q: Do I need a Product Brief for my project?**  
A: Yes. Even small projects benefit from a clear 1-2 page brief. It prevents confusion and scope creep.

**Q: Can I skip this and go straight to PRD?**  
A: Technically yes, but BMAD is designed for this sequence. The brief informs PRFAQ, which informs PRD. Skipping wastes effort on wrong requirements.

**Q: What if my brief looks different from the example?**  
A: That's expected! Every project is different. The example shows the Python YouTube Series. Your brief should reflect YOUR project's unique characteristics.

**Q: Can I use this for real projects?**  
A: Absolutely! This brief template is production-ready. Many companies use similar formats for product planning.

**Q: What if I don't have all the answers yet?**  
A: That's fine. The brief captures what you know now. As you move through PRFAQ and PRD, you'll refine and add more detail. The brief is a living document.

**Q: How detailed should my brief be?**  
A: Keep it to 1-2 pages. If you're writing more, that's probably PRD detail (Story 1-5).

---

## 🔗 Quick Reference

### Opening BMAD Agent Chat
```
Ctrl+Shift+P  →  Search "BMAD: Launch Agent"  →  Pick any agent
```

### Running the Skill (in Agent Chat)
```
use the bmad-product-brief skill
```

### Viewing Your Generated Brief
```
VS Code → File Explorer → _bmad-output/ → planning-artifacts/ → product-brief/
```

### Accessing Templates & Examples
```
Episode Folder → code/
├── brief-template.md   (blank template)
└── brief-example.md    (completed example)
```

### ⚠️ Commands That DON'T Work
```bash
# These WILL FAIL - Don't use them
uv run bmad brief          # ❌ Program not found
uv run bmad plan           # ❌ Program not found
npm run brief              # ❌ Wrong approach
```

**For Product Brief:** Use VS Code Agent Chat instead (Ctrl+Shift+P)

---

## 🎬 Video Information

**YouTube Link:** [YouTube Link](https://www.youtube.com/watch?v=BQnwR-tBLfQ)
**Published:** 2026-08-03
**Status:** ✅ Published

### Timestamps
00:00 – Intro  
00:30 – What BMAD-help told us  
01:06 – Opening the BMAD Agent  
01:36 – Running the bmad-product-brief skill  
02:40 – Answering all 8 brief questions  
09:45 – Reviewing the generated brief  
11:00 – What comes next  
13:30 – Recap & next video

---

## 🚀 What's Next?

### Story 1-5: PRFAQ + PRD
In the next episode, you'll:
- Create a Press Release for your project
- Build a Frequently Asked Questions section
- Define detailed requirements (PRD)
- Learn how to stress-test your idea before building
- Connect the brief to implementation requirements

---

## ✅ Checklist for Viewers

- [ ] Watch the full video
- [ ] Read this README
- [ ] Download `code/brief-template.md`
- [ ] Review `code/brief-example.md`
- [ ] Open BMAD Agent Chat (Ctrl+Shift+P)
- [ ] Run `use the bmad-product-brief skill`
- [ ] Answer all 8 questions for your project
- [ ] Review your generated brief in `_bmad-output/`
- [ ] Compare your brief to the example
- [ ] Ready for Story 1-5 (PRFAQ + PRD)

---

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

**Ready to plan your project? Watch the video and run the skill!** 🎬

---

*Last Updated: 2026-08-03*  
*Status: ✅ Ready for Publishing*
