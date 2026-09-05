#!/bin/bash
# Story 1-2: BMAD Setup Helper Script for Linux / macOS / WSL
# Automates the BMAD + Python environment setup for your convenience
#
# ============================================================================
# WHAT IS THIS SCRIPT?
# ============================================================================
# This script automates all the setup steps shown in the video, so you don't
# have to run each command manually. It creates the Conda environment,
# checks prerequisites, and prepares your project folder for BMAD.
#
# WHO SHOULD USE THIS?
# - Linux and macOS users
# - Windows users with WSL (Windows Subsystem for Linux)
# - Windows users with Git Bash installed
# - Anyone who wants to automate the setup process
#
# ============================================================================
# HOW TO RUN THIS SCRIPT
# ============================================================================
#
# Step 1: Open your terminal
#   - Linux: Terminal app
#   - macOS: Terminal or iTerm2
#   - WSL: Open "Ubuntu" or your WSL distribution
#   - Git Bash: Right-click in folder → "Git Bash Here"
#
# Step 2: Navigate to this folder
#   cd path/to/1-bmad-for-python/1-2-bmad-setup/code
#
# Step 3: Run the setup script
#   bash setup.sh
#
# That's it! The script will handle everything else.
#
# ============================================================================
# WHAT THIS SCRIPT DOES (Step by Step)
# ============================================================================
#
# Step 1: Creates a new Conda environment called "bmad-python" with Python 3.10
# Step 2: Activates the environment so you're inside it
# Step 3: Checks your Node.js version (should be 20.12 or higher)
# Step 4: Checks your Python version (should be 3.10 or higher)
# Step 5: Checks/installs uv (Python package manager)
# Step 6: Creates project folders (code, scripts, docs)
# Step 7: Shows instructions for installing BMAD
#
# ============================================================================
# REQUIREMENTS (Before running this script)
# ============================================================================
#
# ✅ Conda/Anaconda must be installed
#    - Download from: https://www.anaconda.com/download
#    - Or use Miniconda: https://docs.conda.io/en/latest/miniconda.html
#    - Check: run "conda --version" in your terminal
#
# ✅ Node.js 20.12+ must be installed
#    - Download from: https://nodejs.org/
#    - Check: run "node -v" in your terminal
#
# ✅ Internet connection
#    - For downloading packages from npm and pip
#
# ============================================================================
# TROUBLESHOOTING
# ============================================================================
#
# "command: conda not found"
#   → Conda is not installed. Download from https://www.anaconda.com/download
#   → Or reload your terminal after installing Conda
#
# "command: node not found"
#   → Install Node.js from https://nodejs.org/
#
# "permission denied"
#   → Run: chmod +x setup.sh
#   → Then: bash setup.sh
#
# ============================================================================

echo "🚀 BMAD + Python Setup Assistant (Linux / macOS / WSL)"
echo "====================================================="
echo ""

# Step 1: Create Conda environment
echo "📦 Step 1: Creating Conda environment..."
echo "  Environment name: bmad-python"
echo "  Python version: 3.10"
echo ""

conda create -n bmad-python python=3.10 -y
conda activate bmad-python

echo ""
echo "✅ Conda environment created and activated"
echo ""

# Step 2: Check prerequisites
echo "🔍 Step 2: Checking prerequisites..."
echo ""

echo "Node.js version:"
node -v
echo ""

echo "Python version (in bmad-python environment):"
python --version
echo ""

echo "uv version (package manager):"
uv --version 2>/dev/null || echo "⚠️  uv not found. Installing..."

if ! command -v uv &> /dev/null; then
    pip install uv -q
    echo "✅ uv installed"
fi

echo ""

# Step 3: Create project structure
echo "📂 Step 3: Creating project structure..."
mkdir -p code
mkdir -p scripts
mkdir -p docs

echo "✅ Folders created:"
echo "   - code/"
echo "   - scripts/"
echo "   - docs/"
echo ""

# Step 4: Install BMAD (optional)
echo "💡 Step 4: Installing BMAD Method..."
echo ""
echo "BMAD installation is done separately. When ready, run one of these:"
echo ""
echo "  Stable release:"
echo "    npx bmad-method install"
echo ""
echo "  Prerelease (cutting edge):"
echo "    npx bmad-method@next install"
echo ""

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "  1. Activate the bmad-python environment:"
echo "     conda activate bmad-python"
echo ""
echo "  2. Navigate to your project folder"
echo ""
echo "  3. Install BMAD when ready:"
echo "     npx bmad-method install"
echo ""
echo "Happy coding! 🎉"
