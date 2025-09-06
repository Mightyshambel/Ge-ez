# Ge-ez (ጌዝ) - Amharic Programming Language

A programming language that allows you to write code using Amharic keywords and syntax, making programming more accessible to Amharic speakers.

## Features

- **Amharic Keywords**: Use familiar Amharic words for programming concepts
- **Variable Declarations**: Declare variables with `አስተዋውቅ` (declare)
- **Control Flow**: Use `ከሆነ` (if), `አለበለዚያ` (else), `በመሆኑ` (while)
- **Output**: Print with `አለ` (print)
- **Data Types**: Numbers, strings, and booleans (`እውነት`/`ሐሰት`)
- **Operators**: Arithmetic (`+`, `-`, `*`, `/`) and logical (`እና`, `ወይም`, `አይደለም`)

## Amharic Keywords

| Amharic | English | Meaning |
|---------|---------|---------|
| አስተዋውቅ | VAR | declare/let |
| ከሆነ | IF | if |
| አለበለዚያ | ELSE | else |
| በመሆኑ | WHILE | while |
| አለ | PRINT | print |
| እውነት | TRUE | true |
| ሐሰት | FALSE | false |
| እና | AND | and |
| ወይም | OR | or |
| አይደለም | NOT | not |
| ውጣ | EXIT | exit |

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Interactive Mode
```bash
python main.py -i
```

### Run Amharic Program Files
```bash
python main.py examples/hello.geez
```

### Command Line Interface
```bash
python -m geez.cli examples/hello.geez
```

## Example Programs

### Hello World
```amharic
አስተዋውቅ ስም = "ጌዝ"
አለ "ሰላም! ስሜ " + ስም + " ነው።"
```

### Math Operations
```amharic
አስተዋውቅ ሀ = 10
አስተዋውቅ ለ = 5
አለ "ሀ + ለ = " + (ሀ + ለ)
```

### Conditional Statements
```amharic
አስተዋውቅ አድሜ = 25
ከሆነ አድሜ > 18 {
    አለ "አዋቂ ነኝ!"
} አለበለዚያ {
    አለ "ልጅ ነኝ!"
}
```

### Loops
```amharic
አስተዋውቅ ቆጠራ = 1
በመሆኑ ቆጠራ <= 5 {
    አለ "ቆጠራ: " + ቆጠራ
    ቆጠራ = ቆጠራ + 1
}
```

## Project Structure

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
│   └── loop.geez        # Loop example
├── main.py              # Main entry point
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Development

This is an educational project demonstrating how to build a programming language interpreter in Python. The language supports:

- Lexical analysis (tokenization)
- Syntax parsing (AST generation)
- Expression evaluation
- Variable management
- Control flow statements

## Contributing

Feel free to contribute by:
- Adding more Amharic keywords
- Implementing additional language features
- Creating more example programs
- Improving error messages in Amharic

## License

This project is for educational purposes. Feel free to use and modify as needed.
