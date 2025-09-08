#!/usr/bin/env python3
"""
Test suite for Ge-ez (ግእዝ) Amharic Programming Language
"""

import os
import sys
import unittest

# Add the geez module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa: E402

from geez.interpreter import GeEzInterpreter  # noqa: E402
from geez.lexer import GeEzLexer  # noqa: E402
from geez.parser import GeEzParser  # noqa: E402


class TestLexer(unittest.TestCase):
    """Test the lexical analyzer."""

    def setUp(self):
        self.lexer = GeEzLexer()

    def test_basic_tokens(self):
        """Test basic token recognition."""
        code = 'ማተም "ሰላም"'
        tokens = self.lexer.tokenize(code)

        self.assertEqual(
            len(tokens), 2
        )  # PRINT, STRING (EOF is not included in tokenize)
        self.assertEqual(tokens[0].type, "PRINT")
        self.assertEqual(tokens[1].type, "STRING")

    def test_variable_declaration(self):
        """Test variable declaration tokens."""
        code = 'አስተዋውቅ ስም = "አሊ"'
        tokens = self.lexer.tokenize(code)

        self.assertEqual(tokens[0].type, "VAR")
        self.assertEqual(
            tokens[1].type, "AMHARIC_ID"
        )  # Amharic identifiers are AMHARIC_ID
        self.assertEqual(tokens[2].type, "ASSIGN")
        self.assertEqual(tokens[3].type, "STRING")


class TestParser(unittest.TestCase):
    """Test the parser."""

    def setUp(self):
        self.lexer = GeEzLexer()
        self.parser = GeEzParser([])

    def test_print_statement(self):
        """Test print statement parsing."""
        code = 'ማተም "ሰላም"'
        tokens = self.lexer.tokenize(code)
        parser = GeEzParser(tokens)
        ast = parser.parse()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].__class__.__name__, "PrintNode")

    def test_variable_declaration(self):
        """Test variable declaration parsing."""
        code = 'አስተዋውቅ ስም = "አሊ"'
        tokens = self.lexer.tokenize(code)
        parser = GeEzParser(tokens)
        ast = parser.parse()

        self.assertEqual(len(ast), 1)
        self.assertEqual(ast[0].__class__.__name__, "AssignmentNode")


class TestInterpreter(unittest.TestCase):
    """Test the interpreter."""

    def setUp(self):
        self.interpreter = GeEzInterpreter()

    def test_print_execution(self):
        """Test print statement execution."""
        code = 'ማተም "ሰላም"'
        # This would normally capture output, but for now just test it doesn't crash
        try:
            self.interpreter.interpret(code)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Interpreter failed: {e}")

    def test_variable_assignment(self):
        """Test variable assignment and retrieval."""
        code = """
        አስተዋውቅ ስም = "አሊ"
        ማተም ስም
        """
        try:
            self.interpreter.interpret(code)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Interpreter failed: {e}")


class TestClassFeatures(unittest.TestCase):
    """Test class and OOP features."""

    def setUp(self):
        self.interpreter = GeEzInterpreter()

    def test_class_declaration(self):
        """Test class declaration parsing."""
        code = """
        ክፍል ሰው {
            ዘዴ መጀመሪያ(ራሱ, ስም) {
                ራሱ.ስም = ስም
            }
        }
        """
        try:
            self.interpreter.interpret(code)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Class declaration failed: {e}")

    def test_object_creation(self):
        """Test object creation."""
        code = """
        ክፍል ሰው {
            ዘዴ መጀመሪያ(ራሱ, ስም) {
                ራሱ.ስም = ስም
            }
        }
        አስተዋውቅ ሰው_1 = አዲስ ሰው("አሊ")
        """
        try:
            self.interpreter.interpret(code)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Object creation failed: {e}")


if __name__ == "__main__":
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestLexer))
    test_suite.addTest(unittest.makeSuite(TestParser))
    test_suite.addTest(unittest.makeSuite(TestInterpreter))
    test_suite.addTest(unittest.makeSuite(TestClassFeatures))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
