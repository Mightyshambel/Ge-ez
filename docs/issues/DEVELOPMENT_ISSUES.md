# ግእዝ (Ge-ez) Development Issues Documentation

This document catalogs all the major issues encountered during the development of the ግእዝ (Ge-ez) Amharic programming language, along with their solutions and lessons learned.

## Table of Contents

1. [Setup and Environment Issues](#setup-and-environment-issues)
2. [Lexer (Tokenization) Issues](#lexer-tokenization-issues)
3. [Parser (AST Generation) Issues](#parser-ast-generation-issues)
4. [Interpreter (Execution) Issues](#interpreter-execution-issues)
5. [CLI and Interactive Mode Issues](#cli-and-interactive-mode-issues)
6. [Git and Version Control Issues](#git-and-version-control-issues)
7. [Documentation and Image Issues](#documentation-and-image-issues)
8. [Language Design Issues](#language-design-issues)

---

## Setup and Environment Issues

### Issue #1: Python Command Not Found
**Problem**: `zsh: command not found: python`
**Root Cause**: macOS uses `python3` instead of `python`
**Solution**: Use `python3 -m venv .venv` instead of `python -m venv .venv`
**Lesson**: Always check Python installation and use appropriate command for the system

### Issue #2: Virtual Environment Directory Confusion
**Problem**: `cd: no such file or directory: venv`
**Root Cause**: User tried to `cd venv` but the directory is `.venv` (hidden)
**Solution**: Use `cd .venv` or `source .venv/bin/activate`
**Lesson**: Hidden directories start with `.` and need to be explicitly referenced

### Issue #3: Missing Module Errors
**Problem**: `ModuleNotFoundError: No module named 'geez.parser'`
**Root Cause**: Files were missing from the `geez/` package
**Solution**: Created missing files (`geez/lexer.py`, `geez/parser.py`, `geez/interpreter.py`, `geez/cli.py`)
**Lesson**: Ensure all package files exist before importing

---

## Lexer (Tokenization) Issues

### Issue #4: Comments Not Supported
**Problem**: `ስህተት: Unknown character '#' at line 1, column 1`
**Root Cause**: Lexer didn't have a pattern for comments
**Solution**: Added `('COMMENT', r'#.*')` to `TOKEN_PATTERNS` and skip logic
**Lesson**: Always include comment support in programming languages

### Issue #5: Token Precedence Issues
**Problem**: `==` was tokenized as two `=` tokens instead of `EQUAL`
**Root Cause**: `ASSIGN` pattern was defined before `EQUAL` pattern
**Solution**: Reordered `TOKEN_PATTERNS` to put multi-character operators before single-character ones
**Lesson**: Token pattern order matters - longer patterns must come first

### Issue #6: Amharic Identifier Pattern Limitations
**Problem**: `እኩል_ነው` was tokenized as separate tokens: `እኩል`, `_`, `ነው`
**Root Cause**: `AMHARIC_ID` pattern only supported Amharic characters, not mixed identifiers
**Solution**: Updated pattern to `r'[\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2F][\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2Fa-zA-Z0-9_]*'`
**Lesson**: Programming languages need to support mixed character sets in identifiers

### Issue #7: Keyword vs Identifier Conflict
**Problem**: `ለ` (FOR keyword) couldn't be used as variable name
**Root Cause**: Lexer converted `ለ` to `FOR` token, but parser only accepted `AMHARIC_ID` for variables
**Solution**: Updated parser to accept `FOR` token as identifier in variable declarations
**Lesson**: Keywords should be context-sensitive when possible

---

## Parser (AST Generation) Issues

### Issue #8: Method Signature Mismatch
**Problem**: `consume() takes 3 positional arguments but 4 were given`
**Root Cause**: `consume` method signature didn't match usage
**Solution**: Modified `consume` method to accept `*token_types` and `message` as keyword argument
**Lesson**: Method signatures must match their usage patterns

### Issue #9: Function Call vs Assignment Confusion
**Problem**: Function calls were being parsed as assignments
**Root Cause**: Parser couldn't distinguish between `name = value` and `name(args)`
**Solution**: Added check for `LPAREN` token to identify function calls
**Lesson**: Parsers need context to disambiguate similar syntax patterns

### Issue #10: For Loop Keyword Consumption
**Problem**: `በ` keyword in for loops wasn't being consumed properly
**Root Cause**: Parser expected `IN` token but lexer provided `AMHARIC_ID`
**Solution**: Added explicit consumption of `IN` token in `parse_for_statement`
**Lesson**: Keyword mapping between lexer and parser must be consistent

---

## Interpreter (Execution) Issues

### Issue #11: String Concatenation Type Error
**Problem**: `can only concatenate str (not "float") to str`
**Root Cause**: Binary `+` operation didn't handle type conversion
**Solution**: Added explicit string conversion in `execute_binary_op` for `+` operator
**Lesson**: Dynamic languages need implicit type conversion for common operations

### Issue #12: Multi-Statement Parsing in Interactive Mode
**Problem**: Multiple statements failed in interactive mode with "Expected token" errors
**Root Cause**: Interactive mode parsed each line independently, but parser expected multiple statements
**Solution**: Modified CLI to accumulate statements and execute them together with `አፈጣጠር` command
**Lesson**: Interactive mode needs different parsing strategy than file mode

---

## CLI and Interactive Mode Issues

### Issue #13: File Path Confusion
**Problem**: `ፋይል አልተገኘም: name.geez`
**Root Cause**: User tried to run file from wrong directory
**Solution**: Explained correct path `examples/name.geez`
**Lesson**: Clear error messages should include helpful path information

### Issue #14: Interactive Mode Statement Handling
**Problem**: Interactive mode couldn't handle multiple statements
**Root Cause**: Each line was parsed as separate program
**Solution**: Implemented statement accumulation with execution trigger
**Lesson**: Interactive mode requires different UX than file execution

---

## Git and Version Control Issues

### Issue #15: Git Reset on Initial Commit
**Problem**: `fatal: ambiguous argument 'HEAD~1': unknown revision or path not in the working tree`
**Root Cause**: Tried to reset on first commit
**Solution**: Used `git reset --soft HEAD~1` to prepare for incremental commits
**Lesson**: Git history manipulation requires understanding of commit structure

### Issue #16: Commit Strategy
**Problem**: User wanted incremental commits instead of bulk commits
**Root Cause**: Assistant was committing all changes at once
**Solution**: Implemented step-by-step commit strategy with proper documentation
**Lesson**: Follow user preferences for commit granularity

---

## Documentation and Image Issues

### Issue #17: README Table Formatting
**Problem**: Search/replace failed due to formatting issues in README table
**Root Cause**: Table had malformed content (`ማተምበለዚያ` instead of `አለበለዚያ`)
**Solution**: Read file content, fixed table, then applied changes
**Lesson**: Always verify file content before making changes

### Issue #18: Image Upload and Resolution
**Problem**: Low-resolution image (529x705) in README
**Root Cause**: User uploaded low-res image
**Solution**: Found higher-res PDF, converted to PNG (1191x1685), updated README
**Lesson**: Image quality matters for documentation

### Issue #19: Broken Image Links
**Problem**: Image showed as broken link in README
**Root Cause**: Empty placeholder file (0 bytes)
**Solution**: Replaced with actual high-resolution image
**Lesson**: Placeholder files should be clearly marked as such

---

## Language Design Issues

### Issue #20: Amharic Spelling Correction
**Problem**: User corrected spelling from "Ge-ez" to "ግእዝ"
**Root Cause**: Initial spelling was incorrect
**Solution**: Updated all references throughout codebase
**Lesson**: Get native speaker input for language-specific content

### Issue #21: Keyword Selection
**Problem**: User corrected `አይተ` to `ግብአት` for input function
**Root Cause**: Initial keyword choice wasn't appropriate
**Solution**: Updated lexer, parser, interpreter, and documentation
**Lesson**: Keyword selection should be culturally appropriate

### Issue #22: Print Keyword Change
**Problem**: User changed print keyword from `አለ` to `ማተም`
**Root Cause**: Initial choice wasn't the best Amharic word
**Solution**: Updated throughout codebase
**Lesson**: Function names should be intuitive in the target language

---

## Summary of Lessons Learned

1. **Token Pattern Order**: Multi-character patterns must come before single-character patterns
2. **Context-Sensitive Parsing**: Keywords should be context-sensitive when possible
3. **Mixed Character Sets**: Programming languages need to support mixed character sets
4. **Interactive vs File Mode**: Different parsing strategies needed for different execution modes
5. **Type Conversion**: Dynamic languages need implicit type conversion for common operations
6. **Native Speaker Input**: Always get native speaker input for language-specific content
7. **Incremental Development**: Build and test features incrementally
8. **Error Messages**: Provide clear, helpful error messages
9. **Documentation Quality**: High-quality documentation requires attention to detail
10. **Git Workflow**: Follow user preferences for commit strategy

---

## Tools and Techniques Used

- **Debugging**: Created small test files to isolate issues
- **Token Analysis**: Used debug scripts to examine tokenization
- **Pattern Matching**: Analyzed regex patterns for correctness
- **Incremental Testing**: Built and tested features step by step
- **User Feedback**: Incorporated user corrections and preferences
- **Documentation**: Maintained comprehensive documentation throughout

---

*This document serves as a reference for future development and helps other developers understand the challenges faced in creating a programming language with non-Latin scripts.*
