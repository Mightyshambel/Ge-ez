#!/usr/bin/env python3
"""
Ge-ez - Amharic Programming Language
Main entry point for the application
"""

from geez.interpreter import GeEzInterpreter
from geez.cli import main as cli_main


def main():
    """Main function"""
    print("Welcome to Ge-ez! (ጌዝ አማርኛ የፕሮግራሚንግ ቋንቋ)")
    print("Amharic Programming Language")
    print("=" * 40)
    
    # Run the CLI
    cli_main()


if __name__ == "__main__":
    main()
