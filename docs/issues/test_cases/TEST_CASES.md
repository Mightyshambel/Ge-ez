# Test Cases Used During Development

This document contains all the test cases used to debug and verify features during the development of ግእዝ (Ge-ez).

## 🔍 Token Analysis Test Cases

### Basic Tokenization
```amharic
# test_simple.geez
አስተዋውቅ ሀ = 5
ማተም ሀ
```

### Mixed Identifiers
```amharic
# test_mixed_identifiers.geez
አስተዋውቅ እኩል_ነው = ሀ == ለ
ማተም እኩል_ነው
```

### Comparison Operators
```amharic
# test_comparison.geez
አስተዋውቅ ሀ = 5
አስተዋውቅ ለ = 3
አስተዋውቅ እኩል_ነው = ሀ == ለ
ማተም እኩል_ነው
```

## 🚨 Error Reproduction Test Cases

### Token Precedence Issue
```amharic
# test_equality_debug.geez
አስተዋውቅ ሀ = 5
አስተዋውቅ ለ = 3
አስተዋውቅ እኩል_ነው = ሀ == ለ
```

### Multi-Statement Parsing
```amharic
# test_multistatement.geez
አስተዋውቅ ሀ = 5
አስተዋውቅ ለ = 3
አስተዋውቅ እኩል_ነው = ሀ == ለ
ማተም እኩል_ነው
```

### Function Call vs Assignment
```amharic
# test_function_call.geez
አስተዋውቅ ሀ = 5
ማተም ሀ
```

## ✅ Working Test Cases

### Basic Arithmetic
```amharic
# test_arithmetic.geez
አስተዋውቅ ሀ = 5
አስተዋውቅ ለ = 3
አስተዋውቅ ውጤት = ሀ + ለ
ማተም ውጤት
```

### String Operations
```amharic
# test_strings.geez
አስተዋውቅ ስም = "ግእዝ"
አስተዋውቅ መልዕክት = "ሰላም " + ስም
ማተም መልዕክት
```

### Lists and Arrays
```amharic
# test_lists.geez
አስተዋውቅ ዝርዝር = [1, 2, 3]
ማተም ዝርዝር
አስተዋውቅ ዋጋ = ዝርዝር[0]
ማተም ዋጋ
```

### Input Function
```amharic
# test_input.geez
አስተዋውቅ ስም = ግብአት("ስምህን አስገባ: ")
ማተም "ሰላም " + ስም
```

### Control Flow
```amharic
# test_control_flow.geez
አስተዋውቅ ሀ = 5
ከሆነ ሀ > 3 {
    ማተም "ሀ ከ 3 ይበልጣል"
}
```

### Functions
```amharic
# test_functions.geez
ተግባር ማባዛት(ሀ, ለ) {
    ተመለስ ሀ * ለ
}

አስተዋውቅ ውጤት = ማባዛት(5, 3)
ማተም ውጤት
```

### Loops
```amharic
# test_loops.geez
አስተዋውቅ ዝርዝር = [1, 2, 3, 4, 5]
ለ ንጥል በ ዝርዝር {
    ማተም ንጥል
}
```

## 🧪 Interactive Mode Test Cases

### Single Statement
```amharic
አስተዋውቅ ሀ = 5
```

### Multiple Statements
```amharic
አስተዋውቅ ሀ = 5
አስተዋውቅ ለ = 3
አስተዋውቅ እኩል_ነው = ሀ == ለ
ማተም እኩል_ነው
አፈጣጠር
```

## 🔧 Debug Scripts Used

### Token Debug Script
```python
#!/usr/bin/env python3
from geez.lexer import GeEzLexer

lexer = GeEzLexer()
code = "your_code_here"
tokens = lexer.tokenize(code)

print("Tokens:")
for i, token in enumerate(tokens):
    print(f"{i}: {token.type} = '{token.value}' (line {token.line}, col {token.column})")
```

### Pattern Match Debug Script
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

## 📊 Test Results Summary

### Before Fixes
- ❌ Multi-statement parsing failed
- ❌ Comparison operators failed
- ❌ Mixed identifiers failed
- ❌ Interactive mode failed

### After Fixes
- ✅ Multi-statement parsing works
- ✅ Comparison operators work
- ✅ Mixed identifiers work
- ✅ Interactive mode works
- ✅ All basic features work

## 🎯 Test Coverage

### Core Features
- [x] Variables and assignments
- [x] Arithmetic operations
- [x] String operations
- [x] Comparison operators
- [x] Control flow
- [x] Functions
- [x] Lists and arrays
- [x] Input function
- [x] Interactive mode
- [x] File execution

### Edge Cases
- [x] Mixed character identifiers
- [x] Keyword as variable name
- [x] Multi-statement parsing
- [x] Token precedence
- [x] Type conversion

---

*These test cases were instrumental in identifying and fixing issues during development.*
