# Architecture Spine Template
# Define the consistent rules and decisions that guide all implementation

---

## ARCHITECTURE OVERVIEW

**Project:** [Your Project Name]

**Purpose of this Architecture Spine:**
- Define consistent rules that all future work must follow
- Prevent costly inconsistencies across the codebase
- Enable scaling and team collaboration
- Serve as reference for decision-making

---

## ARCHITECTURAL DECISIONS (ADs)

### AD1: Project Organization Structure

**Binds:**
- All episodes/modules must follow the folder pattern: `{epic}-{episode}-{description}/`
- Inside each folder: `script/`, `code/`, `assets/`, `README.md`

**Prevents:**
- Inconsistent folder naming
- Mixed organizational patterns
- Hard-to-navigate codebases

**Rule:**
Every new episode/story automatically gets this folder structure. No exceptions.

---

### AD2: Naming Conventions

**Binds:**
- Episodes: `1-1`, `1-2`, `2-3` (epic-episode format)
- Story files: `1-1-what-is-bmad` (epic-episode-slug format)
- Folders: Lowercase with hyphens, descriptive names
- Variables/functions: [Your language convention]

**Prevents:**
- Ambiguous or unclear naming
- Hard-to-discover content
- Inconsistent capitalization/formatting

**Rule:**
New episodes must follow naming convention before being created.

---

### AD3: Repository Organization

**Binds:**
- Content: `/episodes/` or `/1-bmad-for-python/`
- Planning: `/_bmad-output/`
- Infrastructure: `/_bmad/`
- Shared: `README.md`, `LICENSE`, `.gitignore` at root

**Prevents:**
- Mixed content and configuration
- Unclear ownership of files
- Difficult backups and organization

**Rule:**
Files go to designated folders based on their category. No spillover.

---

### AD4: Code Quality Standards

**Binds:**
- All code in `/code/` folder must be runnable
- No pseudo-code or incomplete examples
- Include comments explaining concepts
- Follow [Your Language Style Guide]

**Prevents:**
- Broken code that viewers can't run
- Inconsistent code quality
- Hard-to-understand examples

**Rule:**
Every code file must pass: "Can a beginner run this and get the expected output?"

---

### AD5: Documentation Requirements

**Binds:**
- Every episode has `/script/script.md` (full video text)
- Every episode has `/README.md` (learning guide)
- Every episode has `/assets/ASSETS.md` (production checklist)
- Every episode has README with learning objectives and FAQ

**Prevents:**
- Missing or incomplete documentation
- Viewers unsure how to follow along
- Inconsistent learning experience

**Rule:**
Episodes without complete documentation are not approved for production.

---

### AD6: Video Delivery Model

**Binds:**
- All videos published to YouTube (primary distribution)
- Organized into playlists by series/epic
- Episodes released in numerical order
- Each video links to previous/next episodes
- GitHub folder linked in description

**Prevents:**
- Viewers missing earlier context
- Orphaned or hard-to-find videos
- Broken narrative progression

**Rule:**
Videos must link to previous/next and include GitHub references.

---

### AD7: Community Engagement Pattern

**Binds:**
- Questions answered via GitHub Issues first
- YouTube comments enabled and monitored
- Responses within X hours (define your SLA)
- Links provided between code and video

**Prevents:**
- Duplicate support conversations
- Missed questions
- Poor user experience

**Rule:**
Active management of both GitHub Issues and YouTube comments.

---

### AD8: Quality Gates

**Binds:**
- Before recording: script ✓, code ✓, assets ✓, README ✓
- Before publishing: captions ✓, description ✓, links ✓
- Before marking done: All acceptance criteria met

**Prevents:**
- Low-quality releases
- Incomplete episodes
- Inconsistent quality across series

**Rule:**
Quality gates are mandatory. No exceptions.

---

## INVARIANTS (Things That Must Always Be True)

1. **Consistency**: All episodes follow the same folder structure and naming
2. **Quality**: Every episode passes all quality gates
3. **Documentation**: Every episode has complete documentation
4. **Linkage**: All videos link to previous/next episodes
5. **Accessibility**: All content has captions and transcripts
6. **Runability**: All code examples work and are runnable

---

## PATTERNS TO REPEAT

**Episode Production Pattern:**
1. Create story file in `stories/` folder
2. Create episode folder with script/code/assets/README
3. Record video using script as teleprompter
4. Add captions and description
5. Publish to YouTube
6. Link to previous/next episodes
7. Mark story as "done" in sprint-status.yaml

**This pattern repeats for all 27 stories across 8 sprints.**

---

## ARCHITECTURE DIAGRAM

```
Series Repository Structure

1-bmad-for-python/          (All episodes for this epic)
├── 1-1-what-is-bmad/
│   ├── script/script.md
│   ├── code/main.py
│   ├── assets/ASSETS.md
│   └── README.md
├── 1-2-bmad-setup/
│   ├── script/script.md
│   ├── code/verify_setup.py
│   ├── assets/ASSETS.md
│   └── README.md
└── 1-3-bmad-loop-setup/
    ├── script/script.md
    ├── code/explore_loop.py
    ├── assets/ASSETS.md
    └── README.md

_bmad-output/              (Planning artifacts)
├── implementation-artifacts/stories/
│   ├── 1-1-what-is-bmad.md
│   ├── 1-2-bmad-setup.md
│   └── ...
└── execution-artifacts/
    ├── sprint-1-execution-report.yaml
    └── sprint-1-production-checklist.md

_bmad/                     (Infrastructure)
├── scripts/
├── config.yaml
└── modules/
```

---

## HOW TO USE THIS ARCHITECTURE SPINE

**When Creating New Episodes:**
- Reference AD1-8 to ensure consistency
- Use folder structure pattern (AD1)
- Follow naming convention (AD2)
- Organize files per AD3

**When Building Code:**
- Follow quality standards (AD4)
- Ensure code is runnable
- Add helpful comments

**When Documenting:**
- Follow documentation requirements (AD5)
- Include script, README, assets checklist

**When Publishing:**
- Follow video delivery model (AD6)
- Link to previous/next episodes
- Include GitHub references

**When Supporting Community:**
- Follow engagement pattern (AD7)
- Monitor GitHub Issues and YouTube comments

**When Quality-Checking:**
- Verify all quality gates (AD8)
- No exceptions

---

**Architecture Version:** 1.0  
**Created:** [Date]  
**Last Updated:** [Date]  
**Owner:** [Your name/organization]  
**Status:** Approved
