# Installation Guide

This guide will help you install Ge-ez (ግእዝ) on your system.

## 🚀 Quick Installation

### From PyPI (Recommended)
```bash
pip install geez-lang
```

### From Source
```bash
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
pip install -r requirements.txt
pip install -e .
```

## 📋 Prerequisites

- **Python 3.7+** (Python 3.8+ recommended)
- **pip** (Python package installer)
- **Git** (for source installation)

### Check Python Version
```bash
python3 --version
# or
python --version
```

### Check pip Installation
```bash
pip --version
# or
pip3 --version
```

## 🖥️ Platform-Specific Instructions

### Windows

#### Option 1: Using pip
```cmd
pip install geez-lang
```

#### Option 2: From Source
```cmd
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
pip install -r requirements.txt
pip install -e .
```

### macOS

#### Using Homebrew (Recommended)
```bash
# Install Python if not already installed
brew install python

# Install Ge-ez
pip3 install geez-lang
```

#### From Source
```bash
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
pip3 install -r requirements.txt
pip3 install -e .
```

### Linux (Ubuntu/Debian)

#### Using apt
```bash
# Install Python and pip
sudo apt update
sudo apt install python3 python3-pip

# Install Ge-ez
pip3 install geez-lang
```

#### From Source
```bash
# Install dependencies
sudo apt install git python3 python3-pip

# Clone and install
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
pip3 install -r requirements.txt
pip3 install -e .
```

### Linux (CentOS/RHEL/Fedora)

#### Using yum/dnf
```bash
# Install Python and pip
sudo yum install python3 python3-pip
# or for newer versions
sudo dnf install python3 python3-pip

# Install Ge-ez
pip3 install geez-lang
```

## 🔧 Development Installation

If you want to contribute to Ge-ez or run it in development mode:

```bash
# Clone the repository
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez

# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy
```

## ✅ Verify Installation

After installation, verify that Ge-ez is working correctly:

```bash
# Check version
geez --version

# Run a simple test
geez --help

# Test with a simple program
echo 'ማተም "ሰላም ዓለም!"' > test.geez
geez test.geez
```

Expected output:
```
ሰላም ዓለም!
```

## 🐛 Troubleshooting

### Common Issues

#### 1. "geez: command not found"
**Solution:** Make sure the installation directory is in your PATH, or use:
```bash
python3 -m geez your_file.geez
```

#### 2. "No module named 'geez'"
**Solution:** Reinstall the package:
```bash
pip uninstall geez-lang
pip install geez-lang
```

#### 3. Permission Errors
**Solution:** Use user installation:
```bash
pip install --user geez-lang
```

#### 4. Python Version Issues
**Solution:** Make sure you're using Python 3.7+:
```bash
python3 --version
# If version is too old, install a newer version
```

### Unicode/Encoding Issues

If you encounter Unicode issues with Amharic text:

#### Windows
```cmd
chcp 65001
set PYTHONIOENCODING=utf-8
```

#### Linux/macOS
```bash
export PYTHONIOENCODING=utf-8
```

## 🔄 Updating Ge-ez

To update to the latest version:

```bash
pip install --upgrade geez-lang
```

## 🗑️ Uninstalling Ge-ez

To remove Ge-ez from your system:

```bash
pip uninstall geez-lang
```

## 📦 Alternative Installation Methods

### Using conda (Coming Soon)
```bash
conda install -c conda-forge geez-lang
```

### Using Docker (Coming Soon)
```bash
docker pull mightyshambel/geez:latest
docker run -it mightyshambel/geez:latest
```

## 🆘 Getting Help

If you encounter any issues during installation:

1. **Check the [Issues](https://github.com/Mightyshambel/Ge-ez/issues)** page on GitHub
2. **Create a new issue** with details about your problem
3. **Join our community** discussions
4. **Check the documentation** for troubleshooting tips

## 🎉 Next Steps

After successful installation:

1. **Read the [Getting Started](getting-started.md)** guide
2. **Try the [Examples](examples/)** 
3. **Explore the [Language Reference](language-reference.md)**
4. **Join the community** and start coding in Amharic!

---

**Welcome to the world of Amharic programming! 🇪🇹**