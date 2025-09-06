"""
Ge-ez Interpreter
Executes the Abstract Syntax Tree (AST)
"""

from typing import Any, Dict, List
from .parser import (
    ASTNode, NumberNode, StringNode, BooleanNode, IdentifierNode,
    BinaryOpNode, UnaryOpNode, AssignmentNode, PrintNode, IfNode, WhileNode
)


class GeEzInterpreter:
    """Interpreter for Ge-ez Amharic programming language"""
    
    def __init__(self):
        self.variables: Dict[str, Any] = {}
    
    def interpret(self, code: str) -> Any:
        """Interpret Ge-ez code"""
        from .lexer import GeEzLexer
        from .parser import GeEzParser
        
        try:
            # Tokenize
            lexer = GeEzLexer()
            tokens = lexer.tokenize(code)
            
            # Parse
            parser = GeEzParser(tokens)
            ast = parser.parse()
            
            # Execute
            result = None
            for statement in ast:
                result = self.execute(statement)
            
            return result
            
        except Exception as e:
            print(f"ስህተት: {e}")
            return None
    
    def execute(self, node: ASTNode) -> Any:
        """Execute an AST node"""
        if isinstance(node, NumberNode):
            return node.value
        
        elif isinstance(node, StringNode):
            return node.value
        
        elif isinstance(node, BooleanNode):
            return node.value
        
        elif isinstance(node, IdentifierNode):
            return self.get_variable(node.name)
        
        elif isinstance(node, BinaryOpNode):
            return self.execute_binary_op(node)
        
        elif isinstance(node, UnaryOpNode):
            return self.execute_unary_op(node)
        
        elif isinstance(node, AssignmentNode):
            return self.execute_assignment(node)
        
        elif isinstance(node, PrintNode):
            return self.execute_print(node)
        
        elif isinstance(node, IfNode):
            return self.execute_if(node)
        
        elif isinstance(node, WhileNode):
            return self.execute_while(node)
        
        else:
            raise RuntimeError(f"Unknown node type: {type(node)}")
    
    def execute_binary_op(self, node: BinaryOpNode) -> Any:
        """Execute binary operation"""
        left = self.execute(node.left)
        right = self.execute(node.right)
        
        if node.operator == '+':
            return left + right
        elif node.operator == '-':
            return left - right
        elif node.operator == '*':
            return left * right
        elif node.operator == '/':
            if right == 0:
                raise RuntimeError("Division by zero")
            return left / right
        elif node.operator == '==':
            return left == right
        elif node.operator == '!=':
            return left != right
        elif node.operator == '<':
            return left < right
        elif node.operator == '>':
            return left > right
        elif node.operator == '<=':
            return left <= right
        elif node.operator == '>=':
            return left >= right
        elif node.operator == 'እና':  # AND
            return left and right
        elif node.operator == 'ወይም':  # OR
            return left or right
        else:
            raise RuntimeError(f"Unknown binary operator: {node.operator}")
    
    def execute_unary_op(self, node: UnaryOpNode) -> Any:
        """Execute unary operation"""
        right = self.execute(node.operand)
        
        if node.operator == '-':
            return -right
        elif node.operator == 'አይደለም':  # NOT
            return not right
        else:
            raise RuntimeError(f"Unknown unary operator: {node.operator}")
    
    def execute_assignment(self, node: AssignmentNode) -> Any:
        """Execute assignment"""
        value = self.execute(node.value)
        self.variables[node.identifier] = value
        return value
    
    def execute_print(self, node: PrintNode) -> Any:
        """Execute print statement"""
        value = self.execute(node.expression)
        print(value)
        return value
    
    def execute_if(self, node: IfNode) -> Any:
        """Execute if statement"""
        condition = self.execute(node.condition)
        
        if condition:
            for statement in node.then_block:
                self.execute(statement)
        elif node.else_block:
            for statement in node.else_block:
                self.execute(statement)
        
        return None
    
    def execute_while(self, node: WhileNode) -> Any:
        """Execute while loop"""
        while self.execute(node.condition):
            for statement in node.block:
                self.execute(statement)
        
        return None
    
    def get_variable(self, name: str) -> Any:
        """Get variable value"""
        if name in self.variables:
            return self.variables[name]
        else:
            raise RuntimeError(f"Undefined variable: {name}")
    
    def set_variable(self, name: str, value: Any) -> None:
        """Set variable value"""
        self.variables[name] = value
    
    def clear_variables(self) -> None:
        """Clear all variables"""
        self.variables.clear()
