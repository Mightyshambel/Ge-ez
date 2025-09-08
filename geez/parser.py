"""
Ge-ez Parser
Builds Abstract Syntax Tree (AST) from tokens
"""

from typing import List, Optional
from .lexer import Token
from .errors import AmharicErrorMessages


class ASTNode:
    """Base class for AST nodes"""

    pass


class NumberNode(ASTNode):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class StringNode(ASTNode):
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"String({self.value!r})"


class BooleanNode(ASTNode):
    def __init__(self, value: bool):
        self.value = value

    def __repr__(self):
        return f"Boolean({self.value})"


class IdentifierNode(ASTNode):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"


class ListNode(ASTNode):
    def __init__(self, elements: List[ASTNode]):
        self.elements = elements

    def __repr__(self):
        return f"List({self.elements})"


class IndexNode(ASTNode):
    def __init__(self, list_expr: ASTNode, index_expr: ASTNode):
        self.list_expr = list_expr
        self.index_expr = index_expr

    def __repr__(self):
        return f"Index({self.list_expr}[{self.index_expr}])"


class InputNode(ASTNode):
    def __init__(self, prompt: Optional[ASTNode] = None):
        self.prompt = prompt

    def __repr__(self):
        return f"Input({self.prompt})"


class BinaryOpNode(ASTNode):
    def __init__(self, left: ASTNode, operator: str, right: ASTNode):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left}, {self.operator}, {self.right})"


class UnaryOpNode(ASTNode):
    def __init__(self, operator: str, operand: ASTNode):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return f"UnaryOp({self.operator}, {self.operand})"


class AssignmentNode(ASTNode):
    def __init__(self, identifier: str, value: ASTNode):
        self.identifier = identifier
        self.value = value

    def __repr__(self):
        return f"Assignment({self.identifier}, {self.value})"


class PrintNode(ASTNode):
    def __init__(self, expression: ASTNode):
        self.expression = expression

    def __repr__(self):
        return f"Print({self.expression})"


class IfNode(ASTNode):
    def __init__(
        self,
        condition: ASTNode,
        then_block: List[ASTNode],
        elif_blocks: List[tuple] = None,
        else_block: Optional[List[ASTNode]] = None,
    ):
        self.condition = condition
        self.then_block = then_block
        self.elif_blocks = elif_blocks or []  # List of (condition, block) tuples
        self.else_block = else_block

    def __repr__(self):
        return f"If({self.condition}, {self.then_block}, elif:{self.elif_blocks}, else:{self.else_block})"


class WhileNode(ASTNode):
    def __init__(self, condition: ASTNode, block: List[ASTNode]):
        self.condition = condition
        self.block = block

    def __repr__(self):
        return f"While({self.condition}, {self.block})"


class FunctionNode(ASTNode):
    def __init__(self, name: str, parameters: List[str], body: List[ASTNode]):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        return f"Function({self.name}, {self.parameters}, {self.body})"


class CallNode(ASTNode):
    def __init__(self, name: str, arguments: List[ASTNode]):
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return f"Call({self.name}, {self.arguments})"


class ReturnNode(ASTNode):
    def __init__(self, value: Optional[ASTNode]):
        self.value = value

    def __repr__(self):
        return f"Return({self.value})"


class ForNode(ASTNode):
    def __init__(self, variable: str, iterable: ASTNode, body: List[ASTNode]):
        self.variable = variable
        self.iterable = iterable
        self.body = body

    def __repr__(self):
        return f"For({self.variable}, {self.iterable}, {self.body})"


class StringMethodNode(ASTNode):
    def __init__(self, method: str, string: ASTNode, args: List[ASTNode] = None):
        self.method = method
        self.string = string
        self.args = args or []

    def __repr__(self):
        return f"StringMethod({self.method}, {self.string}, {self.args})"


class BuiltinFunctionNode(ASTNode):
    def __init__(self, function: str, args: List[ASTNode] = None):
        self.function = function
        self.args = args or []

    def __repr__(self):
        return f"BuiltinFunction({self.function}, {self.args})"


