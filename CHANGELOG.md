# Changelog

All notable changes to the Ge-ez Amharic Programming Language project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Function definitions and calls
- Array/list data types
- File I/O operations
- Syntax highlighting support
- IDE integration

### Changed
- Improved error messages in Amharic
- Better performance optimizations

## [0.1.0] - 2025-01-27

### Added
- **Core Language Features**
  - Amharic keyword support (`አስተዋውቅ`, `ከሆነ`, `አለበለዚያ`, `በመሆኑ`, `አለ`)
  - Variable declarations and assignments
  - Print statements
  - Conditional statements (if/else)
  - While loops
  - Boolean values (`እውነት`, `ሐሰት`)
  - Logical operators (`እና`, `ወይም`, `አይደለም`)

- **Data Types**
  - Numbers (integers and floats)
  - Strings with Unicode support
  - Booleans

- **Operators**
  - Arithmetic: `+`, `-`, `*`, `/`
  - Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Logical: `እና`, `ወይም`, `አይደለም`

- **Language Components**
  - Lexical analyzer (tokenizer) with Amharic Unicode support
  - Parser with Abstract Syntax Tree (AST) generation
  - Interpreter with variable management
  - Command-line interface

- **User Interface**
  - Interactive mode with Amharic prompt (`ግእዝ>`)
  - File execution mode
  - Help system

- **Documentation**
  - Comprehensive README with examples
  - Complete API documentation
  - Installation guide for all platforms
  - Amharic keywords reference table
  - Code examples and tutorials

- **Example Programs**
  - Hello world program (`examples/hello.geez`)
  - Math operations (`examples/math.geez`)
  - Loop demonstration (`examples/loop.geez`)
  - Simple variable example (`examples/simple.geez`)

- **Project Structure**
  - Modular package design (`geez/` package)
  - Proper Python package structure
  - Git repository with clean history
  - GitHub repository setup

### Technical Details
- **Lexer**: Handles Amharic Unicode ranges (U+1200-U+137F, U+1380-U+139F, U+2D80-U+2DDF, U+AB00-U+AB2F)
- **Parser**: Recursive descent parser with proper precedence
- **Interpreter**: Tree-walking interpreter with variable scope
- **CLI**: Argument parsing with interactive and file modes

### Supported Platforms
- Windows (Command Prompt, PowerShell)
- macOS (Terminal)
- Linux (Ubuntu, Debian, and other distributions)

### Dependencies
- Python 3.7+
- No external dependencies (pure Python implementation)

## [0.0.1] - 2025-01-27

### Added
- Initial project setup
- Basic project structure
- Git repository initialization
- GitHub repository creation

---

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

## Release Process

1. Update version numbers in relevant files
2. Update this changelog
3. Create a git tag for the version
4. Push changes to GitHub
5. Create a GitHub release with release notes

## Contributing

When contributing to this project, please:

1. Update this changelog with your changes
2. Follow the existing format
3. Group changes by type (Added, Changed, Deprecated, Removed, Fixed, Security)
4. Use present tense ("Add feature" not "Added feature")
5. Reference issues and pull requests when applicable

## Future Roadmap

### Version 0.2.0 (Planned)
- Function definitions and calls
- Local variable scoping
- Return statements
- Better error handling

### Version 0.3.0 (Planned)
- Array/list data types
- String manipulation functions
- File I/O operations
- Import system

### Version 0.4.0 (Planned)
- Object-oriented programming features
- Classes and methods
- Inheritance
- Polymorphism

### Version 1.0.0 (Planned)
- Complete language specification
- Comprehensive test suite
- Performance optimizations
- Package distribution
- IDE support and syntax highlighting
