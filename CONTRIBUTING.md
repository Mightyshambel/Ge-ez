# Contributing to Ge-ez (ግእዝ)

Thank you for your interest in contributing to Ge-ez! We welcome contributions from the community to help make this the best Amharic programming language possible.

## 🤝 How to Contribute

### Types of Contributions

- **Bug Reports** - Report issues you find
- **Feature Requests** - Suggest new features
- **Code Contributions** - Submit code improvements
- **Documentation** - Improve documentation
- **Examples** - Add example programs
- **Testing** - Add or improve tests
- **Translation** - Help with Amharic translations

## 🚀 Getting Started

### 1. Fork the Repository
1. Go to [Ge-ez on GitHub](https://github.com/Mightyshambel/Ge-ez)
2. Click the "Fork" button
3. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Ge-ez.git
   cd Ge-ez
   ```

### 2. Set Up Development Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/your-bugfix-name
```

## 📝 Development Guidelines

### Code Style

We use the following tools to maintain code quality:

- **Black** - Code formatting
- **isort** - Import sorting
- **flake8** - Linting
- **mypy** - Type checking

Run these before committing:
```bash
black .
isort .
flake8 geez/ tests/
mypy geez/
```

### Commit Messages

Use clear, descriptive commit messages:

```bash
# Good
git commit -m "Add support for inheritance in classes"
git commit -m "Fix method call parsing issue"
git commit -m "Update documentation for new features"

# Avoid
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

### Testing

Write tests for new features and bug fixes:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=geez --cov-report=html

# Run specific test
pytest tests/test_parser.py::test_class_parsing
```

## 🐛 Reporting Bugs

### Before Reporting
1. Check if the issue already exists
2. Try the latest version
3. Check the documentation

### Bug Report Template
```markdown
**Bug Description**
A clear description of the bug.

**Steps to Reproduce**
1. Create file with content: `...`
2. Run command: `geez file.geez`
3. See error: `...`

**Expected Behavior**
What should happen instead.

**Environment**
- OS: [e.g., Windows 10, macOS 12, Ubuntu 20.04]
- Python version: [e.g., 3.9.7]
- Ge-ez version: [e.g., 1.0.0]

**Additional Context**
Any other relevant information.
```

## 💡 Suggesting Features

### Feature Request Template
```markdown
**Feature Description**
A clear description of the feature.

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should this feature work?

**Alternatives**
Other solutions you've considered.

**Additional Context**
Any other relevant information.
```

## 🔧 Code Contributions

### Areas That Need Help

1. **Language Features**
   - Inheritance support
   - Module system
   - Advanced data structures
   - More built-in functions

2. **Performance**
   - Optimize interpreter
   - Memory management
   - Caching improvements

3. **Documentation**
   - API documentation
   - Tutorials
   - Examples

4. **Testing**
   - Unit tests
   - Integration tests
   - Performance tests

### Pull Request Process

1. **Create your branch** from `main`
2. **Make your changes** following the guidelines
3. **Add tests** for new functionality
4. **Update documentation** if needed
5. **Run tests** and ensure they pass
6. **Submit pull request** with clear description

### Pull Request Template
```markdown
**Description**
Brief description of changes.

**Type of Change**
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

**Testing**
- [ ] Tests pass
- [ ] New tests added
- [ ] Manual testing completed

**Documentation**
- [ ] Documentation updated
- [ ] Examples added/updated
- [ ] README updated

**Additional Notes**
Any additional information.
```

## 🌍 Amharic Language Guidelines

### Amharic Keywords
When adding new keywords, follow these guidelines:

1. **Use proper Amharic** - Consult native speakers
2. **Be consistent** - Follow existing patterns
3. **Be descriptive** - Choose clear, meaningful words
4. **Document** - Explain the choice in comments

### Error Messages
Error messages should be:
- **Clear** - Easy to understand
- **Helpful** - Provide suggestions
- **Consistent** - Follow the same format
- **In Amharic** - Use proper Amharic

## 📚 Documentation Contributions

### Types of Documentation
- **API Documentation** - Function and class references
- **Tutorials** - Step-by-step guides
- **Examples** - Code samples
- **Language Reference** - Complete syntax guide

### Documentation Style
- **Clear and concise**
- **Include examples**
- **Use proper Amharic**
- **Follow markdown best practices**

## 🧪 Testing Guidelines

### Test Structure
```python
def test_feature_name():
    """Test description."""
    # Arrange
    code = "test code"
    
    # Act
    result = interpreter.interpret(code)
    
    # Assert
    assert result == expected
```

### Test Categories
- **Unit Tests** - Individual components
- **Integration Tests** - Component interactions
- **End-to-End Tests** - Complete workflows
- **Performance Tests** - Speed and memory usage

## 🎯 Example Contributions

### Adding a New Built-in Function
1. Add keyword to lexer
2. Add parsing logic
3. Add execution logic
4. Add tests
5. Update documentation

### Adding a New Language Feature
1. Design the syntax
2. Add lexer tokens
3. Add parser rules
4. Add interpreter logic
5. Add comprehensive tests
6. Update documentation

## 📋 Code Review Process

### For Contributors
- **Respond to feedback** promptly
- **Make requested changes**
- **Ask questions** if unclear
- **Be patient** - reviews take time

### For Reviewers
- **Be constructive** in feedback
- **Explain reasoning** for suggestions
- **Be respectful** and helpful
- **Test changes** before approving

## 🏆 Recognition

Contributors will be recognized in:
- **CONTRIBUTORS.md** file
- **Release notes**
- **Documentation credits**
- **Community acknowledgments**

## 📞 Getting Help

### Communication Channels
- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - General questions and ideas
- **Pull Request Comments** - Code review discussions

### Community Guidelines
- **Be respectful** and inclusive
- **Help others** learn and grow
- **Share knowledge** and experience
- **Follow the code of conduct**

## 📄 License

By contributing to Ge-ez, you agree that your contributions will be licensed under the same MIT License that covers the project.

## 🙏 Thank You

Thank you for contributing to Ge-ez! Your efforts help make Amharic programming accessible to everyone.

---

**Together, we're building the future of Amharic programming! 🇪🇹**
