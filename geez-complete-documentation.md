# Ge-ez (ግእዝ) - Complete Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Language Reference](#language-reference)
4. [Examples](#examples)
5. [Installation](#installation)
6. [Contributing](#contributing)
7. [API Reference](#api-reference)
8. [Tutorials](#tutorials)
9. [FAQ](#faq)

---

## Introduction

Welcome to Ge-ez (ግእዝ), the world's first complete Amharic programming language! 

### 🌟 Features
- Complete Amharic syntax
- Object-oriented programming
- File I/O operations
- Error handling
- Modern data structures

### 🚀 Quick Start
```amharic
ማተም "ሰላም ዓለም!"
```

### 📖 Learn More
- [Getting Started Guide](#getting-started)
- [Language Reference](#language-reference)
- [Examples](#examples)
- [Installation](#installation)

### 🌐 Try Online
Interactive Playground - Write and run Ge-ez code in your browser!

### 🤝 Contributing
We welcome contributions! See our [Contributing Guide](#contributing).

### 📄 License
MIT License - see LICENSE file.

---
**Made with ❤️ for the Amharic-speaking programming community**

---

## Getting Started

### What is Ge-ez?
Ge-ez (ግእዝ) is the world's first complete Amharic programming language, designed to make programming accessible to Amharic speakers.

### Installation

#### Using pip
```bash
pip install geez-lang
```

#### From source
```bash
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
pip install -e .
```

### Your First Program

Create a file called `hello.geez`:

```amharic
ማተም "ሰላም ዓለም!"
```

Run it:
```bash
geez hello.geez
```

### Basic Concepts

#### Variables
```amharic
አስተዋውቅ ስም = "አሊ"
አስተዋውቅ አድሜ = 25
```

#### Functions
```amharic
ዘዴ ማተም_ስም(ስም) {
    ማተም "ስም:", ስም
}

ማተም_ስም("አሊ")
```

#### Classes
```amharic
ክፍል ሰው {
    ዘዴ መጀመሪያ(ራሱ, ስም) {
        ራሱ.ስም = ስም
    }
}

አስተዋውቅ ሰው_1 = አዲስ ሰው("አሊ")
```

---

## Language Reference

### Keywords

#### Variable Declaration
- `አስተዋውቅ` - Declare variable

#### Control Flow
- `ከሆነ` - If
- `አለዚያ` - Else
- `ሳለ` - While
- `ለ` - For

#### Functions
- `ዘዴ` - Function/Method
- `መጀመሪያ` - Constructor
- `መልስ` - Return

#### Classes
- `ክፍል` - Class
- `አዲስ` - New
- `ራሱ` - Self/This
- `ተወላጅ` - Inherits

#### I/O Operations
- `ማተም` - Print
- `ግብአት` - Input
- `አንብብ` - Read file
- `ጻፍ` - Write file
- `ጨምር` - Append file

#### Error Handling
- `ሞክር` - Try
- `ያዝ` - Catch
- `በመጨረሻ` - Finally
- `አስተላልፍ` - Throw

### Data Types

#### Numbers
```amharic
አስተዋውቅ ቁጥር = 42
አስተዋውቅ አስርዮሽ = 3.14
```

#### Strings
```amharic
አስተዋውቅ ጽሑፍ = "ሰላም"
```

#### Booleans
```amharic
አስተዋውቅ እውነት = እውነት
አስተዋውቅ ሐሰት = ሐሰት
```

#### Lists
```amharic
አስተዋውቅ ዝርዝር = [1, 2, 3]
```

#### Dictionaries
```amharic
አስተዋውቅ መዝገብ = {"ስም": "አሊ", "አድሜ": 25}
```

### Operators

#### Arithmetic
- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division
- `%` - Modulo

#### Comparison
- `==` - Equal
- `!=` - Not equal
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal
- `>=` - Greater than or equal

#### Logical
- `እና` - And
- `ወይም` - Or
- `አይደለም` - Not

### Built-in Functions

#### String Functions
- `ርዝመት(ጽሑፍ)` - Length
- `መከፋፈል(ጽሑፍ, አልጋ)` - Split
- `አገናኝ(ዝርዝር)` - Join
- `ወደላይ(ጽሑፍ)` - Upper
- `ወደታች(ጽሑፍ)` - Lower

#### Utility Functions
- `ወሰን(ዝርዝር)` - Range
- `ዓይነት(ተለዋዋጭ)` - Type
- `ቁጥር(ጽሑፍ)` - Number
- `ጽሑፍ(ቁጥር)` - String

---

## Examples

### Basic Examples

#### Hello World
```amharic
ማተም "ሰላም ዓለም!"
```

#### Variables and Math
```amharic
አስተዋውቅ ሀ = 10
አስተዋውቅ ለ = 20
አስተዋውቅ ድምር = ሀ + ለ
ማተም "ድምር:", ድምር
```

#### User Input
```amharic
አስተዋውቅ ስም = ግብአት "ስምህን አስገባ:"
ማተም "ሰላም", ስም
```

### Control Flow

#### If-Else
```amharic
አስተዋውቅ አድሜ = 18

ከሆነ አድሜ >= 18 {
    ማተም "አዋቂ"
} አለዚያ {
    ማተም "ልጅ"
}
```

#### While Loop
```amharic
አስተዋውቅ ቁጥር = 1

ሳለ ቁጥር <= 5 {
    ማተም ቁጥር
    ቁጥር = ቁጥር + 1
}
```

#### For Loop
```amharic
ለ አስተዋውቅ እ = 1 እስከ 5 {
    ማተም እ
}
```

### Functions

#### Simple Function
```amharic
ዘዴ ማተም_ስም(ስም) {
    ማተም "ስም:", ስም
}

ማተም_ስም("አሊ")
```

#### Function with Return
```amharic
ዘዴ ድምር(ሀ, ለ) {
    መልስ ሀ + ለ
}

አስተዋውቅ ውጤት = ድምር(5, 3)
ማተም ውጤት
```

### Classes and Objects

#### Simple Class
```amharic
ክፍል ሰው {
    ዘዴ መጀመሪያ(ራሱ, ስም, አድሜ) {
        ራሱ.ስም = ስም
        ራሱ.አድሜ = አድሜ
    }
    
    ዘዴ ማተም_መረጃ(ራሱ) {
        ማተም "ስም:", ራሱ.ስም
        ማተም "አድሜ:", ራሱ.አድሜ
    }
}

አስተዋውቅ ሰው_1 = አዲስ ሰው("አሊ", 25)
ሰው_1.ማተም_መረጃ()
```

### File Operations

#### Write File
```amharic
ጻፍ "test.txt" "ሰላም ዓለም!"
```

#### Read File
```amharic
አስተዋውቅ ይዘት = አንብብ "test.txt"
ማተም ይዘት
```

#### Append File
```amharic
ጨምር "test.txt" "አዲስ መስመር"
```

### Error Handling

#### Try-Catch
```amharic
ሞክር {
    አስተዋውቅ ቁጥር = 10 / 0
} ያዝ (ስህተት) {
    ማተም "ስህተት ተገኝቷል:", ስህተት
} በመጨረሻ {
    ማተም "በመጨረሻ ተጠናቋል"
}
```

#### Throw Error
```amharic
ዘዴ አረጋግጥ(አድሜ) {
    ከሆነ አድሜ < 0 {
        አስተላልፍ "አድሜ አሉታዊ ሊሆን አይችልም"
    }
}
```

### Data Structures

#### Lists
```amharic
አስተዋውቅ ዝርዝር = [1, 2, 3, 4, 5]

ለ አስተዋውቅ ንጥል በ ዝርዝር {
    ማተም ንጥል
}
```

#### Dictionaries
```amharic
አስተዋውቅ መዝገብ = {
    "ስም": "አሊ",
    "አድሜ": 25,
    "ከተማ": "አዲስ አበባ"
}

ማተም መዝገብ["ስም"]
```

### Advanced Examples

#### Calculator
```amharic
ዘዴ ካልኩሌተር(ሀ, ለ, ስራ) {
    ከሆነ ስራ == "+" {
        መልስ ሀ + ለ
    } አለዚያ ከሆነ ስራ == "-" {
        መልስ ሀ - ለ
    } አለዚያ ከሆነ ስራ == "*" {
        መልስ ሀ * ለ
    } አለዚያ ከሆነ ስራ == "/" {
        መልስ ሀ / ለ
    } አለዚያ {
        አስተላልፍ "ያልታወቀ ስራ"
    }
}

አስተዋውቅ ውጤት = ካልኩሌተር(10, 5, "+")
ማተም "ውጤት:", ውጤት
```

#### File Manager
```amharic
ክፍል ፋይል_መቆጣጠሪያ {
    ዘዴ መጀመሪያ(ራሱ) {
        ማተም "ፋይል መቆጣጠሪያ ተጀመረ"
    }
    
    ዘዴ ፋይል_ፍጠር(ራሱ, ስም, ይዘት) {
        ጻፍ ስም ይዘት
        ማተም "ፋይል ተፈጥሯል:", ስም
    }
    
    ዘዴ ፋይል_አንብብ(ራሱ, ስም) {
        አስተዋውቅ ይዘት = አንብብ ስም
        መልስ ይዘት
    }
}

አስተዋውቅ ፋይል_መቆጣጠሪያ_1 = አዲስ ፋይል_መቆጣጠሪያ()
ፋይል_መቆጣጠሪያ_1.ፋይል_ፍጠር("test.txt", "ሰላም ዓለም!")
```

---

## Installation

### System Requirements
- Python 3.7 or higher
- pip package manager

### Installation Methods

#### Method 1: Using pip (Recommended)
```bash
pip install geez-lang
```

#### Method 2: From Source
```bash
# Clone the repository
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez

# Install in development mode
pip install -e .
```

#### Method 3: Using conda
```bash
conda install -c conda-forge geez-lang
```

### Verification
After installation, verify Ge-ez is working:

```bash
geez --version
```

### Running Ge-ez Programs

#### Command Line
```bash
geez program.geez
```

#### Interactive Mode
```bash
geez
```

#### Python Integration
```python
from geez import GeEzInterpreter

interpreter = GeEzInterpreter()
interpreter.execute("ማተም 'ሰላም ዓለም!'")
```

### Troubleshooting

#### Common Issues

##### Python Version
Make sure you have Python 3.7+:
```bash
python --version
```

##### Permission Errors
Use `--user` flag:
```bash
pip install --user geez-lang
```

##### Virtual Environment
Create a virtual environment:
```bash
python -m venv geez-env
source geez-env/bin/activate  # On Windows: geez-env\Scripts\activate
pip install geez-lang
```

### Development Setup
For contributing to Ge-ez:

```bash
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
pip install -e .
pip install -r requirements-dev.txt
```

### Uninstallation
```bash
pip uninstall geez-lang
```

### Getting Help
- Documentation
- GitHub Issues
- Community Forum

---

## Contributing

Thank you for your interest in contributing to Ge-ez (ግእዝ)! We welcome contributions from the community.

### How to Contribute

#### 1. Fork the Repository
1. Go to [Ge-ez GitHub repository](https://github.com/Mightyshambel/Ge-ez)
2. Click "Fork" button
3. Clone your fork locally

#### 2. Set Up Development Environment
```bash
git clone https://github.com/YOUR_USERNAME/Ge-ez.git
cd Ge-ez
pip install -e .
pip install -r requirements-dev.txt
```

#### 3. Make Changes
- Create a new branch: `git checkout -b feature/your-feature`
- Make your changes
- Test your changes: `python -m pytest tests/`

#### 4. Submit Pull Request
- Commit your changes: `git commit -m "Add your feature"`
- Push to your fork: `git push origin feature/your-feature`
- Create a Pull Request

### Areas for Contribution

#### Language Features
- New keywords and syntax
- Built-in functions
- Data structures
- Error handling improvements

#### Documentation
- Tutorials and examples
- Language reference updates
- Translation to other languages
- Video tutorials

#### Tools and Ecosystem
- IDE extensions
- Syntax highlighters
- Package managers
- Build tools

#### Testing
- Unit tests
- Integration tests
- Performance benchmarks
- Example programs

### Code Style

#### Python Code
- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions small and focused

#### Ge-ez Code
- Use meaningful Amharic names
- Comment complex logic
- Follow existing patterns
- Test thoroughly

### Testing

#### Running Tests
```bash
python -m pytest tests/
```

#### Writing Tests
- Test both success and failure cases
- Use descriptive test names
- Keep tests simple and focused
- Test edge cases

### Documentation

#### Writing Documentation
- Use clear, simple language
- Include examples
- Update when adding features
- Test all code examples

#### Translation
We welcome translations! Please:
- Maintain the same structure
- Keep examples consistent
- Test translated examples
- Update when source changes

### Community Guidelines

#### Be Respectful
- Use inclusive language
- Respect different skill levels
- Be patient with questions
- Help others learn

#### Communication
- Use English for technical discussions
- Amharic is welcome for examples and documentation
- Be clear and concise
- Ask questions when unsure

### Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Invited to maintainer discussions
- Given credit in documentation

### Questions?

- GitHub Discussions
- GitHub Issues
- Email: [your-email@example.com]

Thank you for helping make Ge-ez better for everyone! 🙏

---

## API Reference

### GeEzInterpreter Class

#### Methods

##### `execute(code: str) -> Any`
Execute Ge-ez code and return the result.

##### `execute_file(filename: str) -> Any`
Execute a Ge-ez file and return the result.

##### `get_variables() -> Dict[str, Any]`
Get all current variables.

##### `clear_variables()`
Clear all variables.

### GeEzLexer Class

#### Methods

##### `tokenize(code: str) -> List[Token]`
Tokenize Ge-ez code into tokens.

### GeEzParser Class

#### Methods

##### `parse(tokens: List[Token]) -> ASTNode`
Parse tokens into an Abstract Syntax Tree.

### Built-in Functions

#### String Functions
- `ርዝመት(ጽሑፍ)` - Get string length
- `መከፋፈል(ጽሑፍ, አልጋ)` - Split string
- `አገናኝ(ዝርዝር)` - Join list
- `ወደላይ(ጽሑፍ)` - Convert to uppercase
- `ወደታች(ጽሑፍ)` - Convert to lowercase

#### Utility Functions
- `ወሰን(መጀመሪያ, መጨረሻ)` - Create range
- `ዓይነት(ተለዋዋጭ)` - Get variable type
- `ቁጥር(ጽሑፍ)` - Convert to number
- `ጽሑፍ(ቁጥር)` - Convert to string

---

## Tutorials

### Tutorial 1: Your First Program
Learn the basics of Ge-ez programming.

### Tutorial 2: Variables and Data Types
Understand how to work with different data types.

### Tutorial 3: Control Flow
Master if-else statements and loops.

### Tutorial 4: Functions
Learn to create and use functions.

### Tutorial 5: Classes and Objects
Introduction to object-oriented programming.

### Tutorial 6: File Operations
Working with files and directories.

### Tutorial 7: Error Handling
Proper error handling techniques.

### Tutorial 8: Advanced Features
Explore advanced Ge-ez features.

---

## FAQ

### General Questions

#### What is Ge-ez?
Ge-ez (ግእዝ) is the world's first complete Amharic programming language.

#### Why was Ge-ez created?
To make programming accessible to Amharic speakers and preserve the Ge-ez script.

#### Is Ge-ez free?
Yes, Ge-ez is open source and free to use.

### Technical Questions

#### What Python version is required?
Python 3.7 or higher.

#### Can I use Ge-ez with other languages?
Yes, Ge-ez can be integrated with Python applications.

#### Is there an IDE for Ge-ez?
Currently, you can use any text editor. IDE support is planned.

### Learning Questions

#### How do I learn Ge-ez?
Start with our Getting Started Guide.

#### Are there examples?
Yes, see our Examples page.

#### Can I try Ge-ez online?
Yes, use our Online Playground.

### Community Questions

#### How can I contribute?
See our Contributing Guide.

#### Where can I get help?
- GitHub Discussions
- GitHub Issues
- Community Forum

#### Can I translate documentation?
Yes! We welcome translations.

---

## License

MIT License

Copyright (c) 2024 Ge-ez (ግእዝ)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Contributors

Thank you to all contributors who have helped make Ge-ez (ግእዝ) possible!

### Core Team
- **Mightyshambel** - Creator and Lead Developer

### Contributors
- [Your name here]

### How to Add Your Name
If you've contributed to Ge-ez, please add your name to this list in your pull request.

### Recognition
All contributors are recognized for their valuable contributions to the Ge-ez project.

---

**End of Documentation**

*This document contains the complete Ge-ez (ግእዝ) programming language documentation. For the latest updates, visit our GitHub repository.*

**Made with ❤️ for the Amharic-speaking programming community**

