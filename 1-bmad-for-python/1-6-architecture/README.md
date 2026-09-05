# Story 1-6: Architecture (BMAD Planning Phase Episode)

**Duration:** 27-28 minutes
**Difficulty:** Intermediate  
**Prerequisites:** Stories 1-1 through 1-5  
**Next Episode:** Story 1-7 (Epics & Stories)

---

## 📖 What You'll Learn

After completing this episode, you'll:

- ✅ Understand what an Architecture Spine is and why it matters
- ✅ Know the 8 key architecture decisions for the Python YouTube series
- ✅ Understand how architecture prevents inconsistencies
- ✅ See the complete repository structure for all 27 stories
- ✅ Know how architecture informs epics and stories breakdown
- ✅ Be ready to create epics and stories from the architecture

---

## 📂 Folder Contents

**script/** — Full video script  
- `script.md` — Complete 27-28 minute video script with all sections and timestamps

**code/** — Architecture templates and example  
- `architecture-template.md` — Blank template for documenting architecture
- `architecture-example.md` — Complete Architecture Spine for Python Series (8 decisions)

**assets/** — Production requirements  
- `ASSETS.md` — Production checklist

---

## 🎯 Key Concepts

### What is an Architecture Spine?

An Architecture Spine is a concise document that captures key decisions:

- **What it is:** Core rules that guide all future development
- **Why it matters:** Prevents inconsistencies across 27 stories
- **How it works:** Each decision specifies what's required and why
- **Where it lives:** GitHub as architectural reference

### The 8 Architecture Decisions

| Decision | What It Binds | Why It Matters |
|----------|---------------|---|
| **AD1** | Folder structure pattern | Consistency across all episodes |
| **AD2** | Naming conventions | Predictable file locations |
| **AD3** | Repository organization | Clear content vs infrastructure |
| **AD4** | Code quality standards | Viewers can run all examples |
| **AD5** | Documentation requirements | Complete learning experience |
| **AD6** | Video delivery model | Clear progression for viewers |
| **AD7** | Community engagement | Support is organized and timely |
| **AD8** | Quality gates | Every episode meets standards |

### Why Architecture Before Epics?

If you go straight from PRD to Epics without Architecture:
- ❌ Epics might have inconsistent structure
- ❌ Code organization might be random
- ❌ Documentation might be incomplete
- ❌ Production process might vary by episode
- ❌ Quality might be inconsistent

**With Architecture first:**
- ✅ All 27 stories follow same pattern
- ✅ Automation becomes possible
- ✅ Quality is consistent
- ✅ Viewers have predictable experience
- ✅ Production workflow is reliable

---

## 🔗 Quick Reference

### Opening BMAD Agent Chat
```
Ctrl+Shift+P  →  Search "BMAD: Launch Agent"  →  Pick any agent
```

### Running the Skill (in Agent Chat)
```
use the bmad-architecture skill
```

### Viewing Your Generated Architecture
```
VS Code → File Explorer → _bmad-output/ → planning-artifacts/ → architecture/
```

### Accessing Templates & Examples
```
Episode Folder → code/
├── architecture-template.md   (blank template)
└── architecture-example.md    (completed example)
```

---

## 🎬 Video Information

**YouTube Link:** [YouTube Link](https://www.youtube.com/watch?v=wVtGtAaEDwo)  
**Published:** 2026-08-05
**Status:** ✅ Published

### Timestamps:
- 00:00 – Intro
- 00:30 – What BMAD-help told us
- 01:30 — Opening the BMAD Agent
- 01:50 – Running Architecture
- 17:50 – Architecture breakdown
- 23:40 – Reviewing the architecture
- 25:15 – What comes next
- 27:10 – Recap & next video

---

## 🚀 What's Next?

### Story 1-7: Epics & Stories
In the next episode, you'll:
- Break down architecture into epics
- Create user stories from epics
- Write acceptance criteria
- Understand the complete 27-story breakdown
- Be ready for the Design Phase

---

## ✅ Checklist for Viewers

- [ ] Watch the full video
- [ ] Read this README
- [ ] Download `code/architecture-template.md`
- [ ] Review `code/architecture-example.md`
- [ ] Open BMAD Agent Chat (Ctrl+Shift+P)
- [ ] Run `use the bmad-architecture skill`
- [ ] Answer the 8 architecture decision questions
- [ ] Review your generated architecture in `_bmad-output/`
- [ ] Compare your architecture to the example
- [ ] Ready for Story 1-7 (Epics & Stories)

---

**Ready to design your system backbone? Watch the video and run the skill!** 🎬

---

*Last Updated: 2026-08-05*
*Status: ✅ Ready for Publishing*
