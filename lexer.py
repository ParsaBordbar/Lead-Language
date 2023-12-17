from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
        
    def create_tokens(self):
        
        #Print
        self.lexer.add('PRINT', r'chap')
        
        #Parenthesis
        self.lexer.add('OPEN_PARA', r'\(')
        self.lexer.add('CLOSE_PARA', r'\)')
        
        #Semi-colon
        self.lexer.add('SEMI_COLON', r'\;')
        
        #Dot
        self.lexer.add('Dot', r'\.')
        
        #Assignment 
        self.lexer.add('Assignment', r'\=')
        
        #Math Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        
        #Logical Operators
        self.lexer.add('LOGICAL_EQUAL', r'==')
        self.lexer.add('LOGICAL_HIGHER', r'>')
        self.lexer.add('LOGICAL_HIGHER_OR_EQUAL', r'>=')
        self.lexer.add('LOGICAL_LOWER', r'<')
        self.lexer.add('LOGICAL_LOWER_OR_EQUAL', r'<=')

        #Number
        self.lexer.add('NUMBER', r'\d+') 
        self.lexer.add('INT', r'sahih') 
        self.lexer.add('FLOAT', r'ashar') 
        
        #Spaces => should be ignored
        self.lexer.ignore('\s+')
        self.lexer.ignore('\t+')
        self.lexer.ignore('\n+')
        
        #CurlyBraces
        self.lexer.add('OPEN_BRACE', r'\{')
        self.lexer.add('CLOSE_BRACE', r'\}')
        
        #If statement(agar in this language)
        self.lexer.add('If', r'agar')
        
        #Identifier => variables 
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')
                
        #For Loops
        self.lexer.add('for', r'halgheh')

    def get_lexer(self):
        self.create_tokens()
        return self.lexer.build()       