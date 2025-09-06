#!/usr/bin/env python3
"""
Ge-ez Command Line Interface
Provides a command-line interface for running Amharic programs
"""

import sys
import argparse
from .interpreter import GeEzInterpreter
from .lexer import GeEzLexer
from .parser import GeEzParser


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(description='Ge-ez: Amharic Programming Language')
    parser.add_argument('file', nargs='?', help='Amharic program file to execute')
    parser.add_argument('-i', '--interactive', action='store_true', 
                       help='Start interactive mode')
    
    args = parser.parse_args()
    
    interpreter = GeEzInterpreter()
    
    if args.interactive:
        print("Ge-ez Interactive Mode (ተገልጋይ ሁነት)")
        print("Type 'ውጣ' to exit")
        print("Type 'አፈጣጠር' to execute accumulated statements")
        
        accumulated_code = []
        while True:
            try:
                line = input("ግእዝ> ")
                if line.strip() == 'ውጣ':
                    break
                elif line.strip() == 'አፈጣጠር':
                    # Execute all accumulated statements
                    if accumulated_code:
                        full_code = '\n'.join(accumulated_code)
                        interpreter.interpret(full_code)
                        accumulated_code = []  # Clear after execution
                    else:
                        print("ምንም ኮድ አልተገኘም")
                elif line.strip():
                    # Add line to accumulated code
                    accumulated_code.append(line)
            except KeyboardInterrupt:
                print("\nውጣ")
                break
            except Exception as e:
                print(f"ስህተት: {e}")
    
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                code = f.read()
            interpreter.interpret(code)
        except FileNotFoundError:
            print(f"ፋይል አልተገኘም: {args.file}")
        except Exception as e:
            print(f"ስህተት: {e}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()