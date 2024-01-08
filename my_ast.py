# Define a base class for AST nodes
class Node:
    pass

# Define a class for program node
class Program(Node):
    def __init__(self, statements):
        self.statements = statements

# Define a class for variable declaration node
class VarDecl(Node):
    def __init__(self, name, type):
        self.name = name
        self.type = type

# Define a class for variable assignment node
class VarAssign(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Define a class for if statement node
class IfStatement(Node):
    def __init__(self, condition, then_body, else_body):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

# Define a class for binary expression node
class BinExpr(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

# Define a class for integer literal node
class IntLiteral(Node):
    def __init__(self, value):
        self.value = value

# Define a class for float literal node
class FloatLiteral(Node):
    def __init__(self, value):
        self.value = value

# Define a class for variable reference node
class VarRef(Node):
    def __init__(self, name):
        self.name = name