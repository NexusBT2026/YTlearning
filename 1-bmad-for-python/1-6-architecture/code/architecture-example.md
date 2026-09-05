# Architecture Spine — Python YouTube Series
# Complete example showing all decisions for the BMAD series

---

## PROJECT OVERVIEW

**Project Name:** Python YouTube Series: Real Projects for Beginners  
**Epics:** 5 (BMAD Foundation, Real Projects, Crypto, Tutorials, Shorts)  
**Total Stories:** 27 across 8 sprints  
**Architecture Version:** 1.0  
**Status:** Approved and Active

---

## ARCHITECTURAL DECISIONS

### AD1: Episode Folder Structure

**Binds:**
- All episodes under `/1-bmad-for-python/` for Epic 1
- Folder naming: `{epic}-{episode}-{slug}`
- Example: `1-4-product-brief`, `2-1-rest-api-client`
- Inside each: `script/`, `code/`, `assets/`, `README.md`

**Prevents:**
- Inconsistent folder layout across 27 stories
- Hard-to-navigate repository
- Missing required files

**Rule:**
Before creating Story 2-3, folder must exist with all subdirectories.

**Why This Decision:**
- Automation can predictably find script, code, and assets
- Viewers can reliably find code examples
- Production workflow is consistent across all episodes

---

### AD2: Naming Convention

**Binds:**
- **Stories:** `{epic}-{episode}-{slug}`
  - `1-1-what-is-bmad` (Epic 1, Episode 1)
  - `2-3-websocket-client` (Epic 2, Episode 3)
  - `3-2-smart-contracts` (Epic 3, Episode 2)
  
- **Folders:** Same as story name with lowercase hyphens
  - `1-bmad-for-python/1-1-what-is-bmad/`
  - `2-real-projects/2-1-rest-api-client/`
  
- **Story Files:** `{story-id}.md`
  - `1-1-what-is-bmad.md` (in `_bmad-output/implementation-artifacts/stories/`)
  
- **Code Files:** Descriptive, lowercase
  - `main.py`, `verify_setup.py`, `explore_loop.py`

**Prevents:**
- Ambiguous naming
- Hard to find episodes
- Unpredictable file locations

**Rule:**
New stories automatically get this naming. No variations.

**Why This Decision:**
- Naming encodes episode information
- Predictable paths enable scripting
- YouTube URL structure can match folder names

---

### AD3: Repository Root Organization

**Binds:**
- `/1-bmad-for-python/` — All Epic 1 episode folders
- `/2-real-projects/` — All Epic 2 episode folders (future)
- `/_bmad-output/` — All planning and execution artifacts
  - `/implementation-artifacts/stories/` — Story markdown files
  - `/execution-artifacts/` — Sprint reports and checklists
- `/_bmad/` — Infrastructure and scripts
  - `/scripts/` — Automation (execute_sprint.py, etc.)
  - `/custom/` — User customizations
- Root level: `README.md`, `LICENSE`, `sprint-status.yaml`

**Prevents:**
- Mixed content and configuration
- Unclear which files are production vs planning
- Difficult to back up or reorganize

**Rule:**
Files go to designated folders. If unsure, check this architecture.

**Why This Decision:**
- Clear separation: content, planning, infrastructure
- Easy to backup (e.g., just backup `/1-bmad-for-python/` for release)
- Viewers see working code, not build artifacts

---

### AD4: Code Quality Standards

**Binds:**
- All code in `/code/` must be runnable (no pseudo-code)
- Code must work with Python 3.10+ (no external GPUs)
- Include docstrings explaining what code does
- Follow PEP 8 style guide (with linter)
- Error handling required (try/except for expected errors)
- Comments for non-obvious concepts

**Prevents:**
- Broken code that frustrates viewers
- Viewers stuck on environment issues
- Inconsistent code quality across episodes

**Rule:**
Every code file must pass: "Can a beginner with Python 3.10 run this and get output?"

**Example:**
```python
#!/usr/bin/env python3
"""
Story 1-4: Exploring the BMAD Loop
Shows how to use the bmad-execute-sprint skill
"""

import subprocess
import json

def main():
    """Main entry point for the BMAD Loop explorer."""
    print("🤖 BMAD Loop Explorer\n")
    # ... rest of code with error handling
```

**Why This Decision:**
- Viewers follow along and succeed
- Confidence building is critical for beginners
- Sets expectation for professional code standards

---

### AD5: Documentation Requirements

**Binds:**
- Every episode MUST have:
  1. `/script/script.md` — Full video transcript (5-50 minutes)
  2. `/README.md` — Learning guide with objectives, FAQ, checklist
  3. `/assets/ASSETS.md` — Production checklist (thumbnails, captions, etc.)
  4. `/code/` directory with working examples
  
- Documentation must include:
  - Learning objectives (what viewers will learn)
  - Key concepts explained
  - Timestamps for key sections
  - FAQ with common questions
  - Production checklist for recording

**Prevents:**
- Viewers unsure how to follow along
- Inconsistent video quality
- Missing production assets

**Rule:**
Episodes without all four documentation pieces are not approved for production.

**Why This Decision:**
- Viewers know what they'll learn
- Hosts have clear content roadmap
- Checklists prevent missing steps

---

### AD6: Video Delivery Model

**Binds:**
- All videos published on YouTube (primary channel)
- Organized into playlists:
  - "BMAD Series" — Stories 1-1 through 1-10
  - "Real Projects" — Stories 2-1 through 2-9 (future)
  - "Crypto Series" — Stories 3-1 through 3-5 (future)
  
