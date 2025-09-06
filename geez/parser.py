"""
Ge-ez Parser
Builds Abstract Syntax Tree (AST) from tokens
"""

from typing import List, Optional, Union
from .lexer import Token


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
    def __init__(self, condition: ASTNode, then_block: List[ASTNode], else_block: Optional[List[ASTNode]] = None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
    
    def __repr__(self):
        return f"If({self.condition}, {self.then_block}, {self.else_block})"


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
        if self.match('VAR'):
            return self.parse_variable_declaration()
        elif self.match('PRINT'):
            return self.parse_print_statement()
        elif self.match('IF'):
            return self.parse_if_statement()
        elif self.match('WHILE'):
            return self.parse_while_statement()
        elif self.match('FOR'):
            return self.parse_for_statement()
        elif self.match('FUNCTION'):
            return self.parse_function_declaration()
        elif self.match('RETURN'):
            return self.parse_return_statement()
        elif self.match('IDENTIFIER', 'AMHARIC_ID'):
            # Check if this is a function call or assignment
            if self.check('LPAREN'):
                return self.parse_function_call_statement()
            else:
                return self.parse_assignment()
        else:
            return self.parse_expression()
    
    def parse_variable_declaration(self) -> ASTNode:
        """Parse variable declaration: አስተዋውቅ identifier = expression"""
        identifier = self.consume('IDENTIFIER', 'AMHARIC_ID', 'Expected identifier').value
        self.consume('ASSIGN', 'Expected =')
        value = self.parse_expression()
        return AssignmentNode(identifier, value)
    
    def parse_print_statement(self) -> ASTNode:
        """Parse print statement: ማተም expression"""
        expression = self.parse_expression()
        return PrintNode(expression)
    
    def parse_if_statement(self) -> ASTNode:
        """Parse if statement: ከሆነ condition { statements } ማተምበለዚያ { statements }"""
        condition = self.parse_expression()
        
        then_block = []
        if self.match('LBRACE'):
            while not self.match('RBRACE') and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    then_block.append(stmt)
        
        else_block = None
        if self.match('ELSE'):
            else_block = []
            if self.match('LBRACE'):
                while not self.match('RBRACE') and not self.is_at_end():
                    stmt = self.parse_statement()
                    if stmt:
                        else_block.append(stmt)
        
        return IfNode(condition, then_block, else_block)
    
    def parse_while_statement(self) -> ASTNode:
        """Parse while statement: በመሆኑ condition { statements }"""
        condition = self.parse_expression()
        
        block = []
        if self.match('LBRACE'):
            while not self.match('RBRACE') and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    block.append(stmt)
        
        return WhileNode(condition, block)
    
    def parse_for_statement(self) -> ASTNode:
        """Parse for statement: ለ variable በ iterable { body }"""
        variable = self.consume('IDENTIFIER', 'AMHARIC_ID', 'Expected variable name').value
        
        # Skip በ keyword
        if self.match('IN'):
            pass  # Skip the በ keyword
        else:
            raise SyntaxError("Expected በ keyword")
        
        # Parse iterable (for now, just a simple range or list)
        iterable = self.parse_expression()
        
        # Parse for loop body
        body = []
        if self.match('LBRACE'):
            while not self.match('RBRACE') and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    body.append(stmt)
        
        return ForNode(variable, iterable, body)
    
    def parse_function_declaration(self) -> ASTNode:
        """Parse function declaration: ተግባር name (parameters) { body }"""
        name = self.consume('IDENTIFIER', 'AMHARIC_ID', 'Expected function name').value
        
        # Parse parameters
        parameters = []
        if self.match('LPAREN'):
            if not self.match('RPAREN'):
                while True:
                    param = self.consume('IDENTIFIER', 'AMHARIC_ID', 'Expected parameter name').value
                    parameters.append(param)
                    if not self.match('COMMA'):
                        break
                self.consume('RPAREN', 'Expected )')
        
        # Parse function body
        body = []
        if self.match('LBRACE'):
            while not self.match('RBRACE') and not self.is_at_end():
                stmt = self.parse_statement()
                if stmt:
                    body.append(stmt)
        
        return FunctionNode(name, parameters, body)
    
    def parse_return_statement(self) -> ASTNode:
        """Parse return statement: ተመለስ expression"""
        value = None
        if not self.match('SEMICOLON', 'NEWLINE'):
            value = self.parse_expression()
        return ReturnNode(value)
    
    def parse_function_call_statement(self) -> ASTNode:
        """Parse function call as statement"""
        name = self.previous().value
        arguments = []
        if self.match('LPAREN'):
            if not self.match('RPAREN'):
                while True:
                    arguments.append(self.parse_expression())
                    if not self.match('COMMA'):
                        break
                self.consume('RPAREN', 'Expected )')
        return CallNode(name, arguments)
    
    def parse_assignment(self) -> ASTNode:
        """Parse assignment: identifier = expression"""
        identifier = self.previous().value
        self.consume('ASSIGN', 'Expected =')
        value = self.parse_expression()
        return AssignmentNode(identifier, value)
    
    def parse_expression(self) -> ASTNode:
        """Parse expression"""
        return self.parse_logical_or()
    
    def parse_logical_or(self) -> ASTNode:
        """Parse logical OR: expression ወይም expression"""
        left = self.parse_logical_and()
        
        while self.match('OR'):
            operator = self.previous().value
            right = self.parse_logical_and()
            left = BinaryOpNode(left, operator, right)
        
        return left
    
    def parse_logical_and(self) -> ASTNode:
        """Parse logical AND: expression እና expression"""
        left = self.parse_equality()
        
        while self.match('AND'):
            operator = self.previous().value
            right = self.parse_equality()
            left = BinaryOpNode(left, operator, right)
        
        return left
    
    def parse_equality(self) -> ASTNode:
        """Parse equality: expression == expression or expression != expression"""
        left = self.parse_comparison()
        
        while self.match('EQUAL', 'NOT_EQUAL'):
            operator = self.previous().value
            right = self.parse_comparison()
            left = BinaryOpNode(left, operator, right)
        
        return left
    
    def parse_comparison(self) -> ASTNode:
        """Parse comparison: expression < > <= >= expression"""
        left = self.parse_term()
        
        while self.match('LESS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL'):
            operator = self.previous().value
            right = self.parse_term()
            left = BinaryOpNode(left, operator, right)
        
        return left
    
    def parse_term(self) -> ASTNode:
        """Parse term: expression + - expression"""
        left = self.parse_factor()
        
        while self.match('PLUS', 'MINUS'):
            operator = self.previous().value
            right = self.parse_factor()
            left = BinaryOpNode(left, operator, right)
        
        return left
    
    def parse_factor(self) -> ASTNode:
        """Parse factor: expression * / expression"""
        left = self.parse_unary()
        
        while self.match('MULTIPLY', 'DIVIDE'):
            operator = self.previous().value
            right = self.parse_unary()
            left = BinaryOpNode(left, operator, right)
        
        return left
    
    def parse_unary(self) -> ASTNode:
        """Parse unary: - expression or ! expression"""
        if self.match('MINUS', 'NOT'):
            operator = self.previous().value
            right = self.parse_unary()
            return UnaryOpNode(operator, right)
        
        return self.parse_primary()
    
    def parse_primary(self) -> ASTNode:
        """Parse primary: number, string, boolean, identifier, or (expression)"""
        if self.match('NUMBER'):
            return NumberNode(float(self.previous().value))
        
        if self.match('STRING'):
            value = self.previous().value[1:-1]  # Remove quotes
            return StringNode(value)
        
        if self.match('TRUE'):
            return BooleanNode(True)
        
        if self.match('FALSE'):
            return BooleanNode(False)
        
        if self.match('IDENTIFIER', 'AMHARIC_ID'):
            name = self.previous().value
            # Check if this is a function call
            if self.match('LPAREN'):
                arguments = []
                if not self.match('RPAREN'):
                    while True:
                        arguments.append(self.parse_expression())
                        if not self.match('COMMA'):
                            break
                    self.consume('RPAREN', 'Expected )')
                return CallNode(name, arguments)
            else:
                return IdentifierNode(name)
        
        if self.match('LPAREN'):
            expr = self.parse_expression()
            self.consume('RPAREN', 'Expected )')
            return expr
        
        raise SyntaxError(f"Unexpected token: {self.peek()}")
    
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
    
    def advance(self) -> Token:
        """Move to next token"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()
    
    def is_at_end(self) -> bool:
        """Check if we're at the end of tokens"""
        return self.peek().type == 'EOF' or self.current >= len(self.tokens)
    
    def peek(self) -> Token:
        """Get current token without advancing"""
        if self.current >= len(self.tokens):
            return Token('EOF', '', 0, 0)
        return self.tokens[self.current]
    
    def previous(self) -> Token:
        """Get previous token"""
        return self.tokens[self.current - 1]
    
    def consume(self, *token_types: str, message: str = "Expected token") -> Token:
        """Consume token of expected type"""
        for token_type in token_types:
            if self.check(token_type):
                return self.advance()
        
        raise SyntaxError(f"{message} at line {self.peek().line}, column {self.peek().column}")