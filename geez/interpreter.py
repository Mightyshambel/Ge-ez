"""
Ge-ez Interpreter
Executes the Abstract Syntax Tree (AST)
"""

from typing import Any, Dict, List
from .parser import (
    ASTNode, NumberNode, StringNode, BooleanNode, IdentifierNode,
    BinaryOpNode, UnaryOpNode, AssignmentNode, PrintNode, IfNode, WhileNode,
    FunctionNode, CallNode, ReturnNode, ForNode, ListNode, IndexNode, InputNode,
    StringMethodNode, BuiltinFunctionNode, TryCatchNode, ThrowNode, FileOperationNode,
    DictNode, DictAccessNode, DictOperationNode
)
from .errors import AmharicErrorMessages


class GeEzInterpreter:
    """Interpreter for Ge-ez Amharic programming language"""
    
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, FunctionNode] = {}
        self.in_try_catch = False  # Flag to track if we're in try-catch context
        
        # Performance optimizations
        self._expression_cache: Dict[str, Any] = {}  # Cache for computed expressions
        self._variable_cache: Dict[str, Any] = {}    # Cache for variable lookups
        self._function_cache: Dict[str, FunctionNode] = {}  # Cache for function lookups
        self._cache_enabled = True  # Enable/disable caching
        
        # Dispatch table for faster node execution
        self._node_handlers = {
            NumberNode: lambda n: n.value,
            StringNode: lambda n: n.value,
            BooleanNode: lambda n: n.value,
            IdentifierNode: lambda n: self.get_variable(n.name),
            ListNode: self.execute_list,
            IndexNode: self.execute_index,
            InputNode: self.execute_input,
            StringMethodNode: self.execute_string_method,
            BuiltinFunctionNode: self.execute_builtin_function,
            TryCatchNode: self.execute_try_catch,
            ThrowNode: self.execute_throw,
            FileOperationNode: self.execute_file_operation,
            DictNode: self.execute_dict,
            DictAccessNode: self.execute_dict_access,
            DictOperationNode: self.execute_dict_operation,
            BinaryOpNode: self.execute_binary_op,
            UnaryOpNode: self.execute_unary_op,
            AssignmentNode: self.execute_assignment,
            PrintNode: self.execute_print,
            IfNode: self.execute_if,
            WhileNode: self.execute_while,
            ForNode: self.execute_for,
            FunctionNode: self.execute_function_declaration,
            CallNode: self.execute_function_call,
            ReturnNode: self.execute_return,
        }
    
    def clear_cache(self) -> None:
        """Clear all caches for memory management"""
        self._expression_cache.clear()
        self._variable_cache.clear()
        self._function_cache.clear()
    
    def enable_cache(self, enabled: bool = True) -> None:
        """Enable or disable caching"""
        self._cache_enabled = enabled
        if not enabled:
            self.clear_cache()
    
    def get_cache_stats(self) -> Dict[str, int]:
        """Get cache statistics for performance monitoring"""
        return {
            'expression_cache_size': len(self._expression_cache),
            'variable_cache_size': len(self._variable_cache),
            'function_cache_size': len(self._function_cache),
            'cache_enabled': self._cache_enabled
        }
    
    def interpret(self, code: str) -> Any:
        """Interpret Ge-ez code"""
        from .lexer import GeEzLexer
        from .parser import GeEzParser, TryCatchNode
        
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
                # Special handling for try-catch statements
                if isinstance(statement, TryCatchNode):
                    result = self.execute_try_catch(statement)
                else:
                    result = self.execute(statement)
            
            return result
            
        except Exception as e:
            # Only catch exceptions if we're not in a try-catch context
            if not self.in_try_catch:
                error_msg = AmharicErrorMessages.format_error_with_suggestion(
                    'runtime_error',
                    str(e)
                )
                print(error_msg)
            else:
                # Re-raise the exception so it can be caught by try-catch blocks
                raise e
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
        
        elif isinstance(node, InputNode):
            return self.execute_input(node)
        
        elif isinstance(node, StringMethodNode):
            return self.execute_string_method(node)
        
        elif isinstance(node, BuiltinFunctionNode):
            return self.execute_builtin_function(node)
        
        elif isinstance(node, TryCatchNode):
            return self.execute_try_catch(node)
        
        elif isinstance(node, ThrowNode):
            return self.execute_throw(node)
        
        elif isinstance(node, FileOperationNode):
            return self.execute_file_operation(node)
        
        elif isinstance(node, DictNode):
            return self.execute_dict(node)
        
        elif isinstance(node, DictAccessNode):
            return self.execute_dict_access(node)
        
        elif isinstance(node, DictOperationNode):
            return self.execute_dict_operation(node)
        
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
                error_msg = AmharicErrorMessages.format_error_with_suggestion(
                    'division_by_zero',
                    AmharicErrorMessages.get_interpreter_error('division_by_zero')
                )
                raise RuntimeError(error_msg)
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
        """Execute assignment with optimized variable setting"""
        value = self.execute(node.value)
        self.set_variable(node.identifier, value)
        return value
    
    def execute_print(self, node: PrintNode) -> Any:
        """Execute print statement"""
        value = self.execute(node.expression)
        print(value)
        return value
    
    def execute_if(self, node: IfNode) -> Any:
        """Execute if statement with elif support"""
        condition = self.execute(node.condition)
        
        if condition:
            for statement in node.then_block:
                self.execute(statement)
        else:
            # Check elif blocks
            elif_executed = False
            for elif_condition, elif_block in node.elif_blocks:
                if self.execute(elif_condition):
                    for statement in elif_block:
                        self.execute(statement)
                    elif_executed = True
                    break
            
            # Execute else block if no elif was executed
            if not elif_executed and node.else_block:
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
        """Get variable value with caching optimization"""
        # Check cache first if enabled
        if self._cache_enabled and name in self._variable_cache:
            return self._variable_cache[name]
        
        # Check variables dictionary
        if name in self.variables:
            value = self.variables[name]
            # Cache the result if caching is enabled
            if self._cache_enabled:
                self._variable_cache[name] = value
            return value
        else:
            error_msg = AmharicErrorMessages.format_error_with_suggestion(
                'undefined_variable',
                AmharicErrorMessages.get_interpreter_error('undefined_variable', variable=name),
                variable=name
            )
            raise RuntimeError(error_msg)
    
    def set_variable(self, name: str, value: Any) -> None:
        """Set variable value with cache update"""
        self.variables[name] = value
        # Update cache if enabled
        if self._cache_enabled:
            self._variable_cache[name] = value
    
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
            error_msg = AmharicErrorMessages.format_error_with_suggestion(
                'undefined_function',
                AmharicErrorMessages.get_interpreter_error('undefined_function', function=node.name),
                function=node.name
            )
            raise RuntimeError(error_msg)
        
        function = self.functions[node.name]
        
        # Check argument count
        if len(node.arguments) != len(function.parameters):
            error_msg = AmharicErrorMessages.get_interpreter_error(
                'argument_count_mismatch',
                function=node.name,
                expected=len(function.parameters),
                actual=len(node.arguments)
            )
            raise RuntimeError(error_msg)
        
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
            error_msg = AmharicErrorMessages.format_error_with_suggestion(
                'index_out_of_range',
                AmharicErrorMessages.get_interpreter_error(
                    'index_error',
                    index=index,
                    length=len(list_value)
                )
            )
            raise IndexError(error_msg)
        
        return list_value[index]
    
    def execute_input(self, node: InputNode) -> str:
        """Execute input function: ግብአት() or ግብአት(prompt)"""
        if node.prompt:
            prompt_value = self.execute(node.prompt)
            if isinstance(prompt_value, str):
                user_input = input(prompt_value)
            else:
                user_input = input(str(prompt_value))
        else:
            user_input = input()
        
        return user_input
    
    def execute_string_method(self, node: StringMethodNode) -> Any:
        """Execute string methods"""
        string_value = self.execute(node.string)
        
        # Convert to string if not already (except for JOIN method)
        if node.method != 'JOIN' and not isinstance(string_value, str):
            string_value = str(string_value)
        
        if node.method == 'LENGTH':
            return len(string_value)
        
        elif node.method == 'UPPER':
            return string_value.upper()
        
        elif node.method == 'LOWER':
            return string_value.lower()
        
        elif node.method == 'SPLIT':
            if node.args:
                separator = self.execute(node.args[0])
                if not isinstance(separator, str):
                    separator = str(separator)
                return string_value.split(separator)
            else:
                return string_value.split()
        
        elif node.method == 'JOIN':
            if node.args:
                separator = self.execute(node.args[0])
                if not isinstance(separator, str):
                    separator = str(separator)
                # For JOIN, the string_value should be a list
                if isinstance(string_value, list):
                    return separator.join(str(item) for item in string_value)
                else:
                    raise ValueError("አገናኝ method requires a list as the first argument, got: " + str(type(string_value)))
            else:
                # Default join with space
                if isinstance(string_value, list):
                    return ' '.join(str(item) for item in string_value)
                else:
                    raise ValueError("አገናኝ method requires a list as the first argument")
        
        elif node.method == 'REPLACE':
            if len(node.args) >= 2:
                old_str = self.execute(node.args[0])
                new_str = self.execute(node.args[1])
                if not isinstance(old_str, str):
                    old_str = str(old_str)
                if not isinstance(new_str, str):
                    new_str = str(new_str)
                return string_value.replace(old_str, new_str)
            else:
                raise ValueError("ተክ method requires two arguments: old_string, new_string")
        
        else:
            raise ValueError(f"Unknown string method: {node.method}")

    def execute_builtin_function(self, node: BuiltinFunctionNode) -> Any:
        """Execute built-in functions"""
        # Evaluate all arguments first
        args = [self.execute(arg) for arg in node.args]
        
        if node.function == 'RANGE':
            if len(args) == 1:
                # range(stop)
                return list(range(int(args[0])))
            elif len(args) == 2:
                # range(start, stop)
                return list(range(int(args[0]), int(args[1])))
            elif len(args) == 3:
                # range(start, stop, step)
                return list(range(int(args[0]), int(args[1]), int(args[2])))
            else:
                raise ValueError("ወሰን function requires 1-3 arguments")
        
        elif node.function == 'TYPE':
            if len(args) != 1:
                raise ValueError("ዓይነት function requires exactly 1 argument")
            value = args[0]
            if isinstance(value, bool):
                return "boolean"
            elif isinstance(value, int):
                return "integer"
            elif isinstance(value, float):
                return "number"
            elif isinstance(value, str):
                return "string"
            elif isinstance(value, list):
                return "list"
            else:
                return "unknown"
        
        elif node.function == 'INT':
            if len(args) != 1:
                raise ValueError("ቁጥር function requires exactly 1 argument")
            try:
                return int(float(args[0]))  # Convert to float first to handle "3.14"
            except (ValueError, TypeError):
                raise ValueError(f"Cannot convert '{args[0]}' to integer")
        
        elif node.function == 'STR':
            if len(args) != 1:
                raise ValueError("ጽሑፍ function requires exactly 1 argument")
            return str(args[0])
        
        elif node.function == 'MAX':
            if len(args) < 1:
                raise ValueError("ከፍተኛ function requires at least 1 argument")
            try:
                return max(args)
            except TypeError:
                raise ValueError("ከፍተኛ function requires comparable values")
        
        elif node.function == 'MIN':
            if len(args) < 1:
                raise ValueError("ዠቅተኛ function requires at least 1 argument")
            try:
                return min(args)
            except TypeError:
                raise ValueError("ዠቅተኛ function requires comparable values")
        
        else:
            raise ValueError(f"Unknown built-in function: {node.function}")

    def execute_try_catch(self, node: TryCatchNode) -> Any:
        """Execute try-catch-finally block"""
        # Set flag to indicate we're in try-catch context
        old_flag = self.in_try_catch
        self.in_try_catch = True
        
        try:
            # Execute try block
            for statement in node.try_block:
                self.execute(statement)
        except Exception as e:
            # Find matching catch block
            caught = False
            for exception_type, variable_name, catch_block in node.catch_blocks:
                # Catch all exceptions if no specific type is specified, or if it matches
                # Remove quotes from exception_type if it's a string literal
                clean_exception_type = exception_type
                if isinstance(exception_type, str) and exception_type.startswith('"') and exception_type.endswith('"'):
                    clean_exception_type = exception_type[1:-1]
                
                if (exception_type is None or 
                    clean_exception_type == "Exception" or 
                    clean_exception_type == "RuntimeError" or
                    clean_exception_type == str(type(e).__name__)):
                    # Store exception in variable if specified
                    if variable_name:
                        self.variables[variable_name] = str(e)
                    
                    # Execute catch block
                    for statement in catch_block:
                        self.execute(statement)
                    caught = True
                    break
            
            # If no catch block matched, re-raise the exception
            if not caught:
                raise e
        
        finally:
            # Execute finally block if present
            if node.finally_block:
                for statement in node.finally_block:
                    self.execute(statement)
            
            # Restore the flag
            self.in_try_catch = old_flag
    
    def execute_throw(self, node: ThrowNode) -> Any:
        """Execute throw statement"""
        exception_value = self.execute(node.expression)
        raise Exception(str(exception_value))
    
    def execute_file_operation(self, node: FileOperationNode) -> Any:
        """Execute file operation"""
        import os
        
        filename = self.execute(node.filename)
        if not isinstance(filename, str):
            filename = str(filename)
        
        try:
            if node.operation == 'READ':
                # Read file content
                with open(filename, 'r', encoding='utf-8') as f:
                    return f.read()
            
            elif node.operation == 'WRITE':
                # Write content to file
                if node.content is None:
                    raise ValueError("ጻፍ operation requires content to write")
                content = self.execute(node.content)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(str(content))
                return True
            
            elif node.operation == 'APPEND':
                # Append content to file
                if node.content is None:
                    raise ValueError("ጨምር operation requires content to append")
                content = self.execute(node.content)
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(str(content))
                return True
            
            elif node.operation == 'EXISTS':
                # Check if file exists
                return os.path.exists(filename)
            
            elif node.operation == 'DELETE':
                # Delete file
                if os.path.exists(filename):
                    os.remove(filename)
                    return True
                else:
                    return False
            
            elif node.operation == 'LIST':
                # List directory contents
                if os.path.isdir(filename):
                    return os.listdir(filename)
                else:
                    raise ValueError(f"Directory not found: {filename}")
            
            elif node.operation == 'CREATE':
                # Create directory
                os.makedirs(filename, exist_ok=True)
                return True
            
            else:
                raise ValueError(f"Unknown file operation: {node.operation}")
                
        except Exception as e:
            raise RuntimeError(f"File operation failed: {str(e)}")
    
    def execute_dict(self, node: DictNode) -> Any:
        """Execute dictionary creation"""
        result = {}
        for key_node, value_node in node.pairs:
            key = self.execute(key_node)
            value = self.execute(value_node)
            result[key] = value
        return result
    
    def execute_dict_access(self, node: DictAccessNode) -> Any:
        """Execute dictionary access: dict[key]"""
        dict_value = self.execute(node.dict_expr)
        key = self.execute(node.key_expr)
        
        if not isinstance(dict_value, dict):
            error_msg = AmharicErrorMessages.get_interpreter_error(
                'type_error_dict_access',
                type=type(dict_value).__name__
            )
            raise TypeError(error_msg)
        
        if key not in dict_value:
            error_msg = AmharicErrorMessages.get_interpreter_error(
                'key_not_found',
                key=str(key)
            )
            raise KeyError(error_msg)
        
        return dict_value[key]
    
    def execute_dict_operation(self, node: DictOperationNode) -> Any:
        """Execute dictionary operation: ADD, REMOVE, HAS"""
        dict_value = self.execute(node.dict_expr)
        key = self.execute(node.key_expr)
        
        if not isinstance(dict_value, dict):
            error_msg = AmharicErrorMessages.get_interpreter_error(
                'type_error_dict_operation',
                type=type(dict_value).__name__
            )
            raise TypeError(error_msg)
        
        if node.operation == 'ADD':
            if node.value_expr is None:
                error_msg = AmharicErrorMessages.get_interpreter_error(
                    'add_requires_value'
                )
                raise ValueError(error_msg)
            value = self.execute(node.value_expr)
            dict_value[key] = value
            return True
        
        elif node.operation == 'REMOVE':
            if key in dict_value:
                del dict_value[key]
                return True
            else:
                return False
        
        elif node.operation == 'HAS':
            return key in dict_value
        
        else:
            error_msg = AmharicErrorMessages.get_interpreter_error(
                'unknown_dict_operation',
                operation=node.operation
            )
            raise ValueError(error_msg)


class ReturnException(Exception):
    """Exception used for return statements"""
    def __init__(self, value: Any):
        self.value = value