class TryCatchNode(ASTNode):
    def __init__(
        self,
        try_block: List[ASTNode],
        catch_blocks: List[tuple] = None,
        finally_block: Optional[List[ASTNode]] = None,
    ):
        self.try_block = try_block
        self.catch_blocks = (
            catch_blocks or []
        )  # List of (exception_type, variable_name, block) tuples
        self.finally_block = finally_block

    def __repr__(self):
        return f"TryCatch(try:{self.try_block}, catch:{self.catch_blocks}, finally:{self.finally_block})"


class ThrowNode(ASTNode):
    def __init__(self, expression: ASTNode):
        self.expression = expression

    def __repr__(self):
        return f"Throw({self.expression})"


class FileOperationNode(ASTNode):
    def __init__(
        self, operation: str, filename: ASTNode, content: Optional[ASTNode] = None
    ):
        self.operation = operation  # READ, WRITE, APPEND, EXISTS, DELETE, LIST, CREATE
        self.filename = filename
        self.content = content  # For WRITE and APPEND operations

    def __repr__(self):
        return f"FileOperation({self.operation}, {self.filename}, {self.content})"


class DictNode(ASTNode):
    def __init__(self, pairs: List[tuple]):
        self.pairs = pairs  # List of (key, value) tuples

    def __repr__(self):
        return f"Dict({self.pairs})"


class DictAccessNode(ASTNode):
    def __init__(self, dict_expr: ASTNode, key_expr: ASTNode):
        self.dict_expr = dict_expr
        self.key_expr = key_expr

    def __repr__(self):
        return f"DictAccess({self.dict_expr}[{self.key_expr}])"


class DictOperationNode(ASTNode):
    def __init__(
        self,
        operation: str,
        dict_expr: ASTNode,
        key_expr: ASTNode,
        value_expr: Optional[ASTNode] = None,
    ):
        self.operation = operation  # ADD, REMOVE, HAS
        self.dict_expr = dict_expr
        self.key_expr = key_expr
        self.value_expr = value_expr  # For ADD operation

    def __repr__(self):
        return f"DictOperation({self.operation}, {self.dict_expr}, {self.key_expr}, {self.value_expr})"


class ClassNode(ASTNode):
    def __init__(
        self,
        name: str,
        methods: List[ASTNode],
        properties: List[ASTNode] = None,
        parent_class: Optional[str] = None,
    ):
        self.name = name
        self.methods = methods
        self.properties = properties or []
        self.parent_class = parent_class

    def __repr__(self):
        return f"Class({self.name}, methods:{len(self.methods)}, parent:{self.parent_class})"


class MethodNode(ASTNode):
    def __init__(
        self,
        name: str,
        parameters: List[str],
        body: List[ASTNode],
        is_constructor: bool = False,
    ):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.is_constructor = is_constructor

    def __repr__(self):
        return f"Method({self.name}, params:{self.parameters}, constructor:{self.is_constructor})"


class PropertyNode(ASTNode):
    def __init__(self, name: str, initial_value: Optional[ASTNode] = None):
        self.name = name
        self.initial_value = initial_value

    def __repr__(self):
        return f"Property({self.name}, initial:{self.initial_value})"


class NewNode(ASTNode):
    def __init__(self, class_name: str, arguments: List[ASTNode]):
        self.class_name = class_name
        self.arguments = arguments

    def __repr__(self):
        return f"New({self.class_name}, args:{len(self.arguments)})"


class AccessNode(ASTNode):
    def __init__(self, object_expr: ASTNode, property_name: str):
        self.object_expr = object_expr
        self.property_name = property_name

    def __repr__(self):
        return f"Access({self.object_expr}.{self.property_name})"


class CallMethodNode(ASTNode):
    def __init__(
        self, object_expr: ASTNode, method_name: str, arguments: List[ASTNode]
    ):
        self.object_expr = object_expr
        self.method_name = method_name
        self.arguments = arguments

    def __repr__(self):
        return f"CallMethod({self.object_expr}.{self.method_name}, args:{len(self.arguments)})"


