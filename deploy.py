#!/usr/bin/env python3
"""
Deployment script for Ge-ez (ግእዝ)
Handles building, testing, and deploying the package
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        sys.exit(1)


def clean_build():
    """Clean build artifacts."""
    print("🧹 Cleaning build artifacts...")
    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for pattern in dirs_to_clean:
        if "*" in pattern:
            import glob

            for path in glob.glob(pattern):
                if os.path.isdir(path):
                    shutil.rmtree(path)
        elif os.path.exists(pattern):
            shutil.rmtree(pattern)
    print("✅ Build artifacts cleaned")


def run_tests():
    """Run the test suite."""
    run_command("python -m pytest tests/ -v", "Running tests")


def run_linting():
    """Run code quality checks."""
    run_command("black --check .", "Code formatting check")
    run_command("isort --check-only .", "Import sorting check")
    run_command("flake8 geez/ tests/", "Linting check")
    run_command("mypy geez/", "Type checking")


def build_package():
    """Build the package."""
    run_command("python -m build", "Building package")


def check_package():
    """Check the built package."""
    run_command("twine check dist/*", "Checking package")


def deploy_to_pypi():
    """Deploy to PyPI."""
    if input("🚀 Deploy to PyPI? (y/N): ").lower() == "y":
        run_command("twine upload dist/*", "Deploying to PyPI")
    else:
        print("⏭️ Skipping PyPI deployment")


def deploy_docs():
    """Deploy documentation."""
    if input("📚 Deploy documentation? (y/N): ").lower() == "y":
        run_command("mkdocs build", "Building documentation")
        run_command("mkdocs gh-deploy", "Deploying documentation")
    else:
        print("⏭️ Skipping documentation deployment")


def main():
    """Main deployment process."""
    print("🚀 Ge-ez Deployment Script")
    print("=" * 50)

    # Check if we're in the right directory
    if not os.path.exists("setup.py"):
        print("❌ Error: setup.py not found. Please run from project root.")
        sys.exit(1)

    # Clean previous builds
    clean_build()

    # Run tests
    run_tests()

    # Run linting
    run_linting()

    # Build package
    build_package()

    # Check package
    check_package()

    # Deploy options
    deploy_to_pypi()
    deploy_docs()

    print("\n🎉 Deployment process completed!")
    print("📦 Package built in dist/ directory")
    print("📚 Documentation available locally")


if __name__ == "__main__":
    main()
