# Ge-ez (ግእዝ) - Amharic Programming Language

A programming language that allows you to write code using Amharic keywords and syntax, making programming more accessible to Amharic speakers.

## 🎯 Project Goals

This project aims to:
- Make programming more accessible to Amharic speakers
- Preserve and promote the Amharic language in technology
- Create an educational tool for learning programming concepts
- Demonstrate how to build a programming language interpreter

## 🚀 Features

- **Amharic Keywords**: Use familiar Amharic words for programming concepts
- **Variable Declarations**: Declare variables with `አስተዋውቅ` (declare)
- **Control Flow**: Use `ከሆነ` (if), `ማተምበለዚያ` (else), `በመሆኑ` (while)
- **Output**: Print with `ማተም` (print)
- **Data Types**: Numbers, strings, and booleans (`እውነት`/`ሐሰት`)
- **Operators**: Arithmetic (`+`, `-`, `*`, `/`) and logical (`እና`, `ወይም`, `አይደለም`)
- **Comments**: Support for `#` comments

## 📚 Amharic Keywords Reference

| Amharic | English | Meaning | Example |
|---------|---------|---------|---------|
| አስተዋውቅ | VAR | declare/let | `አስተዋውቅ ስም = "ግእዝ"` |
| ከሆነ | IF | if | `ከሆነ አድሜ > 18` |
| ማተምበለዚያ | ELSE | else | `ማተምበለዚያ { ማተም "ልጅ" }` |
| በመሆኑ | WHILE | while | `በመሆኑ ቆጠራ < 5` |
| ማተም | PRINT | print | `ማተም "ሰላም"` |
| እውነት | TRUE | true | `አስተዋውቅ እውነት_ነው = እውነት` |
| ሐሰት | FALSE | false | `አስተዋውቅ ሐሰት_ነው = ሐሰት` |
| እና | AND | and | `ሀ > 0 እና ሀ < 10` |
| ወይም | OR | or | `ሀ == 0 ወይም ሀ == 1` |
| አይደለም | NOT | not | `አይደለም ሐሰት` |
| ውጣ | EXIT | exit | `ውጣ` (in interactive mode) |

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Git (for cloning the repository)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Language
```bash
python main.py
```

## 📖 Usage Examples

### Hello World
```amharic
# አማርኛ ፕሮግራም - ሰላም ዓለም
አስተዋውቅ ስም = "ግእዝ"
ማተም "ሰላም! ስሜ " + ስም + " ነው።"
```

### Math Operations
```amharic
# ሒሳብ ምሳሌ
አስተዋውቅ ሀ = 10
አስተዋውቅ ለ = 5
ማተም "ሀ + ለ = " + (ሀ + ለ)
ማተም "ሀ - ለ = " + (ሀ - ለ)
ማተም "ሀ * ለ = " + (ሀ * ለ)
ማተም "ሀ / ለ = " + (ሀ / ለ)
```

### Conditional Statements
```amharic
# ሁኔታዊ መግለጫዎች
አስተዋውቅ አድሜ = 25
ከሆነ አድሜ > 18 {
    ማተም "አዋቂ ነኝ!"
} ማተምበለዚያ {
    ማተም "ልጅ ነኝ!"
}
```

### Loops
```amharic
# ሉፕ ምሳሌ
አስተዋውቅ ቆጠራ = 1
በመሆኑ ቆጠራ <= 5 {
    ማተም "ቆጠራ: " + ቆጠራ
    ቆጠራ = ቆጠራ + 1
}
```

## 🎮 Interactive Mode

Run the language in interactive mode for experimentation:

```bash
python main.py -i
```

Example session:
```
Ge-ez Interactive Mode (ተገልጋይ ሁነት)
Type 'ውጣ' to exit
ግእዝ> ማተም "ሰላም አማርኛ!"
ሰላም አማርኛ!
ግእዝ> አስተዋውቅ ቁጥር = 42
ግእዝ> ማተም ቁጥር
42
ግእዝ> ውጣ
```

## 🏗️ Project Architecture

```
Ge-ez/
├── geez/                 # Main package
│   ├── __init__.py      # Package initialization
│   ├── lexer.py         # Tokenizer for Amharic syntax
│   ├── parser.py        # Parser for AST generation
│   ├── interpreter.py   # AST interpreter
│   └── cli.py           # Command-line interface
├── examples/            # Example Amharic programs
│   ├── hello.geez       # Hello world example
│   ├── math.geez        # Math operations example
│   ├── loop.geez        # Loop example
│   └── simple.geez      # Simple variable example
├── main.py              # Main entry point
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Development

### Running Tests
```bash
# Run example programs
python main.py examples/hello.geez
python main.py examples/math.geez
python main.py examples/loop.geez
```

### Adding New Features
1. **New Keywords**: Add to `KEYWORDS` in `geez/lexer.py`
2. **New Operators**: Add patterns to `TOKEN_PATTERNS` in `geez/lexer.py`
3. **New Statements**: Extend parser in `geez/parser.py`
4. **New Execution**: Add to interpreter in `geez/interpreter.py`

### Code Structure
- **Lexer**: Converts Amharic text into tokens
- **Parser**: Builds Abstract Syntax Tree (AST) from tokens
- **Interpreter**: Executes the AST and manages variables

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Areas for Contribution
- Add more Amharic keywords
- Implement additional language features (functions, arrays, etc.)
- Improve error messages in Amharic
- Create more example programs
- Add unit tests
- Improve documentation
- Add syntax highlighting for editors

## 📝 Language Specification

### Data Types
- **Numbers**: `42`, `3.14`
- **Strings**: `"ሰላም"`, `"Hello"`
- **Booleans**: `እውነት`, `ሐሰት`

### Operators
- **Arithmetic**: `+`, `-`, `*`, `/`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `እና`, `ወይም`, `አይደለም`

### Statements
- **Variable Declaration**: `አስተዋውቅ identifier = expression`
- **Print**: `ማተም expression`
- **Conditional**: `ከሆነ condition { statements } ማተምበለዚያ { statements }`
- **Loop**: `በመሆኑ condition { statements }`

## 🐛 Known Issues

- Interactive mode has some input handling issues
- Limited error messages in Amharic
- No support for functions yet
- No array/list data type

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🙏 Acknowledgments

- Inspired by the beauty and richness of the Amharic language
- Built with Python's simplicity and power
- Thanks to the open-source community for inspiration

## 📞 Contact

- **GitHub**: [@Mightyshambel](https://github.com/Mightyshambel)
- **Repository**: [https://github.com/Mightyshambel/Ge-ez](https://github.com/Mightyshambel/Ge-ez)

---

**Made by Mighty Shambel for the Amharic-speaking community**