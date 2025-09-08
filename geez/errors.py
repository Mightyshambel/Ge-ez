"""
Amharic Error Messages for Ge-ez Programming Language
Provides comprehensive error messages in Amharic with context and suggestions
"""

from typing import Dict, Any, Optional


class AmharicErrorMessages:
    """Centralized Amharic error message system"""
    
    # Lexer Error Messages
    LEXER_ERRORS = {
        'unknown_character': "ያልታወቀ ቁምፊ '{char}' በመስመር {line}፣ አምድ {column}",
        'unexpected_eof': "ያልተጠበቀ የፋይል መጨረሻ",
        'invalid_number': "የተሳሳተ ቁጥር '{number}'",
        'unclosed_string': "ያልተዘጋ ገላጭ '{string}'",
        'unclosed_comment': "ያልተዘጋ አስተያየት",
    }
    
    # Parser Error Messages
    PARSER_ERRORS = {
        'unexpected_token': "ያልተጠበቀ ቶከን '{token}' በመስመር {line}፣ አምድ {column}",
        'expected_token': "{expected} ይጠበቅ ነበር በመስመር {line}፣ አምድ {column}",
        'expected_identifier': "የተለዋዋጭ ስም ይጠበቅ ነበር በመስመር {line}፣ አምድ {column}",
        'expected_expression': "ገለጻ ይጠበቅ ነበር በመስመር {line}፣ አምድ {column}",
        'expected_statement': "መግለጫ ይጠበቅ ነበር በመስመር {line}፣ አምድ {column}",
        'unclosed_brace': "ያልተዘጋ ቅንፍ '{' በመስመር {line}፣ አምድ {column}",
        'unclosed_paren': "ያልተዘጋ ቅንፍ '(' በመስመር {line}፣ አምድ {column}",
        'unclosed_bracket': "ያልተዘጋ ቅንፍ '[' በመስመር {line}፣ አምድ {column}",
        'missing_assignment': "የመመደቢያ ምልክት '=' ይጠበቅ ነበር",
        'missing_semicolon': "የመስመር መጨረሻ ';' ይጠበቅ ነበር",
    }
    
    # Interpreter Error Messages
    INTERPRETER_ERRORS = {
        'undefined_variable': "ያልተገለጸ ተለዋዋጭ: '{variable}'",
        'undefined_function': "ያልተገለጸ ተግባር: '{function}'",
        'division_by_zero': "በዜሮ መከፋፈል አይቻልም",
        'type_error': "የተሳሳተ ዓይነት: {message}",
        'index_error': "የዝርዝር መረጃ {index} ከወሰን ውጭ (ዝርዝሩ {length} አካላት አሉት)",
        'value_error': "የተሳሳተ እሴት: {message}",
        'runtime_error': "የመስራት ስህተት: {message}",
        'file_not_found': "ፋይል አልተገኘም: '{filename}'",
        'permission_denied': "ፈቃድ ተሰጥቷል: '{filename}'",
        'file_exists': "ፋይል አስቀድሞ አለ: '{filename}'",
        'directory_not_found': "ዲሬክቶሪ አልተገኘም: '{directory}'",
        'invalid_operation': "የማይቻል ስራ: {operation}",
        'argument_count_mismatch': "ተግባር '{function}' {expected} ነጋሪ እሴቶች ይጠበቃል፣ {actual} ተቀበለ",
        'invalid_iteration': "በ {type} ላይ መድገም አይቻልም",
        'unknown_operator': "ያልታወቀ ኦፔሬተር: '{operator}'",
        'unknown_node_type': "ያልታወቀ የኖድ ዓይነት: {type}",
        'file_operation_failed': "የፋይል ስራ አልተሳካም: {message}",
        'string_method_error': "የገላጭ ዘዴ ስህተት: {message}",
        'builtin_function_error': "የተለዋዋጭ ተግባር ስህተት: {message}",
        'type_error_dict_access': "ንብብ አይነት እንደ ንብብ መጠቀም አለበት፣ {type} አይደለም",
        'key_not_found': "ቁልፍ '{key}' በንብብ ውስጥ አልተገኘም",
        'type_error_dict_operation': "ንብብ አይነት እንደ ንብብ መጠቀም አለበት፣ {type} አይደለም",
        'add_requires_value': "ጨምር_ወደ ክዋኔ እሴት ያስፈልገዋል",
        'unknown_dict_operation': "ያልታወቀ የንብብ ክዋኔ: {operation}",
        'undefined_class': "ያልተገለጸ ክፍል: '{class_name}'",
        'type_error_property_access': "ንብብ አይነት እንደ ንብብ መጠቀም አለበት፣ {type} አይደለም",
        'property_not_found': "ባህሪ '{property}' አልተገኘም",
        'type_error_method_call': "ንብብ አይነት እንደ ንብብ መጠቀም አለበት፣ {type} አይደለም",
        'invalid_object': "የማይቻል ነገር: {object}",
        'method_not_found': "ዘዴ '{method}' በክፍል '{class_name}' ውስጥ አልተገኘም",
    }
    
    # Context-aware suggestions
    SUGGESTIONS = {
        'undefined_variable': "ተለዋዋጭ '{variable}' ከመጠቀም በፊት በ 'አስተዋውቅ' አስተዋውቀው",
        'undefined_function': "ተግባር '{function}' ከመጠቀም በፊት በ 'ተግባር' አስተዋውቀው",
        'missing_assignment': "ተለዋዋጭ ከመመደብ በፊት '=' ምልክት ያስገቡ",
        'unclosed_brace': "የተከፈተ '{' ቅንፍ በ '}' ይዝጉ",
        'unclosed_paren': "የተከፈተ '(' ቅንፍ በ ')' ይዝጉ",
        'unclosed_bracket': "የተከፈተ '[' ቅንፍ በ ']' ይዝጉ",
        'division_by_zero': "በዜሮ ከመከፋፈል በፊት ቁጥሩ ዜሮ እንዳልሆነ ያረጋግጡ",
        'index_out_of_range': "የዝርዝር መረጃ ከዝርዝሩ ርዝመት ያነሰ መሆኑን ያረጋግጡ",
    }
    
    @staticmethod
    def get_lexer_error(error_type: str, **kwargs) -> str:
        """Get lexer error message in Amharic"""
        template = AmharicErrorMessages.LEXER_ERRORS.get(error_type, "ያልታወቀ ስህተት: {error_type}")
        return template.format(**kwargs)
    
    @staticmethod
    def get_parser_error(error_type: str, **kwargs) -> str:
        """Get parser error message in Amharic"""
        template = AmharicErrorMessages.PARSER_ERRORS.get(error_type, "ያልታወቀ ስህተት: {error_type}")
        return template.format(**kwargs)
    
    @staticmethod
    def get_interpreter_error(error_type: str, **kwargs) -> str:
        """Get interpreter error message in Amharic"""
        template = AmharicErrorMessages.INTERPRETER_ERRORS.get(error_type, "ያልታወቀ ስህተት: {error_type}")
        return template.format(**kwargs)
    
    @staticmethod
    def get_suggestion(error_type: str, **kwargs) -> str:
        """Get helpful suggestion for error"""
        template = AmharicErrorMessages.SUGGESTIONS.get(error_type, "")
        return template.format(**kwargs) if template else ""
    
    @staticmethod
    def format_error_with_suggestion(error_type: str, error_message: str, **kwargs) -> str:
        """Format error message with suggestion"""
        suggestion = AmharicErrorMessages.get_suggestion(error_type, **kwargs)
        if suggestion:
            return f"ስህተት: {error_message}\n💡 ምክር: {suggestion}"
        return f"ስህተት: {error_message}"
    
    @staticmethod
    def get_context_info(line: int, column: int, filename: Optional[str] = None) -> str:
        """Get context information for error"""
        context = f"በመስመር {line}፣ አምድ {column}"
        if filename:
            context = f"በፋይል '{filename}' {context}"
        return context
