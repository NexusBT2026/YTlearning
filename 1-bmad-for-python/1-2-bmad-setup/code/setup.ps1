# Story 1-2: BMAD Setup Helper Script for Windows
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
# - Windows users (PowerShell or Windows Terminal)
# - Anyone who wants to automate the setup process
# - Learners who want to skip the manual steps
#
# ============================================================================
# HOW TO RUN THIS SCRIPT
# ============================================================================
#
# IMPORTANT: You must allow PowerShell to run scripts first!
#
# Option 1: Run from PowerShell (RECOMMENDED for beginners)
#   1. Open Windows Terminal or PowerShell
#   2. Navigate to this folder:
#      cd path\to\1-bmad-for-python\1-2-bmad-setup\code
#   3. Run this command to allow scripts (one-time setup):
#      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#   4. Run the setup script:
#      .\setup.ps1
#
# Option 2: Run without permanent policy change
#   powershell -ExecutionPolicy Bypass -File setup.ps1
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
#
# ✅ Node.js 20.12+ must be installed
#    - Download from: https://nodejs.org/
#    - Windows installer recommended
#
# ✅ Internet connection
#    - For downloading packages from npm and pip
#
# ============================================================================
# TROUBLESHOOTING
# ============================================================================
#
# "PowerShell doesn't recognize 'conda'"
#   → Add Conda to your PATH or restart PowerShell after installing Conda
#
# "ExecutionPolicy error"
#   → Run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#
# "node: command not found"
#   → Install Node.js and restart PowerShell
#
# ============================================================================

Write-Host "🚀 BMAD + Python Setup Assistant (Windows)" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""

# Step 1: Create Conda environment
Write-Host "📦 Step 1: Creating Conda environment..." -ForegroundColor Cyan
Write-Host "  Environment name: bmad-python" -ForegroundColor Gray
Write-Host "  Python version: 3.10" -ForegroundColor Gray
Write-Host ""

conda create -n bmad-python python=3.10 -y

Write-Host ""
Write-Host "✅ Conda environment created" -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANT: To use the new environment, you need to activate it." -ForegroundColor Yellow
Write-Host "   Run this command in a NEW PowerShell terminal:" -ForegroundColor Yellow
Write-Host "   conda activate bmad-python" -ForegroundColor Yellow
Write-Host ""

# Step 2: Check prerequisites
Write-Host "🔍 Step 2: Checking prerequisites..." -ForegroundColor Cyan
Write-Host ""

Write-Host "Node.js version:" -ForegroundColor Gray
try {
    node -v
} catch {
    Write-Host "⚠️  Node.js not found. Please install from https://nodejs.org/" -ForegroundColor Red
}

Write-Host ""
Write-Host "Python version (in bmad-python environment):" -ForegroundColor Gray
try {
    conda run -n bmad-python python --version
} catch {
    Write-Host "⚠️  Could not check Python version" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "uv version (package manager):" -ForegroundColor Gray
try {
    conda run -n bmad-python uv --version
} catch {
    Write-Host "⚠️  uv not found. Installing..." -ForegroundColor Yellow
    conda run -n bmad-python pip install uv -q
    Write-Host "✅ uv installed" -ForegroundColor Green
}

Write-Host ""

# Step 3: Create project structure
Write-Host "📂 Step 3: Creating project structure..." -ForegroundColor Cyan
New-Item -ItemType Directory -Path "code" -Force | Out-Null
New-Item -ItemType Directory -Path "scripts" -Force | Out-Null
New-Item -ItemType Directory -Path "docs" -Force | Out-Null

Write-Host "✅ Folders created:" -ForegroundColor Green
Write-Host "   - code/" -ForegroundColor Gray
Write-Host "   - scripts/" -ForegroundColor Gray
Write-Host "   - docs/" -ForegroundColor Gray
Write-Host ""

# Step 4: Install BMAD (optional)
Write-Host "💡 Step 4: Installing BMAD Method..." -ForegroundColor Cyan
Write-Host ""
Write-Host "BMAD installation is done separately. When ready, run one of these:" -ForegroundColor Gray
Write-Host ""
Write-Host "  Stable release:" -ForegroundColor Gray
Write-Host "    npx bmad-method install" -ForegroundColor White
Write-Host ""
Write-Host "  Prerelease (cutting edge):" -ForegroundColor Gray
Write-Host "    npx bmad-method@next install" -ForegroundColor White
Write-Host ""

# Step 5: Verification
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Next steps:" -ForegroundColor Cyan
Write-Host "  1. Open a NEW PowerShell terminal" -ForegroundColor Gray
Write-Host "  2. Run: conda activate bmad-python" -ForegroundColor Gray
Write-Host "  3. Navigate to your project folder" -ForegroundColor Gray
Write-Host "  4. Run: npx bmad-method install" -ForegroundColor Gray
Write-Host ""
Write-Host "🎉 Happy coding!" -ForegroundColor Green
