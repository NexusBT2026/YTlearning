#!/usr/bin/env python3
"""
main.py

Best practices for Conda environment management and Python version handling.

This module demonstrates:
1. Detecting Python version at runtime
2. Loading TOML configuration with tomllib
3. Handling version compatibility issues gracefully
4. Providing helpful error messages for users with older Python versions

Usage:
    python main.py
"""

import sys
from pathlib import Path


def check_python_compatibility():
    """
    Validate Python version and provide helpful guidance if needed.
    
    Returns:
        tuple: (is_compatible: bool, message: str)
    """
    version_info = sys.version_info
    version_str = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
    
    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 11):
        error_msg = (
            f"\n❌ Python Version Error\n"
            f"   Current: Python {version_str}\n"
            f"   Required: Python 3.11+\n\n"
            f"Why? BMAD configuration scripts use tomllib (stdlib), which was\n"
            f"introduced in Python 3.11. Your environment needs updating.\n\n"
            f"Quick Fix (Conda):\n"
            f"   conda install python=3.12\n"
            f"   conda update --all\n\n"
            f"Learn more: Watch Story 1-12 — Python Version Upgrade Guide\n"
        )
        return False, error_msg
    
    return True, version_str


def load_toml_config(config_path: str) -> dict:
    """
    Load a TOML configuration file using tomllib.
    
    This requires Python 3.11+. If you see ImportError here,
    your Python version needs updating.
    
    Args:
        config_path: Path to the .toml file
        
    Returns:
        dict: Parsed TOML configuration
        
    Raises:
        ImportError: If tomllib is not available (Python < 3.11)
        FileNotFoundError: If config file doesn't exist
    """
    try:
        import tomllib
    except ImportError:
        raise ImportError(
            "tomllib not found. Python 3.11+ is required. "
            "Run: conda install python=3.12 && conda update --all"
        )
    
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_file, "rb") as f:
        return tomllib.load(f)


class BMadEnvironmentManager:
    """
    Manages BMAD environment compatibility and configuration.
    
    This class demonstrates best practices for:
    - Version checking at initialization
    - Graceful error handling
    - Helpful user guidance
    """
    
    def __init__(self):
        """Initialize the environment manager with compatibility check."""
        self.compatible, self.version = check_python_compatibility()
        
        if not self.compatible:
            raise RuntimeError(self.version)
        
        print(f"✅ Environment initialized (Python {self.version})")
    
    def load_bmad_config(self, config_name: str = "config.toml") -> dict:
        """
        Load BMAD configuration file.
        
        Args:
            config_name: Name of config file (relative to _bmad/)
            
        Returns:
            dict: Parsed configuration
        """
        # Navigate from this file to project root, then to _bmad/
        project_root = Path(__file__).parent.parent.parent.parent
        config_path = project_root / "_bmad" / config_name
        
        return load_toml_config(str(config_path))


def main():
    """Demonstrate BMAD environment management."""
    print("=" * 60)
    print("BMAD Environment Manager — Demo")
    print("=" * 60)
    print()
    
    # Step 1: Check compatibility
    print("Step 1: Checking Python compatibility...")
    compatible, info = check_python_compatibility()
    
    if compatible:
        print(f"✅ Python {info} is compatible")
    else:
        print(info)
        return 1
    
    print()
    
    # Step 2: Initialize manager
    print("Step 2: Initializing BMAD Environment Manager...")
    try:
        manager = BMadEnvironmentManager()
    except RuntimeError as e:
        print(f"❌ Initialization failed: {e}")
        return 1
    
    print()
    
    # Step 3: Demonstrate TOML loading (if config exists)
    print("Step 3: Attempting to load BMAD configuration...")
    try:
        config = manager.load_bmad_config()
        print("✅ Successfully loaded config.toml")
        print(f"   Found {len(config)} top-level sections")
        if config:
            print(f"   Sections: {', '.join(list(config.keys())[:3])}...")
    except FileNotFoundError as e:
        print(f"⚠️  Config file not found (this is OK for demo): {e}")
    except Exception as e:
        print(f"❌ Failed to load config: {e}")
        return 1
    
    print()
    print("=" * 60)
    print("✅ All checks passed!")
    print("=" * 60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
