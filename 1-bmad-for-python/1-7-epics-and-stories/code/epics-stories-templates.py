#!/usr/bin/env python3
"""
Story 1-7: Epics & Stories Templates
Shows how to document epics and user stories for any project
"""

# ==============================================================================
# EPIC TEMPLATE
# ==============================================================================

epic_template = """
# Epic Name: [Epic title]

**Epic ID:** E-1  
**Status:** Planned / In Progress / Done  
**Owner:** [Your name]

## Overview

[Clear description of what this epic accomplishes]

## Goals

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## User Stories

This epic contains the following stories:

- Story 1-X: [Title]
- Story 1-Y: [Title]
- Story 1-Z: [Title]

## Success Criteria

- ✅ All stories completed
- ✅ All acceptance criteria met
- ✅ Integration tested
- ✅ Ready for production

## Duration Estimate

[Total hours/days for entire epic]

## Dependencies

- [Other epics or stories this depends on]

## Risks

- [Potential risks and mitigation plans]
"""

# ==============================================================================
# USER STORY TEMPLATE
# ==============================================================================

user_story_template = """
# User Story: [Title]

**Story ID:** 1-4  
**Status:** Backlog / Ready for Dev / In Progress / Review / Done  
**Points:** [5, 8, 13, etc.]

## User Story Statement

As a [user type], I want [feature] so that [benefit]

**Example:** As a Python beginner, I want to see working code examples, so that I can understand concepts practically

## Description

[Clear description of what this story accomplishes]

## Acceptance Criteria

- ✅ Criterion 1 (specific, measurable)
- ✅ Criterion 2 (specific, measurable)
- ✅ Criterion 3 (specific, measurable)

## Definition of Done

- [ ] Script is written
- [ ] Code examples are runnable
- [ ] README is complete
- [ ] Assets/checklist is created
- [ ] Video is recorded
- [ ] Captions are added
- [ ] YouTube link is live
- [ ] GitHub link is working
- [ ] Community questions answered

## Related Stories

- [Other stories this connects to]

## Notes

[Any additional context or considerations]
"""

# ==============================================================================
# ACCEPTANCE CRITERIA FOR VIDEO SERIES
# ==============================================================================

video_acceptance_criteria = """
For video series, every story must meet these acceptance criteria:

### Content Creation
✅ Video script written (teleprompter ready)
✅ Code examples are runnable (tested end-to-end)
✅ README created with learning objectives
✅ Production assets checklist completed

### Production & Recording
✅ Video recorded (correct duration, clear audio)
✅ Captions created and synced
✅ Thumbnail designed
✅ Graphics/animations added

### Publishing & Linking
✅ Video uploaded to YouTube
✅ Description includes: objectives, timestamps, related links
✅ Links to previous/next episodes in description
✅ Video added to correct playlist
✅ GitHub folder linked in description

### Community & Support
✅ YouTube comments monitored (48 hours)
✅ GitHub issues monitored
✅ Common questions answered
✅ Feedback recorded for next sprint
"""

if __name__ == "__main__":
    print("Epic Template:")
    print(epic_template)
    print("\n" + "="*80 + "\n")
    print("User Story Template:")
    print(user_story_template)
    print("\n" + "="*80 + "\n")
    print("Video Series Acceptance Criteria:")
    print(video_acceptance_criteria)
