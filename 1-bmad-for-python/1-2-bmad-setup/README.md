# Story 1-2: BMAD Setup

## 📺 Episode Overview

**Title:** Installing the BMAD Method with Python

**Duration:** ~8-9 minutes  
**Difficulty:** Beginner → Intermediate

This episode walks you through installing BMAD on your machine, creating a clean Python environment, and verifying that everything is ready for development.

---

## 🎯 Learning Objectives

After watching this episode, you'll be able to:

- ✅ Create a isolated Conda environment for BMAD projects
- ✅ Check all BMAD prerequisites (Node.js, Python, uv)
- ✅ Install the BMAD Method into a new project folder
- ✅ Verify the installation by running a Python script
- ✅ Understand why we use Conda for environment isolation
- ✅ Know where to install BMAD and why the folder structure matters

---

## 📂 Folder Structure

```
1-2-bmad-setup/
├── script/
│   └── script.md           ← Full video script & transcript
├── code/
│   ├── verify_setup.py     ← Setup verification script
│   └── setup.sh            ← Automated setup helper (macOS/Linux)
├── assets/
│   └── (placeholder for thumbnails, images)
└── README.md               ← This file
```

---

## 🛠️ Prerequisites (Before Starting)

You'll need to have installed on your system:

### 1. **Conda** (Python Environment Manager)
- Download: https://www.anaconda.com/download
- Alternative: https://docs.conda.io/projects/miniconda/en/latest/

```bash
conda --version
```

### 2. **Node.js** (v20.12+)
- Download: https://nodejs.org/
- Check: `node -v`

### 3. **VS Code** or preferred editor
- Download: https://code.visualstudio.com/

---

## 🚀 Setup Steps (Shown in Video)

### Step 1: Create a Conda Environment

```bash
conda create -n bmad-python python=3.10
conda activate bmad-python
```

**Why?** This keeps BMAD and Python isolated from your system. If something breaks, you can just delete this environment and create a new one.

### Step 2: Check Prerequisites

Inside the activated Conda environment, verify you have all required tools:

```bash
node -v
python --version
uv --version
```

**Expected Output:**
```
v20.12.0    (or higher)
Python 3.10.x
0.4.x       (or higher)
```

**If `uv` is missing:**
```bash
pip install uv
```

### Step 3: Create Project Folder

```bash
mkdir bmad-python-project
cd bmad-python-project
code .
```

This creates a new folder for your BMAD project and opens it in VS Code.

### Step 4: Install BMAD

```bash
npx bmad-method install
```

Or for the prerelease version:
```bash
npx bmad-method@next install
```

This will:
- Download BMAD into a `./_bmad/` folder
- Set up configuration files
- Ask you a few questions about modules and tools
- Create your first BMAD workflows

### Step 5: Create Your First Python File

Create `main.py`:
```python
def main():
    print("BMAD + Python environment is ready!")

if __name__ == "__main__":
    main()
```

Run it:
```bash
python main.py
```

**Expected Output:**
```
BMAD + Python environment is ready!
```

---

## ✅ Verify Your Setup

We've included a verification script to confirm everything is installed correctly:

```bash
python code/verify_setup.py
```

**What it checks:**
- ✅ Node.js is installed (v20.12+)
- ✅ Python is installed (3.10+)
- ✅ uv is installed
- ✅ BMAD folder exists

**Expected Output:**
```
======================================================================
🔍 BMAD + Python Setup Verification
======================================================================

1️⃣  Checking Node.js...
   ✅ Node.js installed: v20.12.0

2️⃣  Checking Python...
   ✅ Python installed: Python 3.10.12
   ✅ Python version is 3.10 or higher

3️⃣  Checking uv (Python package manager)...
   ✅ uv installed: uv 0.4.12

4️⃣  Checking BMAD installation...
   ✅ BMAD folder detected at: C:\Users\...\bmad-python-project\_bmad

======================================================================
✅ All prerequisites are installed!
```

---

