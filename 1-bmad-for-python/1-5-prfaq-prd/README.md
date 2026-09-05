# Story 1-5: PRFAQ + PRD (Combined Planning Phase Episode)

## 📺 Episode Overview

**Title:** BMAD Planning Phase — Creating the PRFAQ + PRD (Combined Planning Phase Episode)

**Duration:** 15-16 minutes
**Difficulty:** Intermediate  
**Prerequisites:** Stories 1-1 through 1-4  
**Next Episode:** Story 1-6 (Architecture)

---

## 📖 What You'll Learn

After completing this episode, you'll:

- ✅ Understand PRFAQ (Press Release + FAQ) methodology and why it's important
- ✅ Know how to stress-test your project idea using customer questions
- ✅ Understand PRD (Product Requirements Document) structure and content
- ✅ Be able to write Functional Requirements (FRs) and Non-Functional Requirements (NFRs)
- ✅ Know how to define success criteria and constraints
- ✅ Understand how PRFAQ+PRD feeds into Architecture
- ✅ Be ready to design your system architecture

---

## 📂 Folder Contents

**script/** — Full video script  
- `script.md` — Complete 15-16 minute video script with all sections and timestamps

**code/** — PRFAQ + PRD templates and examples  
- `prfaq-template.md` — Blank Press Release + FAQ template
- `prd-template.md` — Blank PRD template

**assets/** — Production requirements  
- `ASSETS.md` — Production checklist (thumbnails, graphics, screenshots)

---

## 🔧 How to Use This Episode

1. **Watch the full video**
   - Follow along as we create PRFAQ and PRD for the Python YouTube Series

2. **Download the templates**
   - Get `code/prfaq-template.md` and `code/prd-template.md` from this episode folder
   - These are blank templates you can adapt for your own project

3. **Run the skills yourself**
   - Open VS Code Agent Chat (Ctrl+Shift+P)
   - Run `use the bmad-prfaq skill`
   - Answer the customer questions
   - Then run `use the bmad-prd skill`
   - Answer the detailed requirements questions

4. **Compare to the examples**
   - Look at the Python Series PRFAQ and PRD examples
   - See how completed documents look
   - Use them as inspiration for your own answers

5. **Review your generated documents**
   - BMAD creates both in `_bmad-output/planning-artifacts/`
   - These become the foundation for your architecture (Story 1-6)

6. **Move to Story 1-6**
   - With your PRFAQ and PRD complete, you're ready for Architecture design

---

## 🎯 Key Concepts

### What is PRFAQ?

PRFAQ (Press Release + FAQ) is Amazon's "Working Backwards" technique:

1. **Press Release** — Imagine your product is complete. Write a press release announcing it.
2. **FAQ** — Anticipate customer questions and answer them
3. **Red Flags** — Look for gaps, concerns, or doubts revealed in the FAQ
4. **Pivot or Proceed** — Either fix the concept or move forward with confidence

**Why It Matters:**
- Pressure-tests your idea before investing in development
- Surfaces hidden assumptions
- Validates concept from customer perspective
- Often reveals missing features or fatal flaws

### What is a PRD?

PRD (Product Requirements Document) is the detailed specification:

1. **Purpose & Vision** — Why does this project exist?
2. **Audience** — Who is this for?
3. **Features** — What does it do? (Functional Requirements)
4. **Quality Standards** — How well does it do it? (Non-Functional Requirements)
5. **Success Criteria** — How will you know it worked?
6. **Constraints & Risks** — What are the limitations and dangers?

**Why It Matters:**
- Provides single source of truth for what's being built
- Prevents scope creep (define out-of-scope items)
- Guides architecture and development teams
- Creates acceptance criteria for completion

### PRFAQ vs PRD

| Aspect | PRFAQ | PRD |
|--------|-------|-----|
| **Purpose** | Stress-test idea | Specify detailed requirements |
| **Audience** | Customer perspective | Team/stakeholder perspective |
| **Focus** | Value proposition | Technical specifications |
| **Length** | 2-5 pages | 5-15 pages |
| **When** | Before PRD | After PRFAQ |
| **Use** | Validation | Development planning |

### The BMAD Progression

```
Product Brief (Story 1-4)
    ↓
PRFAQ + PRD (Story 1-5) ← You Are Here
    ↓
Architecture (Story 1-6)
    ↓
Epics & Stories (Story 1-7)
    ↓
Implementation Readiness (Story 1-8)
    ↓
Sprint Planning (Story 1-9)
```

---

## ❓ FAQ

**Q: Why do we need both PRFAQ and PRD?**  
A: PRFAQ validates the idea from a customer perspective. PRD specifies exactly what to build. Both are needed for different reasons.

**Q: Can we skip PRFAQ and just do PRD?**  
A: Technically yes, but PRFAQ often reveals hidden issues. Many teams regret skipping it.

**Q: How long does it take to do PRFAQ + PRD?**  
A: Typically 2-4 hours total. This episode shows it taking 15-16 minutes because we're using BMAD automation.

**Q: What if the PRFAQ reveals problems with my idea?**  
A: That's the point! It's better to discover problems now than after you've spent weeks building. Go back to the Product Brief and revise.

**Q: What's the difference between Functional and Non-Functional Requirements?**  
A: **Functional (FR):** What does it DO? (Features, capabilities)  
**Non-Functional (NFR):** How WELL does it do it? (Performance, reliability, usability)

**Q: Can I share my PRFAQ/PRD publicly?**  
A: Yes, many teams do. It shows transparency and gathers feedback. (This Python Series PRD is fully public.)

**Q: How often should we update the PRD?**  
A: PRD is a living document. Update it as you learn and priorities change, but major changes should go through review cycle.

---

## 🔗 Quick Reference

### Opening BMAD Agent Chat
```
Ctrl+Shift+P  →  Search "BMAD: Launch Agent"  →  Pick any agent
```

### Running the Skills (in Agent Chat)
```
use the bmad-prfaq skill
use the bmad-prd skill
```

### Viewing Your Generated Documents
```
VS Code → File Explorer → _bmad-output/ → planning-artifacts/
```

---

## 🎬 Video Information

**YouTube Link:** [YouTube Link](https://www.youtube.com/watch?v=BZPjtGD21QM)  
**Published:** 2026-08-04
**Status:** ✅ Published

### Timestamps
00:00 – Intro
00:45 – What BMAD-help told us
01:48 – Opening the BMAD Agent
02:33 – Running PRFAQ
07:05 – Answering PRFAQ questions
09:20 – Running PRD
10:10 – PRD requirements
14:45 – What comes next
15:17 – Recap & next video

---

## 🚀 What's Next?

### Story 1-6: Architecture
In the next episode, you'll:
- Design the technical backbone
- Make 8 key architecture decisions
- Create an Architecture Spine
- Understand how architecture informs epics
- Be ready to break down 27 stories

---

## ✅ Checklist for Viewers

- [ ] Watch the full video
- [ ] Read this README
- [ ] Download `code/prfaq-template.md` and `code/prd-template.md`
- [ ] Open BMAD Agent Chat (Ctrl+Shift+P)
- [ ] Run `use the bmad-prfaq skill`
- [ ] Answer all customer FAQ questions
- [ ] Run `use the bmad-prd skill`
- [ ] Answer all detailed requirements questions
- [ ] Review your generated PRFAQ and PRD
- [ ] Compare your documents to the examples
- [ ] Ready for Story 1-6 (Architecture)

---

## 💬 Key Concepts

- **BMAD Loop** = Automation orchestrator that runs in VS Code Agent Chat
- **BMAD Skills** = Workflows you run by typing commands in Agent Chat
- **Agent Chat** = VS Code Copilot Chat where BMAD runs (Ctrl+Shift+P)
- **Product Requirements Document** = Your project's detailed requirements document (`_bmad-output/planning-artifacts/prd/prd.md`)
- **PRFAQ Challenge** = Your project's Press Release + FAQ document (`_bmad-output/planning-artifacts/prfaq/prfaq.md`)

### Important
- ❌ BMAD skills do NOT work in terminal
- ✅ BMAD skills run in VS Code Agent Chat
- ✅ Commands like `uv run bmad plan` will fail with "program not found"
- ✅ Use `Ctrl+Shift+P` to open Agent Chat and run skills

**Ready to stress-test your idea? Watch the video and run the skills!** 🎬

---

*Last Updated: 2026-08-04*
*Status: ✅ Ready for Publishing*
