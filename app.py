import argparse, sys
from lexer import (
    Lexer,
    Parser,
    Interpreter,
    SemanticAnalyzer,
    LexerError,
    ParserError,
    SemanticError,
)


def main():
    parser = argparse.ArgumentParser(description="PyPascal")
    parser.add_argument("inputfile", help="Pascal source file")
    parser.add_argument(
        "--scope",
        help="Print scope information",
        action="store_true",
    )
    parser.add_argument(
        "--stack",
        help="Print call stack",
        action="store_true",
    )
    args = parser.parse_args()

    global _SHOULD_LOG_SCOPE, _SHOULD_LOG_STACK
    _SHOULD_LOG_SCOPE, _SHOULD_LOG_STACK = args.scope, args.stack

    text = open(args.inputfile, "r").read()

    lexer = Lexer(text)
    try:
        parser = Parser(lexer)
        tree = parser.parse()
    except (LexerError, ParserError) as e:
        print(e.message)
        sys.exit(1)

    semantic_analyzer = SemanticAnalyzer()
    try:
        semantic_analyzer.visit(tree)
    except SemanticError as e:
        print(e.message)
        sys.exit(1)

    interpreter = Interpreter(tree)
    interpreter.interpret()


if __name__ == "__main__":
    main()
