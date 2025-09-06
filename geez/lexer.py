"""
Ge-ez Lexer (Tokenizer)
Handles lexical analysis for Amharic programming language
"""

import re
from typing import List, Tuple, Optional


class Token:
    """Represents a token in the Amharic language"""
    
    def __init__(self, type_: str, value: str, line: int = 1, column: int = 1):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"


class GeEzLexer:
    """Lexical analyzer for Ge-ez Amharic programming language"""
    
    # Amharic keywords and their English equivalents
    KEYWORDS = {
        'አስተዋውቅ': 'VAR',      # declare/let
        'ከሆነ': 'IF',           # if
        'አለበለዚያ': 'ELSE',      # else
        'ለ': 'FOR',             # for
        'በመሆኑ': 'WHILE',       # while
        'ተመለስ': 'RETURN',      # return
        'ተግባር': 'FUNCTION',    # function
        'እውነት': 'TRUE',        # true
        'ሐሰት': 'FALSE',        # false
        'ማተም': 'PRINT',         # print
        'እና': 'AND',           # and
        'ወይም': 'OR',           # or
        'አይደለም': 'NOT',       # not
        'ውጣ': 'EXIT',          # exit
        'ይጠራ': 'CALL',         # call
        'በ': 'IN',              # in (for loops)
    }
    
    # Token patterns
    TOKEN_PATTERNS = [
        ('COMMENT', r'#.*'),                # Comments
        ('NUMBER', r'\d+\.?\d*'),           # Numbers
        ('STRING', r'"[^"]*"'),             # Strings
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
        ('AMHARIC_ID', r'[\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2F]+'),  # Amharic identifiers
        ('ASSIGN', r'='),                   # Assignment
        ('PLUS', r'\+'),                    # Addition
        ('MINUS', r'-'),                    # Subtraction
        ('MULTIPLY', r'\*'),                # Multiplication
        ('DIVIDE', r'/'),                   # Division
        ('LPAREN', r'\('),                  # Left parenthesis
        ('RPAREN', r'\)'),                  # Right parenthesis
        ('LBRACE', r'\{'),                  # Left brace
        ('RBRACE', r'\}'),                  # Right brace
        ('LBRACKET', r'\['),                # Left bracket (for lists)
        ('RBRACKET', r'\]'),                # Right bracket (for lists)
        ('SEMICOLON', r';'),                # Semicolon
        ('COMMA', r','),                    # Comma
        ('EQUAL', r'=='),                   # Equality
        ('NOT_EQUAL', r'!='),               # Not equal
        ('LESS', r'<'),                     # Less than
        ('GREATER', r'>'),                  # Greater than
        ('LESS_EQUAL', r'<='),              # Less or equal
        ('GREATER_EQUAL', r'>='),           # Greater or equal
        ('NEWLINE', r'\n'),                 # Newline
        ('WHITESPACE', r'\s+'),             # Whitespace
    ]
    
    def __init__(self):
        self.tokens = []
        self.current_line = 1
        self.current_column = 1
    
    def tokenize(self, text: str) -> List[Token]:
        """Tokenize the input text"""
        self.tokens = []
        self.current_line = 1
        self.current_column = 1
        
        # Compile regex patterns
        patterns = [(name, re.compile(pattern)) for name, pattern in self.TOKEN_PATTERNS]
        
        position = 0
        while position < len(text):
            matched = False
            
            for token_type, pattern in patterns:
                match = pattern.match(text, position)
                if match:
                    value = match.group(0)
                    
                    # Skip whitespace and comments but track position
                    if token_type in ('WHITESPACE', 'COMMENT'):
                        if '\n' in value:
                            self.current_line += value.count('\n')
                            self.current_column = 1
                        else:
                            self.current_column += len(value)
                        position = match.end()
                        matched = True
                        break
                    
                    # Handle newlines
                    if token_type == 'NEWLINE':
                        self.current_line += 1
                        self.current_column = 1
                        position = match.end()
                        matched = True
                        break
                    
                    # Check if it's an Amharic keyword
                    if token_type == 'AMHARIC_ID' and value in self.KEYWORDS:
                        token_type = self.KEYWORDS[value]
                    
                    # Create token
                    token = Token(token_type, value, self.current_line, self.current_column)
                    self.tokens.append(token)
                    
                    # Update position
                    self.current_column += len(value)
                    position = match.end()
                    matched = True
                    break
            
            if not matched:
                # Handle unknown characters
                char = text[position]
                if char.strip():  # Only error on non-whitespace
                    raise SyntaxError(f"Unknown character '{char}' at line {self.current_line}, column {self.current_column}")
                position += 1
        
        return self.tokens
    
    def get_tokens(self) -> List[Token]:
        """Get the list of tokens"""
        return self.tokens