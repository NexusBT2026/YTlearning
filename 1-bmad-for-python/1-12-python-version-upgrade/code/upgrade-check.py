#!/usr/bin/env python3
"""
upgrade-check.py

Quick diagnostic script to check Python version and tomllib availability.
This script validates whether your Python installation meets BMAD requirements.

Usage:
    python upgrade-check.py

Exit Codes:
    0 = All checks passed (Python 3.11+ with tomllib available)
    1 = Python version too old (< 3.11)
    2 = tomllib not available
"""

import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.11 or higher."""
    version_info = sys.version_info
    version_str = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
    
    print(f"📍 Current Python Version: {version_str}")
    
    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 11):
        print("❌ FAIL: Python 3.11+ required")
        return False
    
    print("✅ PASS: Python version is 3.11 or higher")
    return True


def check_tomllib():
    """Check if tomllib is available in stdlib."""
    try:
        import tomllib
        print("✅ PASS: tomllib is available")
        return True
    except ImportError:
        print("❌ FAIL: tomllib not found (Python 3.11+ required)")
        return False


def check_bmad_scripts():
    """Verify that BMAD scripts can be imported."""
    # Navigate from code/upgrade-check.py → 1-12-python-version-upgrade/ → 1-bmad-for-python/ → project root
    bmad_script_dir = Path(__file__).parent.parent.parent.parent / "_bmad" / "scripts"
    
    print(f"\n📂 Looking for BMAD scripts in: {bmad_script_dir}")
    
    if not bmad_script_dir.exists():
        print("⚠️  WARNING: _bmad/scripts directory not found (not in project root)")
        return None
    
    resolve_customization = bmad_script_dir / "resolve_customization.py"
    resolve_config = bmad_script_dir / "resolve_config.py"
    
    if resolve_customization.exists():
        print(f"✅ Found: resolve_customization.py")
    else:
        print(f"❌ Missing: resolve_customization.py")
    
    if resolve_config.exists():
        print(f"✅ Found: resolve_config.py")
    else:
        print(f"❌ Missing: resolve_config.py")
    
    return resolve_customization.exists() and resolve_config.exists()


def main():
    """Run all checks and report results."""
    print("=" * 60)
    print("BMAD Python Environment Check")
    print("=" * 60)
    print()
    
    # Step 1: Check Python version
    version_ok = check_python_version()
    print()
    
    # Step 2: Check tomllib
    tomllib_ok = check_tomllib()
    print()
    
    # Step 3: Check BMAD scripts
    scripts_ok = check_bmad_scripts()
    print()
    
    # Summary
    print("=" * 60)
    print("Summary:")
    print("=" * 60)
    
    if version_ok and tomllib_ok:
        print("✅ Your environment is ready for BMAD!")
        print()
        print("Next steps:")
        print("  1. Run your BMAD scripts with confidence")
        print("  2. If you're updating from Python 3.10, remember:")
        print("     - conda update --all  (to sync all dependencies)")
        print("     - Restart your IDE and terminal")
        return 0
    else:
        print("❌ Your environment needs updating")
        print()
        print("Action required:")
        if not version_ok:
            print("  • Upgrade Python to 3.11 or higher")
            print("    Command: conda install python=3.12")
        if not tomllib_ok:
            print("  • tomllib will be available after upgrading Python")
        print()
        print("After upgrading:")
        print("  • Run: conda update --all")
        print("  • Run this script again to verify")
        return 1


if __name__ == "__main__":
    sys.exit(main())
