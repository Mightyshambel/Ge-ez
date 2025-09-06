# Installation Guide

This guide will help you install and set up the Ge-ez Amharic Programming Language on your system.

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.7 or higher
- **Memory**: At least 100MB free space
- **Internet**: Required for downloading dependencies

## Installation Methods

### Method 1: Direct Installation (Recommended)

#### Step 1: Download the Repository
```bash
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
```

#### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Verify Installation
```bash
python main.py --help
```

### Method 2: Development Installation

If you plan to contribute to the project:

#### Step 1: Fork and Clone
```bash
# Fork the repository on GitHub first
git clone https://github.com/YOUR_USERNAME/Ge-ez.git
cd Ge-ez
```

#### Step 2: Set Up Development Environment
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e .
```

#### Step 3: Install Development Dependencies
```bash
pip install pytest black flake8 mypy
```

## Platform-Specific Instructions

### Windows

#### Using Command Prompt
```cmd
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py --help
```

#### Using PowerShell
```powershell
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py --help
```

### macOS

```bash
# Install Git if not already installed
brew install git

# Clone and setup
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py --help
```

### Linux (Ubuntu/Debian)

```bash
# Install Git and Python if not already installed
sudo apt update
sudo apt install git python3 python3-pip python3-venv

# Clone and setup
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py --help
```

## Troubleshooting

### Common Issues

#### Issue: "python: command not found"
**Solution**: Install Python 3.7+ or use `python3` instead of `python`

#### Issue: "git: command not found"
**Solution**: Install Git from [git-scm.com](https://git-scm.com/)

#### Issue: "pip: command not found"
**Solution**: 
```bash
# On Linux/macOS
sudo apt install python3-pip  # Ubuntu/Debian
brew install python3         # macOS

# On Windows
python -m ensurepip --upgrade
```

#### Issue: Virtual Environment Activation Fails
**Solution**: 
```bash
# Try different activation commands
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows CMD
.venv\Scripts\Activate.ps1    # Windows PowerShell
```

#### Issue: Permission Denied
**Solution**: 
```bash
# On Linux/macOS
chmod +x .venv/bin/activate

# On Windows, run as Administrator
```

### Python Version Issues

#### Check Python Version
```bash
python --version
# or
python3 --version
```

#### Install Specific Python Version
```bash
# On Ubuntu/Debian
sudo apt install python3.9

# On macOS with Homebrew
brew install python@3.9

# On Windows, download from python.org
```

### Dependency Issues

#### Clear Pip Cache
```bash
pip cache purge
```

#### Reinstall Dependencies
```bash
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

#### Use Specific Python Version
```bash
python3.9 -m venv .venv
source .venv/bin/activate
python3.9 -m pip install -r requirements.txt
```

## Testing Your Installation

### Basic Test
```bash
python main.py examples/simple.geez
```

Expected output:
```
Welcome to Ge-ez! (ጌዝ አማርኛ የፕሮግራሚንግ ቋንቋ)
Amharic Programming Language
========================================
ጌዝ
```

### Interactive Mode Test
```bash
python main.py -i
```

Then type:
```
አለ "ሰላም አማርኛ!"
ውጣ
```

### All Examples Test
```bash
python main.py examples/hello.geez
python main.py examples/math.geez
python main.py examples/loop.geez
```

## Uninstallation

### Remove Virtual Environment
```bash
# Deactivate first
deactivate

# Remove directory
rm -rf .venv
```

### Remove Repository
```bash
cd ..
rm -rf Ge-ez
```

## Getting Help

If you encounter issues:

1. **Check the Issues**: [GitHub Issues](https://github.com/Mightyshambel/Ge-ez/issues)
2. **Create an Issue**: Describe your problem with:
   - Operating system
   - Python version
   - Error messages
   - Steps to reproduce

3. **Community Support**: 
   - GitHub Discussions
   - Create a Pull Request with fixes

## Next Steps

After successful installation:

1. **Read the Documentation**: [README.md](README.md)
2. **Try Examples**: Run the example programs
3. **Learn the Language**: Study Amharic keywords
4. **Create Programs**: Write your own Amharic programs
5. **Contribute**: Help improve the language

## Development Setup

For contributors:

### Install Development Tools
```bash
pip install pytest black flake8 mypy
```

### Run Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black geez/
flake8 geez/
mypy geez/
```

### Pre-commit Hooks
```bash
pip install pre-commit
pre-commit install
```

## Docker Installation (Advanced)

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
```

### Build and Run
```bash
docker build -t ge-ez .
docker run -it ge-ez
```

## Package Installation (Future)

When the package is published to PyPI:

```bash
pip install ge-ez
```

Then use:
```bash
ge-ez examples/hello.geez
```

---

**Need help?** Open an issue on [GitHub](https://github.com/Mightyshambel/Ge-ez/issues)!