## 🚨 Troubleshooting

### "Node.js not found"
- Install from https://nodejs.org/
- Restart your terminal after installation
- Check with `node -v`

### "Python version is too old"
- You need Python 3.10 or higher
- Conda should have installed 3.10 with `conda create -n bmad-python python=3.10`
- Check with `python --version`

### "uv not found"
```bash
pip install uv
uv --version
```

### "BMAD installation failed"
- Make sure you're in the correct folder (`cd bmad-python-project`)
- Make sure the Conda environment is activated (`conda activate bmad-python`)
- Try the prerelease: `npx bmad-method@next install`
- Check the BMAD documentation

### "VS Code can't find Python"
- In VS Code, press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
- Type "Python: Select Interpreter"
- Choose the `bmad-python` environment

---

## 📊 Environment Isolation Explained

**Why do we use Conda?**

Without Conda (BAD):
```
System Python
├── Project A packages
├── Project B packages
├── BMAD packages
└── Conflicts! 💥
```

With Conda (GOOD):
```
System Python
├── Environment: bmad-python
│   ├── Python 3.10
│   ├── BMAD + dependencies
│   ├── Your project packages
│   └── Isolated & safe ✅
└── Other environments...
```

If something breaks in one environment, you just delete it and create a new one. System Python stays clean.

---

## 📖 Full Video Transcript

See `script/script.md` for the complete video script with all explanations and timestamps.

---

## 🎯 Key Takeaways

1. **Conda environments** = isolated Python spaces for each project
2. **Prerequisites** = Node.js, Python 3.10+, and uv must be available
3. **BMAD installation** = automated with `npx bmad-method install`
4. **Verification** = run the verification script to confirm setup
5. **Next step** = Story 1-3 (BMAD Loop Setup) - actually using BMAD

---

## 🔗 Useful Links

- **Anaconda/Miniconda:** https://docs.conda.io/
- **Node.js:** https://nodejs.org/
- **BMAD GitHub:** https://github.com/bmad-code-org/BMAD-METHOD
- **BMAD Docs:** https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md (or project docs)
- **uv Documentation:** https://docs.astral.sh/uv/

---

## 🎬 Video Information

**YouTube Link:** [YouTube Link](https://www.youtube.com/watch?v=UmlzAN7gV-8)
**Published:** 2026-07-31
**Status:** ✅ Published

### Timestamps
- 00:00 – Intro
- 00:25 – Conda environment setup
- 01:45 – Checking prerequisites
- 03:10 – Project folder creation
- 04:00 – BMAD installation
- 07:28 – First Python script
- 08:42 – Recap

---

## 🚀 What's Next?

### Story 1-3: BMAD Loop Setup
In the next episode, you'll learn:
- The difference between Agent Chat (skills) and Terminal (commands)
- How to activate BMAD workflows
- Running your first BMAD workflow
- Understanding the Loop automation engine

---

## ✅ Checklist for Completion

- [ ] Watch the full video
- [ ] Read `script/script.md` for reference
- [ ] Create a Conda environment
- [ ] Check all prerequisites
- [ ] Install BMAD
- [ ] Run `verify_setup.py` and see all ✅ marks
- [ ] Ready for next episode

---

## 💬 Q&A

**Q: Can I use virtual environments instead of Conda?**  
A: Yes, `python -m venv bmad-env` works too, but Conda is cleaner for managing dependencies across projects.

**Q: What's the difference between `bmad-method install` and `bmad-method@next install`?**  
A: `@next` installs the prerelease (bleeding edge). Stable version is recommended for beginners.

**Q: Do I need VS Code specifically?**  
A: No, but VS Code has the best BMAD extension support. Any editor works, though.

**Q: Can I skip Conda and just use system Python?**  
A: Possible, but not recommended. Conda isolation prevents package conflicts.

---

**Ready to level up? Watch Story 1-3 next!** 🎬

---

*Last Updated: 2026-07-31*
*Status: ✅ Ready for Publishing*
