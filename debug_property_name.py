#!/usr/bin/env python3
from geez.lexer import GeEzLexer
from geez.parser import GeEzParser

code = '''
ሰው_1.ማተም_መረጃ()
'''

lexer = GeEzLexer()
tokens = lexer.tokenize(code)

print("Tokens:")
for i, token in enumerate(tokens):
    print(f"{i}: {token.type}: {token.value}")

print("\nParsing step by step:")
parser = GeEzParser(tokens)

# Debug the parsing step by step
print(f"Current token: {parser.peek()}")
print(f"Current position: {parser.current}")

# Parse atom
atom = parser.parse_atom()
print(f"Atom parsed: {atom}")
print(f"Current token after atom: {parser.peek()}")
print(f"Current position after atom: {parser.current}")

# Check if DOT matches
print(f"Match DOT: {parser.match('DOT')}")
print(f"Current token after DOT match: {parser.peek()}")
print(f"Current position after DOT match: {parser.current}")

# Try to consume property name
try:
    property_name = parser.consume('IDENTIFIER', 'AMHARIC_ID', message='Expected property name').value
    print(f"Property name consumed: {property_name}")
    print(f"Current token after property name: {parser.peek()}")
    print(f"Current position after property name: {parser.current}")
except Exception as e:
    print(f"Error consuming property name: {e}")
    print(f"Current token: {parser.peek()}")
    print(f"Current position: {parser.current}")