class PropertyAssignmentNode(ASTNode):
    def __init__(self, object_expr: ASTNode, property_name: str, value_expr: ASTNode):
        self.object_expr = object_expr
        self.property_name = property_name
        self.value_expr = value_expr

    def __repr__(self):
        return f"PropertyAssignment({self.object_expr}.{self.property_name} = {self.value_expr})"


class GeEzParser:
    """Parser for Ge-ez Amharic programming language"""

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> List[ASTNode]:
        """Parse tokens into AST"""
        statements = []

        while not self.is_at_end():
            statement = self.parse_statement()
            if statement:
                statements.append(statement)

        return statements

    def parse_statement(self) -> Optional[ASTNode]:
        """Parse a single statement"""
        if self.match("VAR"):
            return self.parse_variable_declaration()
        elif self.match("PRINT"):
            return self.parse_print_statement()
        elif self.match("IF"):
            return self.parse_if_statement()
        elif self.match("WHILE"):
            return self.parse_while_statement()
        elif self.match("FOR"):
            return self.parse_for_statement()
        elif self.match("FUNCTION"):
            return self.parse_function_declaration()
        elif self.match("RETURN"):
            return self.parse_return_statement()
        elif self.match("TRY"):
            return self.parse_try_catch_statement()
        elif self.match("THROW"):
            return self.parse_throw_statement()
        elif self.match("CLASS"):
            return self.parse_class_declaration()
        elif (
            self.check("IDENTIFIER")
            or self.check("AMHARIC_ID")
            or self.check("FOR")
            or self.check("SELF")
            or self.check("THIS")
        ):
            # Check if this is a function call or assignment
            if self.check_next("LPAREN"):
                return self.parse_function_call_statement()
            elif self.check_next("ASSIGN"):
                return self.parse_assignment()
            else:
                # Parse as expression (could be property access or method call)
                expr = self.parse_expression()
                return expr
        else:
            return self.parse_expression()

    def parse_variable_declaration(self) -> ASTNode:
        """Parse variable declaration: አስተዋውቅ identifier = expression"""
        identifier = self.consume(
            "IDENTIFIER", "AMHARIC_ID", "FOR", message="Expected identifier"
        ).value
        self.consume("ASSIGN", message="Expected =")
        value = self.parse_expression()
        return AssignmentNode(identifier, value)

    def parse_print_statement(self) -> ASTNode:
        """Parse print statement: ማተም expression"""
        expression = self.parse_expression()
        return PrintNode(expression)

    def parse_if_statement(self) -> ASTNode:
        """Parse if statement: ከሆነ condition { statements } አለበለዚያ condition { statements } ካልሆነ { statements }"""
        condition = self.parse_expression()

        then_block = []
        if self.match("LBRACE"):
            while not self.match("RBRACE") and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    then_block.append(stmt)

        # Parse elif blocks
        elif_blocks = []
        while self.match("ELIF"):
            elif_condition = self.parse_expression()
            elif_block = []
            if self.match("LBRACE"):
                while not self.match("RBRACE") and not self.is_at_end():
                    stmt = self.parse_statement()
                    if stmt:
                        elif_block.append(stmt)
            elif_blocks.append((elif_condition, elif_block))

        # Parse else block
        else_block = None
        if self.match("ELSE"):
            else_block = []
            if self.match("LBRACE"):
                while not self.match("RBRACE") and not self.is_at_end():
                    stmt = self.parse_statement()
                    if stmt:
                        else_block.append(stmt)

        return IfNode(condition, then_block, elif_blocks, else_block)

    def parse_while_statement(self) -> ASTNode:
        """Parse while statement: በመሆኑ condition { statements }"""
        condition = self.parse_expression()

        block = []
        if self.match("LBRACE"):
            while not self.match("RBRACE") and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    block.append(stmt)

        return WhileNode(condition, block)

    def parse_for_statement(self) -> ASTNode:
        """Parse for statement: ለ variable በ iterable { body }"""
        variable = self.consume(
            "IDENTIFIER", "AMHARIC_ID", "FOR", message="Expected variable name"
        ).value

        # Skip በ keyword
        if self.match("IN"):
            pass  # Skip the በ keyword
        else:
            error_msg = AmharicErrorMessages.get_parser_error(
                "expected_token",
                expected="በ",
                line=self.peek().line,
                column=self.peek().column,
            )
            raise SyntaxError(error_msg)

        # Parse iterable (for now, just a simple range or list)
        iterable = self.parse_expression()

        # Parse for loop body
        body = []
        if self.match("LBRACE"):
            while not self.match("RBRACE") and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    body.append(stmt)

        return ForNode(variable, iterable, body)

    def parse_function_declaration(self) -> ASTNode:
        """Parse function declaration: ተግባር name (parameters) { body }"""
        name = self.consume(
            "IDENTIFIER", "AMHARIC_ID", "FOR", message="Expected function name"
        ).value

        # Parse parameters
        parameters = []
        if self.match("LPAREN"):
            if not self.match("RPAREN"):
                while True:
                    param = self.consume(
                        "IDENTIFIER",
                        "AMHARIC_ID",
                        "FOR",
                        message="Expected parameter name",
                    ).value
                    parameters.append(param)
                    if not self.match("COMMA"):
                        break
                self.consume("RPAREN", message="Expected )")

        # Parse function body
        body = []
        if self.match("LBRACE"):
            while not self.match("RBRACE") and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    body.append(stmt)

        return FunctionNode(name, parameters, body)

    def parse_return_statement(self) -> ASTNode:
        """Parse return statement: ተመለስ expression"""
        value = None
        if not self.match("SEMICOLON", "NEWLINE"):
            value = self.parse_expression()
        return ReturnNode(value)

    def parse_function_call_statement(self) -> ASTNode:
        """Parse function call as statement"""
        name = self.previous().value
        arguments = []
        if self.match("LPAREN"):
            if not self.match("RPAREN"):
                while True:
                    arguments.append(self.parse_expression())
                    if not self.match("COMMA"):
                        break
                self.consume("RPAREN", message="Expected )")
        return CallNode(name, arguments)

    def parse_assignment(self) -> ASTNode:
        """Parse assignment: identifier = expression or object.property = expression"""
        # Parse the left side as an expression (could be identifier or property access)
        left = self.parse_expression()

        # Check if this is actually an assignment
        if not self.match("ASSIGN"):
            # Not an assignment, return the expression
            return left

        # Parse the right side
        value = self.parse_expression()

        # Check if left side is a simple identifier
        if isinstance(left, IdentifierNode):
            return AssignmentNode(left.name, value)
        elif isinstance(left, AccessNode):
            # Property assignment: object.property = value
            return PropertyAssignmentNode(left.object_expr, left.property_name, value)
        else:
            # Error: can't assign to this type
            raise SyntaxError("Can only assign to variables or properties")

    def parse_expression(self) -> ASTNode:
        """Parse expression"""
        return self.parse_logical_or()

    def parse_logical_or(self) -> ASTNode:
        """Parse logical OR: expression ወይም expression"""
        left = self.parse_logical_and()

        while self.match("OR"):
            operator = self.previous().value
            right = self.parse_logical_and()
            left = BinaryOpNode(left, operator, right)

        return left

    def parse_logical_and(self) -> ASTNode:
        """Parse logical AND: expression እና expression"""
        left = self.parse_equality()

        while self.match("AND"):
            operator = self.previous().value
            right = self.parse_equality()
            left = BinaryOpNode(left, operator, right)

        return left

    def parse_equality(self) -> ASTNode:
        """Parse equality: expression == expression or expression != expression"""
        left = self.parse_comparison()

        while self.match("EQUAL", "NOT_EQUAL"):
            operator = self.previous().value
            right = self.parse_comparison()
            left = BinaryOpNode(left, operator, right)

        return left

    def parse_comparison(self) -> ASTNode:
        """Parse comparison: expression < > <= >= expression"""
        left = self.parse_term()

        while self.match("LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL"):
            operator = self.previous().value
            right = self.parse_term()
            left = BinaryOpNode(left, operator, right)

        return left

    def parse_term(self) -> ASTNode:
        """Parse term: expression + - expression"""
        left = self.parse_factor()

        while self.match("PLUS", "MINUS"):
            operator = self.previous().value
            right = self.parse_factor()
            left = BinaryOpNode(left, operator, right)

        return left

    def parse_factor(self) -> ASTNode:
        """Parse factor: expression * / expression"""
        left = self.parse_unary()

        while self.match("MULTIPLY", "DIVIDE"):
            operator = self.previous().value
            right = self.parse_unary()
            left = BinaryOpNode(left, operator, right)

        return left

    def parse_unary(self) -> ASTNode:
        """Parse unary: - expression or ! expression"""
        if self.match("MINUS", "NOT"):
            operator = self.previous().value
            right = self.parse_unary()
            return UnaryOpNode(operator, right)

        return self.parse_primary()

    def parse_primary(self) -> ASTNode:
        """Parse primary: number, string, boolean, identifier, or (expression)"""
        expr = self.parse_atom()

        # Handle list indexing: expr[expr]
        while self.match("LBRACKET"):
            index_expr = self.parse_expression()
            self.consume("RBRACKET", "Expected ]")
            expr = IndexNode(expr, index_expr)

        # Handle property access: expr.property
        while self.match("DOT"):
            property_name = self.consume(
                "IDENTIFIER", "AMHARIC_ID", message="Expected property name"
            ).value

            # Handle method calls: expr.method(args)
            if self.match("LPAREN"):
                # This is a method call
                arguments = []
                if not self.match("RPAREN"):
                    while True:
                        arguments.append(self.parse_expression())
                        if not self.match("COMMA"):
                            break
                    self.consume("RPAREN", message="Expected )")
                return CallMethodNode(expr, property_name, arguments)
            else:
                # This is property access
                expr = AccessNode(expr, property_name)

        return expr

    def parse_atom(self) -> ASTNode:
        """Parse atomic expressions"""
        if self.match("NUMBER"):
            return NumberNode(float(self.previous().value))

        if self.match("STRING"):
            value = self.previous().value[1:-1]  # Remove quotes
            return StringNode(value)

        if self.match("TRUE"):
            return BooleanNode(True)

        if self.match("FALSE"):
            return BooleanNode(False)

        if self.match("INPUT"):
            # Parse input function: ግብአት() or ግብአት(prompt)
            self.consume("LPAREN", "Expected ( after ግብአት")
            prompt = None
            if not self.match("RPAREN"):
                prompt = self.parse_expression()
                self.consume("RPAREN", message="Expected )")
            return InputNode(prompt)

        # Parse file operations
        if self.match("READ", "WRITE", "APPEND", "EXISTS", "DELETE", "LIST", "CREATE"):
            return self.parse_file_operation()

        # Parse dictionary operations
        if self.match("ADD", "REMOVE", "HAS"):
            return self.parse_dict_operation()

        # Parse class instantiation
        if self.match("NEW"):
            return self.parse_new_instance()

        # Parse dictionary creation with braces
        if self.match("LBRACE"):
            return self.parse_dict_literal()

        # Parse string methods
        if self.match("LENGTH", "SPLIT", "JOIN", "UPPER", "LOWER", "REPLACE"):
            method = self.previous().type  # Use token type instead of value
            self.consume("LPAREN", f"Expected ( after {method}")

            # Parse the string argument
            string_arg = self.parse_expression()

            # Parse additional arguments for methods that need them
            args = []
            if method == "SPLIT":
                if self.match("COMMA"):
                    args.append(self.parse_expression())
            elif method == "JOIN":
                if self.match("COMMA"):
                    args.append(self.parse_expression())  # separator
            elif method == "REPLACE":
                if self.match("COMMA"):
                    args.append(self.parse_expression())  # old_string
                    if self.match("COMMA"):
                        args.append(self.parse_expression())  # new_string

            self.consume("RPAREN", f"Expected ) after {method}")
            return StringMethodNode(method, string_arg, args)

        if self.match("IDENTIFIER", "AMHARIC_ID", "FOR", "SELF", "THIS"):
            name = self.previous().value
            # Check if this is a function call
            if self.match("LPAREN"):
                # Check if this is a built-in function
                if name in ["ወሰን", "ዓይነት", "ቁጥር", "ጽሑፍ", "ከፍተኛ", "ዠቅተኛ"]:
                    # Map Amharic names to token types
                    function_map = {
                        "ወሰን": "RANGE",
                        "ዓይነት": "TYPE",
                        "ቁጥር": "INT",
                        "ጽሑፍ": "STR",
                        "ከፍተኛ": "MAX",
                        "ዠቅተኛ": "MIN",
                    }
                    function_type = function_map[name]

                    # Parse arguments
                    args = []
                    if not self.match("RPAREN"):
                        while True:
                            args.append(self.parse_expression())
                            if not self.match("COMMA"):
                                break
                        self.consume("RPAREN", f"Expected ) after {name}")

                    return BuiltinFunctionNode(function_type, args)
                else:
                    # Regular function call
                    arguments = []
                    if not self.match("RPAREN"):
                        while True:
                            arguments.append(self.parse_expression())
                            if not self.match("COMMA"):
                                break
                        self.consume("RPAREN", message="Expected )")
                    return CallNode(name, arguments)
            else:
                # Check for dictionary access: identifier[key]
                if self.match("LBRACKET"):
                    key = self.parse_expression()
                    self.consume("RBRACKET", message="Expected ]")
                    return DictAccessNode(IdentifierNode(name), key)
                else:
                    # Return identifier, property access will be handled in parse_primary
                    return IdentifierNode(name)

        if self.match("LPAREN"):
            expr = self.parse_expression()
            self.consume("RPAREN", "Expected )")
            return expr

        error_msg = AmharicErrorMessages.get_parser_error(
            "unexpected_token",
            token=self.peek().value,
            line=self.peek().line,
            column=self.peek().column,
        )
        raise SyntaxError(error_msg)

    def match(self, *token_types: str) -> bool:
        """Check if current token matches any of the given types"""
        for token_type in token_types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def check(self, token_type: str) -> bool:
        """Check if current token is of given type"""
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def check_next(self, *token_types: str) -> bool:
        """Check if the next token matches any of the given types"""
        if self.current + 1 >= len(self.tokens):
            return False
        return self.tokens[self.current + 1].type in token_types

    def advance(self) -> Token:
        """Move to next token"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        """Check if we're at the end of tokens"""
        return self.peek().type == "EOF" or self.current >= len(self.tokens)

    def peek(self) -> Token:
        """Get current token without advancing"""
        if self.current >= len(self.tokens):
            return Token("EOF", "", 0, 0)
        return self.tokens[self.current]

    def previous(self) -> Token:
        """Get previous token"""
        return self.tokens[self.current - 1]

    def consume(self, *token_types: str, message: str = "Expected token") -> Token:
        """Consume token of expected type"""
        for token_type in token_types:
            if self.check(token_type):
                return self.advance()

        # Create enhanced error message
        if message == "Expected token":
            if len(token_types) == 1:
                expected = token_types[0]
            else:
                # Map token types to more readable Amharic names
                token_names = []
                for token_type in token_types:
                    if token_type == "IDENTIFIER":
                        token_names.append("የተለዋዋጭ ስም")
                    elif token_type == "AMHARIC_ID":
                        token_names.append("የአማርኛ ስም")
                    elif token_type == "FOR":
                        token_names.append("ለ")
                    elif token_type == "STRING":
                        token_names.append("ገላጭ")
                    elif token_type == "NUMBER":
                        token_names.append("ቁጥር")
                    else:
                        token_names.append(token_type)
                expected = f"ከ {', '.join(token_names)} ውስጥ አንዱ"

            error_msg = AmharicErrorMessages.get_parser_error(
                "expected_token",
                expected=expected,
                line=self.peek().line,
                column=self.peek().column,
            )
        else:
            # Handle custom messages
            if message == "Expected identifier":
                expected = "የተለዋዋጭ ስም"
            elif message == "Expected variable name":
                expected = "የተለዋዋጭ ስም"
            elif message == "Expected function name":
                expected = "የተግባር ስም"
            elif message == "Expected parameter name":
                expected = "የነጋሪ እሴት ስም"
            elif message == "Expected )":
                expected = ")"
            elif message == "Expected ]":
                expected = "]"
            elif message == "Expected =":
                expected = "="
            else:
                expected = message

            error_msg = AmharicErrorMessages.get_parser_error(
                "expected_token",
                expected=expected,
                line=self.peek().line,
                column=self.peek().column,
            )

        raise SyntaxError(error_msg)

    def parse_try_catch_statement(self) -> ASTNode:
        """Parse try-catch-finally statement: ሞክር { statements } ያዝ exception_type variable { statements } በመጨረሻ { statements }"""
        # Parse try block
        try_block = []
        if self.match("LBRACE"):
            while not self.match("RBRACE") and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    try_block.append(stmt)

        # Parse catch blocks
        catch_blocks = []
        while self.match("CATCH"):
            # Parse exception type and variable name
            exception_type = None
            variable_name = None

            # Check if there are parentheses (optional)
            if self.match("LPAREN"):
                if not self.match("RPAREN"):
                    exception_type = self.consume(
                        "IDENTIFIER",
                        "AMHARIC_ID",
                        "STRING",
                        message="Expected exception type",
                    ).value
                    if self.match("COMMA"):
                        variable_name = self.consume(
                            "IDENTIFIER", "AMHARIC_ID", message="Expected variable name"
                        ).value
                    self.consume("RPAREN", message="Expected )")
                else:
                    # Empty parentheses - no exception type or variable
                    pass

            # Parse catch block
            catch_block = []
            if self.match("LBRACE"):
                while not self.match("RBRACE") and not self.is_at_end():
                    stmt = self.parse_statement()
                    if stmt:
                        catch_block.append(stmt)

            catch_blocks.append((exception_type, variable_name, catch_block))

        # Parse finally block
        finally_block = None
        if self.match("FINALLY"):
            finally_block = []
            if self.match("LBRACE"):
                while not self.match("RBRACE") and not self.is_at_end():
                    stmt = self.parse_statement()
                    if stmt:
                        finally_block.append(stmt)

        return TryCatchNode(try_block, catch_blocks, finally_block)

    def parse_throw_statement(self) -> ASTNode:
        """Parse throw statement: አስተላልፍ expression"""
        expression = self.parse_expression()
        return ThrowNode(expression)

    def parse_file_operation(self) -> ASTNode:
        """Parse file operation: አንብብ/ጻፍ/ጨምር/አለ/ሰርዝ/ዝርዝር/ፍጠር filename [content]"""
        operation = self.previous().type  # READ, WRITE, APPEND, etc.

        # Parse filename
        filename = self.parse_expression()

        # Parse content for WRITE and APPEND operations
        content = None
        if operation in ["WRITE", "APPEND"]:
            if not self.match("SEMICOLON", "NEWLINE"):
                content = self.parse_expression()

        return FileOperationNode(operation, filename, content)

    def parse_dict_operation(self) -> ASTNode:
        """Parse dictionary operation: ጨምር_ወደ/ሰርዝ_ከ/አለ_በ dict key [value]"""
        operation = self.previous().type  # ADD, REMOVE, HAS

        # Parse dictionary operations: ADD, REMOVE, HAS
        # Parse dictionary expression
        dict_expr = self.parse_expression()

        # Parse key
        key_expr = self.parse_expression()

        # Parse value for ADD operation
        value_expr = None
        if operation == "ADD":
            if not self.match("SEMICOLON", "NEWLINE"):
                value_expr = self.parse_expression()

        return DictOperationNode(operation, dict_expr, key_expr, value_expr)

    def parse_dict_literal(self) -> ASTNode:
        """Parse dictionary literal: {key: value, key2: value2}"""
        pairs = []

        if not self.match("RBRACE"):
            while True:
                # Parse key
                key = self.parse_expression()
                self.consume("COLON", message="Expected :")
                # Parse value
                value = self.parse_expression()
                pairs.append((key, value))

                if not self.match("COMMA"):
                    break

            self.consume("RBRACE", message="Expected }")

        return DictNode(pairs)

    def parse_class_declaration(self) -> ASTNode:
        """Parse class declaration: ክፍል name [ተወላጅ parent] { methods }"""
        # CLASS token has already been consumed by match() in parse_statement()
        class_name = self.consume(
            "IDENTIFIER", "AMHARIC_ID", message="Expected class name"
        ).value

        # Parse inheritance
        parent_class = None
        if self.match("INHERITS"):
            parent_class = self.consume(
                "IDENTIFIER", "AMHARIC_ID", message="Expected parent class name"
            ).value

        # Parse class body
        self.consume("LBRACE", message="Expected {")
        methods = []
        properties = []

        while not self.match("RBRACE"):
            if self.match("METHOD"):
                method = self.parse_method_declaration()
                methods.append(method)
            elif self.match("PROPERTY"):
                property_node = self.parse_property_declaration()
                properties.append(property_node)
            else:
                # This should not happen in a well-formed class
                # Skip unexpected tokens
                if not self.is_at_end():
                    self.advance()

        return ClassNode(class_name, methods, properties, parent_class)

    def parse_method_declaration(self) -> ASTNode:
        """Parse method declaration: ዘዴ name(params) { body }"""
        method_name = self.consume(
            "IDENTIFIER", "AMHARIC_ID", message="Expected method name"
        ).value

        # Parse parameters
        parameters = []
        self.consume("LPAREN", message="Expected (")
        if not self.match("RPAREN"):
            while True:
                param = self.consume(
                    "IDENTIFIER",
                    "AMHARIC_ID",
                    "SELF",
                    "THIS",
                    message="Expected parameter name",
                ).value
                parameters.append(param)
                if not self.match("COMMA"):
                    break
            self.consume("RPAREN", message="Expected )")

        # Parse method body
        self.consume("LBRACE", message="Expected {")
        body = []
        while not self.match("RBRACE"):
            # Parse as method body statement
            statement = self.parse_method_body_statement()
            if statement:
                body.append(statement)
            # Skip semicolons if present
            self.match("SEMICOLON")

        # Check if this is a constructor
        is_constructor = method_name == "መጀመሪያ" or method_name == "constructor"

        return MethodNode(method_name, parameters, body, is_constructor)

    def parse_property_declaration(self) -> ASTNode:
        """Parse property declaration: ባህሪ name [= value]"""
        property_name = self.consume(
            "IDENTIFIER", "AMHARIC_ID", message="Expected property name"
        ).value

        # Parse initial value if present
        initial_value = None
        if self.match("ASSIGN"):
            initial_value = self.parse_expression()

        return PropertyNode(property_name, initial_value)

    def parse_new_instance(self) -> ASTNode:
        """Parse new instance: አዲስ class_name(args)"""
        class_name = self.consume(
            "IDENTIFIER", "AMHARIC_ID", message="Expected class name"
        ).value

        # Parse arguments
        arguments = []
        self.consume("LPAREN", message="Expected (")
        if not self.match("RPAREN"):
            while True:
                arguments.append(self.parse_expression())
                if not self.match("COMMA"):
                    break
            self.consume("RPAREN", message="Expected )")

        return NewNode(class_name, arguments)

    def parse_method_body_statement(self) -> ASTNode:
        """Parse a statement within a method body"""
        if self.match("PRINT"):
            return self.parse_print_statement()
        elif self.match("RETURN"):
            return self.parse_return_statement()
        elif (
            self.check("IDENTIFIER")
            or self.check("AMHARIC_ID")
            or self.check("SELF")
            or self.check("THIS")
        ):
            # Check if this is a function call
            if self.check_next("LPAREN"):
                return self.parse_function_call_statement()
            else:
                # Parse as expression (could be property access or method call)
                expr = self.parse_expression()

                # Check if this is followed by an assignment
                if self.match("ASSIGN"):
                    # It's an assignment to the expression
                    value = self.parse_expression()
                    if isinstance(expr, IdentifierNode):
                        return AssignmentNode(expr.name, value)
                    elif isinstance(expr, AccessNode):
                        return PropertyAssignmentNode(
                            expr.object_expr, expr.property_name, value
                        )
                    else:
                        raise SyntaxError("Can only assign to variables or properties")
                else:
                    return expr
        else:
            return self.parse_expression()
