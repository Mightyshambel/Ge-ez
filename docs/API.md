# Ge-ez API Documentation

This document provides detailed API documentation for the Ge-ez Amharic Programming Language.

## Table of Contents
1. [Lexer API](#lexer-api)
2. [Parser API](#parser-api)
3. [Interpreter API](#interpreter-api)
4. [CLI API](#cli-api)
5. [AST Nodes](#ast-nodes)

## Lexer API

### `GeEzLexer`

The lexical analyzer that converts Amharic text into tokens.

#### Methods

##### `__init__(self)`
Initialize the lexer.

##### `tokenize(self, text: str) -> List[Token]`
Convert input text into a list of tokens.

**Parameters:**
- `text` (str): The Amharic code to tokenize

**Returns:**
- `List[Token]`: List of tokens representing the input

**Example:**
```python
from geez.lexer import GeEzLexer

lexer = GeEzLexer()
tokens = lexer.tokenize('አለ "ሰላም"')
```

##### `get_tokens(self) -> List[Token]`
Get the current list of tokens.

**Returns:**
- `List[Token]`: Current tokens

#### Token Class

##### `Token(type_: str, value: str, line: int = 1, column: int = 1)`
Represents a single token in the language.

**Parameters:**
- `type_` (str): Token type (e.g., 'VAR', 'STRING', 'NUMBER')
- `value` (str): The actual token value
- `line` (int): Line number where token appears
- `column` (int): Column number where token appears

#### Supported Keywords

| Amharic | Token Type | Description |
|---------|------------|-------------|
| አስተዋውቅ | VAR | Variable declaration |
| ከሆነ | IF | Conditional statement |
| አለበለዚያ | ELSE | Else clause |
| በመሆኑ | WHILE | While loop |
| አለ | PRINT | Print statement |
| እውነት | TRUE | Boolean true |
| ሐሰት | FALSE | Boolean false |
| እና | AND | Logical AND |
| ወይም | OR | Logical OR |
| አይደለም | NOT | Logical NOT |
| ውጣ | EXIT | Exit command |

## Parser API

### `GeEzParser`

The parser that builds an Abstract Syntax Tree (AST) from tokens.

#### Methods

##### `__init__(self, tokens: List[Token])`
Initialize the parser with a list of tokens.

**Parameters:**
- `tokens` (List[Token]): List of tokens to parse

##### `parse(self) -> List[ASTNode]`
Parse tokens into an Abstract Syntax Tree.

**Returns:**
- `List[ASTNode]`: List of AST nodes representing the program

**Example:**
```python
from geez.lexer import GeEzLexer
from geez.parser import GeEzParser

lexer = GeEzLexer()
tokens = lexer.tokenize('አለ "ሰላም"')
parser = GeEzParser(tokens)
ast = parser.parse()
```

## Interpreter API

### `GeEzInterpreter`

The interpreter that executes AST nodes.

#### Methods

##### `__init__(self)`
Initialize the interpreter with empty variable storage.

##### `interpret(self, code: str) -> Any`
Interpret Ge-ez code directly.

**Parameters:**
- `code` (str): The Amharic code to interpret

**Returns:**
- `Any`: The result of the last expression (if any)

**Example:**
```python
from geez.interpreter import GeEzInterpreter

interpreter = GeEzInterpreter()
result = interpreter.interpret('አለ "ሰላም አማርኛ!"')
```

##### `execute(self, node: ASTNode) -> Any`
Execute a single AST node.

**Parameters:**
- `node` (ASTNode): The AST node to execute

**Returns:**
- `Any`: The result of executing the node

##### `get_variable(self, name: str) -> Any`
Get the value of a variable.

**Parameters:**
- `name` (str): Variable name

**Returns:**
- `Any`: Variable value

**Raises:**
- `RuntimeError`: If variable is not defined

##### `set_variable(self, name: str, value: Any) -> None`
Set a variable value.

**Parameters:**
- `name` (str): Variable name
- `value` (Any): Variable value

##### `clear_variables(self) -> None`
Clear all variables from memory.

## CLI API

### Command Line Interface

The CLI provides a command-line interface for running Amharic programs.

#### Usage

```bash
python main.py [options] [file]
```

#### Options

- `-i, --interactive`: Start interactive mode
- `-h, --help`: Show help message

#### Examples

```bash
# Run a file
python main.py examples/hello.geez

# Interactive mode
python main.py -i

# Help
python main.py -h
```

#### Interactive Mode Commands

- `ውጣ`: Exit interactive mode
- Any valid Ge-ez expression or statement

## AST Nodes

### Base Classes

#### `ASTNode`
Base class for all AST nodes.

### Expression Nodes

#### `NumberNode(value: float)`
Represents a numeric literal.

**Attributes:**
- `value` (float): The numeric value

#### `StringNode(value: str)`
Represents a string literal.

**Attributes:**
- `value` (str): The string value

#### `BooleanNode(value: bool)`
Represents a boolean literal.

**Attributes:**
- `value` (bool): The boolean value

#### `IdentifierNode(name: str)`
Represents a variable reference.

**Attributes:**
- `name` (str): The variable name

#### `BinaryOpNode(left: ASTNode, operator: str, right: ASTNode)`
Represents a binary operation.

**Attributes:**
- `left` (ASTNode): Left operand
- `operator` (str): Operator symbol
- `right` (ASTNode): Right operand

#### `UnaryOpNode(operator: str, operand: ASTNode)`
Represents a unary operation.

**Attributes:**
- `operator` (str): Operator symbol
- `operand` (ASTNode): Operand

### Statement Nodes

#### `AssignmentNode(identifier: str, value: ASTNode)`
Represents a variable assignment.

**Attributes:**
- `identifier` (str): Variable name
- `value` (ASTNode): Value to assign

#### `PrintNode(expression: ASTNode)`
Represents a print statement.

**Attributes:**
- `expression` (ASTNode): Expression to print

#### `IfNode(condition: ASTNode, then_block: List[ASTNode], else_block: Optional[List[ASTNode]])`
Represents an if statement.

**Attributes:**
- `condition` (ASTNode): Condition expression
- `then_block` (List[ASTNode]): Statements in then block
- `else_block` (Optional[List[ASTNode]]): Statements in else block

#### `WhileNode(condition: ASTNode, block: List[ASTNode])`
Represents a while loop.

**Attributes:**
- `condition` (ASTNode): Loop condition
- `block` (List[ASTNode]): Loop body statements

## Error Handling

### Common Exceptions

#### `SyntaxError`
Raised when there's a syntax error in the code.

**Common causes:**
- Unknown characters
- Unexpected tokens
- Missing expected tokens

#### `RuntimeError`
Raised when there's a runtime error during execution.

**Common causes:**
- Undefined variables
- Division by zero
- Type errors

### Error Messages

Error messages are provided in Amharic where possible:

- `ስህተት: {error}` - General error
- `ፋይል አልተገኘም: {filename}` - File not found
- `Unknown character '{char}'` - Unknown character

## Examples

### Basic Usage

```python
from geez.interpreter import GeEzInterpreter

# Create interpreter
interpreter = GeEzInterpreter()

# Simple program
code = '''
አስተዋውቅ ስም = "ግእዝ"
አለ ስም
'''

# Execute
interpreter.interpret(code)
```

### Advanced Usage

```python
from geez.lexer import GeEzLexer
from geez.parser import GeEzParser
from geez.interpreter import GeEzInterpreter

# Step-by-step execution
lexer = GeEzLexer()
parser = GeEzParser(lexer.tokenize(code))
interpreter = GeEzInterpreter()

ast = parser.parse()
for node in ast:
    interpreter.execute(node)
```

## Performance Considerations

- The interpreter is designed for educational purposes
- Not optimized for large programs
- Variables are stored in a simple dictionary
- No garbage collection for variables

## Future Enhancements

- Function definitions and calls
- Array/list data types
- File I/O operations
- Better error reporting
- Syntax highlighting support
- IDE integration
