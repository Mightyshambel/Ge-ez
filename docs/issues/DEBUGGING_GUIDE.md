# Technical Debugging Guide - ግእዝ (Ge-ez)

## 🔍 Debugging Methodology

### 1. Token Analysis
When encountering parsing errors, first analyze the tokens:

```python
#!/usr/bin/env python3
from geez.lexer import GeEzLexer

lexer = GeEzLexer()
code = "your_problematic_code_here"
tokens = lexer.tokenize(code)

print("Tokens:")
for i, token in enumerate(tokens):
    print(f"{i}: {token.type} = '{token.value}' (line {token.line}, col {token.column})")
```

### 2. Pattern Matching Debug
Test which pattern matches a specific string:

```python
#!/usr/bin/env python3
import re
from geez.lexer import GeEzLexer

lexer = GeEzLexer()
patterns = [(name, re.compile(pattern)) for name, pattern in lexer.TOKEN_PATTERNS]

text = "problematic_string"
position = 0

print("Testing which pattern matches:")
for token_type, pattern in patterns:
    match = pattern.match(text, position)
    if match:
        print(f"Pattern '{token_type}' matches: '{match.group(0)}'")
        break
```

### 3. AST Analysis
Debug parser output:

```python
#!/usr/bin/env python3
from geez.lexer import GeEzLexer
from geez.parser import GeEzParser

lexer = GeEzLexer()
parser = GeEzParser(lexer.tokenize("your_code_here"))
ast = parser.parse()

print("AST:")
print(ast)
```

## 🚨 Common Error Patterns

### "Expected token" Errors
**Cause**: Parser expects different token than what lexer provides
**Debug Steps**:
1. Check token output
2. Verify token pattern order
3. Check keyword vs identifier logic

### "Unknown character" Errors
**Cause**: Lexer doesn't have pattern for character
**Debug Steps**:
1. Add missing token pattern
2. Update lexer logic

### Type Errors
**Cause**: Interpreter type mismatch
**Debug Steps**:
1. Check operand types
2. Add type conversion logic

## 🔧 Quick Fixes

### Token Pattern Order
```python
# WRONG - single char before multi-char
TOKEN_PATTERNS = [
    ('ASSIGN', r'='),      # This matches first
    ('EQUAL', r'=='),      # This never matches
]

# CORRECT - multi-char before single-char
TOKEN_PATTERNS = [
    ('EQUAL', r'=='),      # This matches first
    ('ASSIGN', r'='),      # This matches if == doesn't
]
```

### Keyword vs Identifier
```python
# In parser, accept both keyword and identifier tokens
identifier = self.consume('IDENTIFIER', 'AMHARIC_ID', 'FOR', 'Expected identifier').value
```

### Mixed Character Identifiers
```python
# Support mixed Amharic-English identifiers
('AMHARIC_ID', r'[\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2F][\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2Fa-zA-Z0-9_]*')
```

## 📋 Testing Checklist

### Before Committing Changes
- [ ] Test with simple examples
- [ ] Test with complex examples
- [ ] Test both file and interactive modes
- [ ] Test edge cases
- [ ] Verify error messages are helpful
- [ ] Check token output for new features

### For New Features
- [ ] Add lexer patterns
- [ ] Add parser logic
- [ ] Add interpreter logic
- [ ] Add examples
- [ ] Update documentation
- [ ] Test thoroughly

## 🎯 Performance Considerations

### Token Pattern Optimization
- Order patterns by frequency (most common first)
- Use specific patterns before general ones
- Avoid overlapping patterns

### Parser Optimization
- Use lookahead efficiently
- Minimize backtracking
- Cache frequently used tokens

## 🔍 Debugging Tools

### Built-in Debugging
```python
# Enable debug mode in lexer
lexer = GeEzLexer(debug=True)

# Enable debug mode in parser
parser = GeEzParser(tokens, debug=True)
```

### Custom Debug Scripts
Create small test files to isolate issues:
```amharic
# test_simple.geez
አስተዋውቅ ሀ = 5
ማተም ሀ
```

### Interactive Testing
```bash
# Test in interactive mode
python main.py -i
# Then type commands one by one
```

## 📚 Reference Materials

### Unicode Ranges for Amharic
- `\u1200-\u137F`: Ethiopic
- `\u1380-\u139F`: Ethiopic Extended
- `\u2D80-\u2DDF`: Ethiopic Extended-A
- `\uAB00-\uAB2F`: Ethiopic Extended-B

### Common Token Types
- `VAR`: Variable declaration
- `AMHARIC_ID`: Amharic identifier
- `IDENTIFIER`: English identifier
- `NUMBER`: Numeric literal
- `STRING`: String literal
- `EQUAL`: Equality operator
- `ASSIGN`: Assignment operator

## 🚀 Best Practices

1. **Start Simple**: Begin with basic examples
2. **Test Incrementally**: Add one feature at a time
3. **Use Debug Scripts**: Create small test files
4. **Check Token Output**: Always verify tokenization
5. **Handle Edge Cases**: Test with unusual inputs
6. **Provide Clear Errors**: Make error messages helpful
7. **Document Changes**: Update documentation with new features

---

*This guide helps developers debug issues efficiently and avoid common pitfalls.*
