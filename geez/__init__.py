# Ge-ez: Amharic Programming Language

This is the main package for the Ge-ez Amharic programming language interpreter.

## Features
- Amharic keywords for programming concepts
- Variable declarations with `አስተዋውቅ`
- Control flow with `ከሆነ`, `አለበለዚያ`, `በመሆኑ`
- Output with `አለ`
- Support for numbers, strings, and booleans
- Arithmetic and logical operators

## Usage
```python
from geez.interpreter import GeEzInterpreter

interpreter = GeEzInterpreter()
result = interpreter.interpret('አለ "ሰላም አማርኛ!"')
```