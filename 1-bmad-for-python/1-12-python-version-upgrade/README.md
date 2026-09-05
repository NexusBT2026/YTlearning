# Story 1-12: Python Version Upgrade — Why tomllib Matters (Conda Fix)

## 📺 Episode Overview

**Title:** Why Your Python Code Breaks (And How to Fix It with Conda)

**Duration:** ~8-10 minutes  
**Difficulty:** Intermediate

This is a bonus deep-dive episode addressing a critical issue discovered mid-sprint: the BMAD configuration scripts require Python 3.11+ due to the `tomllib` standard library. Learn why the upgrade is necessary and how to use Conda to safely modernize your environment without breaking your workflow.

---

## 🎯 Learning Objectives

After watching this episode, you'll understand:

- ✅ Why `tomllib` matters and why Python 3.10 is no longer sufficient
- ✅ How `resolve_customization.py` and `resolve_config.py` depend on `tomllib`
- ✅ The different upgrade paths for **venv**, **Poetry**, and **Conda** users
- ✅ Why **Conda treats Python as a package** (and why that's powerful)
- ✅ How to safely upgrade Python 3.10 → 3.12 in-place with zero downtime
- ✅ How to ensure all dependencies align after an in-place upgrade using `conda update --all`

## 🛠️ Prerequisites (Before Starting)

You'll need:

- **Python 3.10** currently installed in an active Conda environment
- **Conda** installed and running
- **VS Code** with integrated terminal
- Access to the YTlearning project folder

---

## 🚀 Upgrade Steps (Shown in Video)

### Step 1: Check Your Current Python Version

```powershell
python --version
```

If you see `Python 3.10.x`, you need to upgrade.

### Step 2: Activate Your Conda Environment

Make sure you're inside your Conda environment (e.g., `bmad-python`):

```powershell
conda activate bmad-python
```

### Step 3: Upgrade Python to 3.12

```powershell
conda install python=3.12
```

Conda will show you a Package Plan. Review it and type `y` to proceed.

### Step 4: Verify the Upgrade

```powershell
python --version
```

You should now see `Python 3.12.x`.

### Step 5: Update All Dependencies

```powershell
conda update --all
```

This ensures all your packages are compatible with Python 3.12.

### Step 6: Verify BMAD Scripts Work

```powershell
python _bmad/scripts/resolve_customization.py
```

If this runs without "tomllib not found" errors, you're done!

---

## ✅ Verify Your Upgrade

We've included a verification script to confirm everything is working:

```powershell
python code/upgrade-check.py
```

**Expected Output:**
```
✅ Current Python Version: 3.12.x
✅ PASS: Python version is 3.11 or higher
✅ PASS: tomllib is available
✅ Your environment is ready for BMAD!
```

---

## 🚨 Troubleshooting

### "tomllib not found" error
- You're still on Python 3.10 or older
- Run: `conda install python=3.12`
- Then: `conda update --all`
- Restart your terminal

### "conda command not found"
- Install Conda from: https://www.anaconda.com/download
- Or use Miniconda: https://docs.conda.io/projects/miniconda/

### Environment won't update
- Make sure you're inside the correct Conda environment
- Check with: `conda info --envs`
- Activate with: `conda activate bmad-python`
