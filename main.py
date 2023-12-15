from lexer import Lexer

text_input = """
chap(4 / 4 * 2);
ashar sahih
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)
