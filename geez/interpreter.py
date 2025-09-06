"""
Ge-ez Interpreter
Executes the Abstract Syntax Tree (AST)
"""

from typing import Any, Dict, List
from .parser import (
    ASTNode, NumberNode, StringNode, BooleanNode, IdentifierNode,
    BinaryOpNode, UnaryOpNode, AssignmentNode, PrintNode, IfNode, WhileNode,
    FunctionNode, CallNode, ReturnNode, ForNode, ListNode, IndexNode
)


class GeEzInterpreter:
    """Interpreter for Ge-ez Amharic programming language"""
    
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, FunctionNode] = {}
    
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
        
        elif isinstance(node, ListNode):
            return self.execute_list(node)
        
        elif isinstance(node, IndexNode):
            return self.execute_index(node)
        
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
        
        elif isinstance(node, ForNode):
            return self.execute_for(node)
        
        elif isinstance(node, FunctionNode):
            return self.execute_function_declaration(node)
        
        elif isinstance(node, CallNode):
            return self.execute_function_call(node)
        
        elif isinstance(node, ReturnNode):
            return self.execute_return(node)
        
        else:
            raise RuntimeError(f"Unknown node type: {type(node)}")
    
    def execute_binary_op(self, node: BinaryOpNode) -> Any:
        """Execute binary operation"""
        left = self.execute(node.left)
        right = self.execute(node.right)
        
        if node.operator == '+':
            # Handle string concatenation
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
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
    
    def execute_for(self, node: ForNode) -> Any:
        """Execute for loop"""
        # For now, we'll implement a simple range-based for loop
        # Later we can extend this to work with lists and other iterables
        
        iterable = self.execute(node.iterable)
        
        # Simple range implementation for numbers
        if isinstance(iterable, (int, float)):
            for i in range(int(iterable)):
                self.variables[node.variable] = i
                for statement in node.body:
                    self.execute(statement)
        else:
            raise RuntimeError(f"Cannot iterate over {type(iterable)}")
        
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
    
    def execute_function_declaration(self, node: FunctionNode) -> None:
        """Execute function declaration"""
        self.functions[node.name] = node
        return None
    
    def execute_function_call(self, node: CallNode) -> Any:
        """Execute function call"""
        if node.name not in self.functions:
            raise RuntimeError(f"Undefined function: {node.name}")
        
        function = self.functions[node.name]
        
        # Check argument count
        if len(node.arguments) != len(function.parameters):
            raise RuntimeError(f"Function {node.name} expects {len(function.parameters)} arguments, got {len(node.arguments)}")
        
        # Save current scope
        old_variables = self.variables.copy()
        
        # Create new scope with parameters
        self.variables = {}
        for param, arg in zip(function.parameters, node.arguments):
            self.variables[param] = self.execute(arg)
        
        # Execute function body
        result = None
        try:
            for statement in function.body:
                result = self.execute(statement)
        except ReturnException as e:
            result = e.value
        
        # Restore old scope
        self.variables = old_variables
        
        return result
    
    def execute_return(self, node: ReturnNode) -> Any:
        """Execute return statement"""
        value = self.execute(node.value) if node.value else None
        raise ReturnException(value)
    
    def execute_list(self, node: ListNode) -> List[Any]:
        """Execute list creation: [expr1, expr2, ...]"""
        return [self.execute(element) for element in node.elements]
    
    def execute_index(self, node: IndexNode) -> Any:
        """Execute list indexing: list[index]"""
        list_value = self.execute(node.list_expr)
        index_value = self.execute(node.index_expr)
        
        if not isinstance(list_value, list):
            raise TypeError(f"Can only index lists, not {type(list_value).__name__}")
        
        if not isinstance(index_value, (int, float)):
            raise TypeError(f"List index must be a number, not {type(index_value).__name__}")
        
        index = int(index_value)
        if index < 0 or index >= len(list_value):
            raise IndexError(f"List index {index} out of range (list has {len(list_value)} elements)")
        
        return list_value[index]


class ReturnException(Exception):
    """Exception used for return statements"""
    def __init__(self, value: Any):
        self.value = value
