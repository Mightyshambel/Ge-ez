# ግእዝ: Amharic Programming Language

"""
This is the main package for the ግእዝ Amharic programming language interpreter.

Features:
- Amharic keywords for programming concepts
- Variable declarations with አስተዋውቅ
- Control flow with ከሆነ, ማተምበለዚያ, በመሆኑ
- Output with ማተም
- Support for numbers, strings, and booleans
- Arithmetic and logical operators

Usage:
    from geez.interpreter import GeEzInterpreter

    interpreter = GeEzInterpreter()
    result = interpreter.interpret('ማተም "ሰላም አማርኛ!"')
"""

__version__ = "0.1.0"
__author__ = "Mighty Shambel"
__description__ = "Amharic Programming Language"

from .lexer import GeEzLexer, Token
from .parser import GeEzParser
from .interpreter import GeEzInterpreter

__all__ = ["GeEzLexer", "Token", "GeEzParser", "GeEzInterpreter"]
