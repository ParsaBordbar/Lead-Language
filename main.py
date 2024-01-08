from lexer import Lexer
from parser import Parser

input_file = open('test.pb', 'r')
code = input_file.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(code)

print('Tokens: \n')
for token in tokens:
    print(token, '\n')
    
input_file.close()