- Episodes released in order (1-1, 1-2, 1-3, etc.)
- No skipping ahead (viewers need context)
- Each video description includes:
  - Link to GitHub folder
  - Link to previous episode (if not first)
  - Link to next episode (if known)
  - Timestamps for sections
  - Required resources

**Prevents:**
- Viewers watching episodes out of order
- Orphaned or hard-to-find videos
- Broken narrative progression

**Rule:**
Videos must be published in order. Descriptions must include GitHub links.

**Why This Decision:**
- Clear progression helps beginners
- GitHub links drive code adoption
- Viewers don't skip prerequisites

---

### AD7: Community Engagement Pattern

**Binds:**
- Primary support channel: GitHub Issues (organized by episode)
- Secondary: YouTube comments (monitored)
- Response SLA: Within 48 hours for substantive questions
- All code questions point to GitHub Issues
- YouTube comments used for "soft" feedback (suggestions, appreciation)

**Prevents:**
- Duplicate conversations across platforms
- Missed questions
- Viewer frustration

**Rule:**
Active management of both channels, with GitHub as primary.

**Why This Decision:**
- GitHub Issues create searchable archive
- Code examples stay in GitHub (not comments)
- Viewers learn to use GitHub for real projects

---

### AD8: Quality Gates (Mandatory)

**Binds:**
- **Before Recording:**
  - ✅ Script written and reviewed
  - ✅ Code tested and runnable
  - ✅ Assets checklist created
  - ✅ README complete
  
- **Before Publishing:**
  - ✅ Video recorded and edited
  - ✅ Captions added and synced
  - ✅ Description written with links
  - ✅ Thumbnail created
  - ✅ Playlist assigned
  
- **Before Marking "Done":**
  - ✅ All acceptance criteria met
  - ✅ YouTube link working
  - ✅ GitHub link accessible
  - ✅ Comments monitored for first 48 hours

**Prevents:**
- Low-quality videos
- Incomplete episodes
- Inconsistent viewer experience
- Broken links and access issues

**Rule:**
No exceptions. Every episode passes all gates or doesn't go live.

**Why This Decision:**
- Quality builds audience trust
- Consistency across 27 stories is critical
- Professional standards attract serious learners

---

## INVARIANTS (Things That Must Always Be True)

1. **Consistency**: Every episode follows same folder/naming pattern
2. **Quality**: Every episode passes quality gates
3. **Documentation**: Every episode has script, code, README, assets
4. **Linkage**: Every video links to previous/next episodes
5. **Accessibility**: Every episode has captions and transcript
6. **Runability**: Every code example works end-to-end
7. **Progression**: Episodes released in order, no skipping
8. **Support**: Questions answered via GitHub Issues (primary)

---

## ARCHITECTURE IN ACTION: Sprint 1 Example

**Sprint 1:** BMAD Foundation (Stories 1-1 through 1-3)

```
GitHub Structure:
1-bmad-for-python/
├── 1-1-what-is-bmad/
│   ├── script/script.md         (⬅ Teleprompter for video)
│   ├── code/main.py             (⬅ Demo: python main.py)
│   ├── assets/ASSETS.md         (⬅ Production checklist)
│   └── README.md                (⬅ Learning guide)
├── 1-2-bmad-setup/
│   ├── script/script.md         (⬅ Teleprompter)
│   ├── code/verify_setup.py     (⬅ Setup verification)
│   ├── code/setup.sh            (⬅ Install script)
│   ├── assets/ASSETS.md         (⬅ Production checklist)
│   └── README.md                (⬅ Learning guide)
└── 1-3-bmad-loop-setup/
    ├── script/script.md         (⬅ Teleprompter)
    ├── code/explore_loop.py     (⬅ Interactive tool)
    ├── assets/ASSETS.md         (⬅ Production checklist)
    └── README.md                (⬅ Learning guide)

YouTube Playlist: "BMAD Series"
├── Story 1-1: What is BMAD?
│   └── Description includes: GitHub link, previous (none), next (1-2)
├── Story 1-2: BMAD Setup
│   └── Description includes: GitHub link, previous (1-1), next (1-3)
└── Story 1-3: BMAD Loop Setup
    └── Description includes: GitHub link, previous (1-2), next (1-4)

Production Workflow:
1. Read script/script.md as teleprompter
2. Record demo from code/ folder
3. Use assets/ASSETS.md production checklist
4. Add captions and description with links
5. Publish with previous/next links
6. Monitor GitHub Issues for questions
```

---

## SCALING TO 27 STORIES

This architecture repeats identically for:
- Sprint 2 (Stories 1-4 through 1-6)
- Sprint 3 (Stories 1-7 through 1-11)
- Epic 2: Real Projects (Stories 2-1 through 2-9)
- Epic 3: Crypto (Stories 3-1 through 3-5)
- And so on...

Same pattern, different content.

---

## DECISIONS THAT ENABLE AUTOMATION

Because of these architecture decisions:
- **Sprint Execution** can automatically find and validate stories
- **Code Quality** checks can run against `/code/` folders
- **Production Checklists** can be auto-generated from `/assets/ASSETS.md`
- **Linking** can be scripted (previous/next episodes)
- **Release** can be batched (all approved stories publish together)

---

**Architecture Version:** 1.0  
**Created:** 2026-08-08  
**Last Updated:** 2026-08-08  
**Owner:** [Your name]  
**Status:** Active and Approved for All 27 Stories  
**Next Review:** After Sprint 1 completion
