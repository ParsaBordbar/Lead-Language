# Custom Compiler with RPly

This repository contains the implementation of a custom compiler built using the RPly library. The compiler is designed to parse and interpret a unique language with a variety of features.

## Lexer

The lexer, defined in `Lexer()`, is responsible for the lexical analysis of the source code. It breaks down the code into tokens, each representing a particular element or operator in the language.

Key features of the lexer include:
- Recognition of print statements, parentheses, semi-colons, dots, and assignment operators.
- Handling of mathematical operators such as addition, subtraction, multiplication, and division.
- Interpretation of logical operators including equality and comparison operators.
- Processing of numbers, including integers and floating-point numbers.
- Ignoring of whitespace characters (spaces, tabs, and newlines).
- Handling of curly braces, if statements, identifiers (variables), and for loops.

The lexer is built using the `create_tokens()` method and can be retrieved using the `get_lexer()` method.

## Parser

The parser, defined in `Parser()`, is responsible for the syntactic analysis of the tokenized source code. It constructs an Abstract Syntax Tree (AST) that represents the structure of the program.

Key features of the parser include:
- Parsing of print statements, expressions, and assignments.
- Handling of mathematical operations including addition, subtraction, multiplication, and division.
- Processing of parentheses for grouping expressions.
- Interpretation of numbers and identifiers.
  
The parser is built using the `parse()` method and can be retrieved using the `get_parser()` method.

## Abstract Syntax Tree (AST)

The AST is a tree representation of the structure of the source code. Each node in the tree denotes a construct occurring in the source code. The syntax tree captures the syntactic structure of the code, including the following nodes:

- `Program`: Represents the entire program.
- `VarDecl`: Represents variable declarations.
- `VarAssign`: Represents variable assignments.
- `IfStatement`: Represents if statements.
- `BinExpr`: Represents binary expressions.
- `IntLiteral` and `FloatLiteral`: Represent integer and floating-point literals, respectively.
- `VarRef`: Represents variable references.

This project serves as a robust foundation for further development and customization of the compiler to suit various programming paradigms and language specifications.
