# YTlearning — AI-Driven Development on YouTube

Welcome to **YTlearning**, a comprehensive YouTube series teaching AI-assisted software development through real-world projects and proven frameworks.

## 📺 Series Overview

Currently, we're focusing on the **BMAD for Python series** — a foundational 11-episode course on the **BMAD** (AI-driven Agile Development) methodology.

### 🎬 Series 1: BMAD for Python (11 Episodes) ✅ Complete

Learn how to build software using AI agents and structured workflows.

| Episode | Title | Focus | Duration |
|---------|-------|-------|----------|
| 1-1 | What is BMAD | Methodology intro | 6-7 min. |
| 1-2 | BMAD Setup | Environment setup | 8-9 min. |
| 1-3 | BMAD Loop Setup | Configuration | 20-21 min. |
| 1-4 | Product Brief | Requirements gathering | 13-14 min. |
| 1-5 | PRFAQ & PRD | Planning documents | 15-16 min. |
| 1-6 | Architecture | System design | 27-28 min. |
| 1-7 | Epics & Stories | Work breakdown | 50-51 min. |
| 1-8 | Implementation Readiness | Quality gates | 8-9 min. |
| 1-9 | Sprint Planning | Roadmap planning | 33-34 min. |
| 1-10 | Execution Phase | Sprint workflow (Sprint 1) | 15-16 min. |
| 1-11 | Execution Phase - Final | Sprint workflow (Sprint 2) | 15-16 min. |

**▶️ Watch on YouTube:** [BMAD for Python Playlist](https://www.youtube.com/watch?v=2xA84EbaC3Y&list=PLR0W-0LC9wyE)

---

### 📂 Repository Structure

```
YTlearning/
├── 1-bmad-for-python/           ← 11 complete episodes (scripts, code, resources)
├── 2-real-projects/             ← Coming soon
├── 3-crypto/                    ← Coming soon
├── 4-tutorials/                 ← Coming soon
├── 5-shorts/                    ← Coming soon
├── _bmad/                        ← BMAD framework setup & configs
├── docs/                         ← Additional documentation
└── README.md                     ← This file
```

---

## 🚀 Getting Started

### Watch the Series
1. Start with **Episode 1-1: What is BMAD**
2. Follow the sequence through all 11 episodes
3. Each episode has code examples and detailed explanations

### Access Code & Resources
Each episode folder contains:
- **script/** — Full video transcript
- **code/** — Python code, templates, and examples
- **README.md** — Learning guide and next steps
- **assets/** — Images and supporting materials

### Example: Episode 1-1
```
1-bmad-for-python/1-1-what-is-bmad/
├── script/script.md          ← Full video transcript
├── code/main.py              ← Starter code
├── README.md                 ← Learning guide
└── assets/                   ← Images
```

**Access on GitHub:**
```
https://github.com/NexusBT2026/YTlearning/tree/main/1-bmad-for-python
```

---

## ⚡ Setup

Before diving into the episodes, set up your local environment:

### 1. Clone the Repository
```bash
git clone https://github.com/NexusBT2026/YTlearning.git
cd YTlearning
```

### 2. Configure VS Code Settings
Copy the example settings file to your `.vscode` folder and customize it:

**Windows (PowerShell):**
```powershell
Copy-Item setting.json.example -Destination .vscode/setting.json
```

**Linux / macOS:**
```bash
cp setting.json.example .vscode/setting.json
```

Then edit `.vscode/setting.json` and configure paths for your system (see "Optional: Auto-Activate Conda Environment" section below).

### 3. Install Dependencies

**Install Node.js packages:**
```bash
npm install
```

**Install Python packages:**
```bash
python -m pip install -r requirements.txt
```

### 4. BMAD Auto-Initialize
The BMAD framework in `_bmad/` will automatically initialize when you run any BMAD workflows. No additional setup required.

### 5. (Optional) Create `.env` for API Keys
If you plan to use external APIs in future episodes:
```bash
# Copy the example (no keys needed yet)
cp .env_example .env

# Add your API keys to .env when needed
# .env is gitignored and never shared
```

---

## ⚙️ Optional: Auto-Activate Conda Environment

If you're using VS Code and want to automatically activate the `bmad-python` environment every time you open a terminal, follow this optional setup:

### Why?
When you work with multiple conda environments, manually activating each time can be tedious. This setup ensures the correct environment is always active when you're in this project.

### How to Set Up

1. **Copy the example settings file:**
   ```bash
   cp .vscode/settings.json.example .vscode/settings.json
   ```

2. **Edit `.vscode/settings.json`** and replace `YOUR_USERNAME` with your actual Windows username:
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

   **Find your conda path:**
   ```bash
   conda info --envs
   ```
   Look for the `bmad-python` environment path and update the `defaultInterpreterPath`.

3. **Restart VS Code** — the terminal will now auto-activate `bmad-python` on each new terminal.

### Note
- `.vscode/settings.json` is **gitignored** (not shared) — only your local copy is used
- Each team member configures their own path based on their system
- This is completely optional — you can always manually activate the environment

---

## 📚 What is BMAD?

BMAD is an **AI-driven agile development methodology** that combines:

1. **Planning Phase** — Requirements, brief, architecture
2. **Design Phase** — UX/UI specifications, system design
3. **Development Phase** — Sprint execution with AI agents
4. **Review Phase** — Code review and quality checks
5. **Verification Phase** — Testing and deployment

This series teaches you the framework, philosophy, and practical tools to implement BMAD in your own projects.

---

## 💬 Community & Questions

Have questions about the series or code?

**GitHub Discussions:** [YTlearning Discussions](https://github.com/NexusBT2026/YTlearning/discussions)

We've set up categories for:
- 📢 **Announcements** — New episodes and updates
- 💬 **General** — Off-topic discussions
- 💡 **Ideas** — Suggest episode topics
- ❓ **Q&A** — Questions about concepts or code
- 🎉 **Show and Tell** — Share your projects

---

## 🌱 Future Series

This repository will grow as we release new series:

- **Series 2: Real Projects** — Building actual applications
- **Series 3: Crypto** — Blockchain and Web3 development
- **Series 4: Tutorials** — Deep dives into specific topics
- **Series 5: Shorts** — Quick tips and tricks

Each series will follow the same structure: episodes with scripts, code, and resources.

---

## 🤝 Contributing & Community

Want to help? We welcome:

- **Bug Reports** — Found an error? Open an [issue](https://github.com/NexusBT2026/YTlearning/issues)
- **Feature Requests** — Ideas for new series? Start a [discussion](https://github.com/NexusBT2026/YTlearning/discussions)
- **Questions** — Confused about something? Ask in [Discussions](https://github.com/NexusBT2026/YTlearning/discussions)
- **Show & Tell** — Built with BMAD? Share your project!

Read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) first.

---

## 📋 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) file for details.

In short: You're free to use, modify, and distribute this code as long as you include the license and copyright notice.

---

## 👤 About

Created for developers who want to master AI-driven development workflows.

**YouTube Channel:** [YTlearning](https://www.youtube.com/@kellyvanhole/playlists)

**GitHub:** [@NexusBT2026](https://github.com/NexusBT2026)

---

## 🎯 What's Next?

1. **Watch Episode 1-1** on YouTube
2. **Clone this repo** to access all code and resources
3. **Join Discussions** to ask questions and share projects
4. **Subscribe** for new series announcements

Happy learning! 🚀
