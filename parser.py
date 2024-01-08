from rply import ParserGenerator
from lexer import Lexer

class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['PRINT', 'OPEN_PARA', 'CLOSE_PARA', 'SEMI_COLON', 'DOT', 'ASSIGNMENT', 'SUM', 'SUB', 'MUL', 'DIV',
             'LOGICAL_EQUAL', 'LOGICAL_HIGHER', 'LOGICAL_HIGHER_OR_EQUAL', 'LOGICAL_LOWER', 'LOGICAL_LOWER_OR_EQUAL',
             'NUMBER', 'INT_VALUE', 'FLOAT_VALUE', 'INT', 'FLOAT', 'OPEN_BRACE', 'CLOSE_BRACE', 'IF', 'IDENTIFIER', 'FOR']
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PARA expression CLOSE_PARA SEMI_COLON')
        def program(p):
            return Program(p[2])

        @self.pg.production('program : expression SEMI_COLON')
        def program_expr(p):
            return p[0]

        @self.pg.production('expression : IDENTIFIER ASSIGNMENT expression SEMI_COLON')
        def expression_assignment(p):
            return VarAssign(p[0].getstr(), p[2])

        @self.pg.production('expression : expression SUM expression SEMI_COLON')
        @self.pg.production('expression : expression SUB expression SEMI_COLON')
        @self.pg.production('expression : expression MUL expression SEMI_COLON')
        @self.pg.production('expression : expression DIV expression SEMI_COLON')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return BinExpr(left, '+', right)
            elif operator.gettokentype() == 'SUB':
                return BinExpr(left, '-', right)
            elif operator.gettokentype() == 'MUL':
                return BinExpr(left, '*', right)
            elif operator.gettokentype() == 'DIV':
                return BinExpr(left, '/', right)

        @self.pg.production('expression : OPEN_PARA expression CLOSE_PARA')
        def expression_paren(p):
            return p[1]

        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return IntLiteral(int(p[0].getstr()))

        @self.pg.production('expression : IDENTIFIER SEMI_COLON')
        def expression_name(p):
            return VarRef(p[0].getstr())



    def get_parser(self):
        return self.pg.build()
