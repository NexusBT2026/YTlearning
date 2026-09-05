# Story 5-1: VS Code Hack — Auto-Activate Your Conda Environment

## Overview

A quick YouTube Short teaching Python developers how to auto-activate their Conda environment in VS Code with a simple `.vscode/settings.json` configuration.

**Duration**: ~50 seconds  
**Platform**: YouTube Shorts  
**Target Audience**: Python developers, VS Code users  

---

## 🎬 What You'll Learn

- How VS Code settings can automate Conda environment activation
- One-time setup that saves time daily
- Copy-paste ready configuration
- Where to find the example in the main repository

---

## 📝 Script

See `script/script.md` for the full 50-second voiceover script.

**Key Points**:
- Hook: "Quick VS Code hack for Python developers"
- Problem: Manual `conda activate` every time
- Solution: `settings.json` with terminal profile configuration
- Benefit: Automatic activation on every new terminal
- CTA: Copy `settings.json.example` from repo

---

## 💻 Code & Configuration

**File**: `code/settings.json.example`

This is a template `.vscode/settings.json` that users can copy and customize:

```json
{
  "python.defaultInterpreterPath": "C:\\Users\\YOUR_USERNAME\\anaconda3\\envs\\bmad-python\\python.exe",
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "args": ["-NoExit", "-Command", "conda activate bmad-python"]
    }
  }
}
```

**Setup Instructions**:
1. Copy this file to `.vscode/settings.json` in your project
2. Replace `YOUR_USERNAME` with your actual Windows username
3. Replace `bmad-python` with your conda environment name (if different)
4. Restart VS Code
5. All new terminals will auto-activate the environment

---

## 🎨 Assets

See `assets/ASSETS.md` for complete production checklist:
- ✅ Thumbnail (vertical 1080×1920 format)
- ✅ Script (50 seconds)
- ✅ Code example (settings.json)
- ✅ Video file (MP4, final edit)
- ✅ YouTube metadata (title, description, tags)

---

## 📊 Production Status

| Item | Status | Notes |
|------|--------|-------|
| Script | ✅ Complete | 50-second voiceover ready |
| Code | ✅ Complete | settings.json.example finalized |
| Thumbnail | ✅ Ready | Vertical format (1080×1920) |
| Video Recording | ✅ Complete | Recorded with demos |
| Video Edit | ✅ Complete | Final render ready |
| Captions | ✅ Complete | YouTube auto-generated |
| Metadata | ✅ Complete | Title, description, tags configured |
| Upload | ✅ PUBLISHED | Live on YouTube Shorts |

---

## 🎯 YouTube Metadata

**Title** (< 50 chars):  
`VS Code Hack — Auto-Activate Your Conda Environment`

**Description**:  
```
Auto‑activate your Conda environment in VS Code with one simple settings.json file.

This trick saves beginners time and keeps your Python workflow clean.

👇 Copy the example file from the repo
https://github.com/NexusBT2026/YTlearning/blob/main/.vscode/settings.json.example

👇 README section
"Optional: Auto‑Activate Conda Environment" in the main README

👇 Full repo
https://github.com/NexusBT2026/YTlearning

#Python #VSCode #Conda #DeveloperTools #CodingTips #Shorts
```

**Tags**:  
`#Python` `#VSCode` `#Conda` `#DeveloperTools` `#CodingTips` `#Shorts` `#PythonDeveloper` `#TerminalHack` `#ProductivityTip`

---

## ✅ Quality Checklist (Before Upload)

- [x] Video duration: 45-59 seconds ✓
- [x] Vertical format: 1080×1920 ✓
- [x] Audio: Clear, no background noise ✓
- [x] Hook in first 2 seconds ✓
- [x] Text/code readable on phone screen ✓
- [x] Thumbnail: High contrast, eye-catching ✓
- [x] Title: Clear and SEO-friendly ✓
- [x] Description: Includes all links and hashtags ✓
- [x] Captions: Enabled and accurate ✓
- [x] Category: Education ✓
- [x] Playlist: "SHORTS" assigned ✓
- [x] Visibility: Public ✓

---

## 🎉 Status: PUBLISHED

✅ **Video is now live on YouTube Shorts**

All production phases complete:
- ✅ Pre-production: Script, code, assets prepared
- ✅ Recording: Recorded with VS Code terminal demo
- ✅ Post-production: Edited, captioned, rendered
- ✅ Publishing: Live on YouTube Shorts channel
- ✅ Monitoring: Tracking engagement and feedback

---

## 📚 Next Steps

1. **Monitor Engagement** — Track views, likes, comments
2. **Respond to Comments** — Answer viewer questions
3. **Gather Feedback** — Note topics for future shorts
4. **Analyze Metrics** — Review retention and CTR after 1 week

---

## 🔗 Related Resources

- **Main Repo**: [YTlearning](https://github.com/NexusBT2026/YTlearning)
- **Settings Template**: [`5-shorts/5-1-vs-code-hack-auto-activate/code/settings.json`](https://github.com/NexusBT2026/YTlearning/blob/main/5-shorts/5-1-vs-code-hack-auto-activate/code/settings.json)
- **README Section**: [Optional: Auto-Activate Conda Environment](https://github.com/NexusBT2026/YTlearning#-optional-auto-activate-conda-environment)
- **YouTube Shorts Playlist**: [SHORTS](https://www.youtube.com/watch?v=yg_PvGrODEM&list=PLCB19e4KkvY0)

---

## 📝 Notes

- **Shorts Algorithm**: Optimal for 30-45 seconds; keep under 60 seconds for best reach
- **Mobile-First**: All graphics/text must be readable on small phone screens
- **Hook Critical**: First 2 seconds determine if viewers watch or skip
- **Captions Essential**: Most Shorts viewed on mute; ensure captions are accurate
- **Consistency**: Use similar visual style to maintain channel recognition

