from abc import abstractmethod
from abc import ABCMeta

def Expression(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

def Statement(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

def Condition(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

def VarDeclaration(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

def VarAssignment(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

def ExpressionAnd(Expression):
    def __init__(self, expression, condition):
        self.expression = expression
        self.condition = condition
    def accept(self, visitor):
        return visitor.visitExprAnd(self)
    
def ExpressionOr(Expression):
    def __init__(self, expression, condition):
        self.expression = expression
        self.condition = condition
    def accept(self, visitor):
        return visitor.visitExprOr(self)
    
def ExpressionNot(Expression):
    def __init__(self, condition):
        self.condition = condition
    def accept(self, visitor):
        return visitor.visitExprNot(self)

def ConditionTerm(Condition):
    def __init__(self, term):
        self.term = term
    def accept(self, visitor):
        return visitor.visitConditionTerm(self)
    
def ExpressionStatement(Expression):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitExpressionStatement(self)
    
def VarDeclarationMutId(VarDeclaration):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitVarDeclarationMutId(self)

def VarDeclarationMutParam(VarDeclaration):
    def __init__(self, param, expression):
        self.param = param
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitVarDeclarationMutParam(self)

def VarDeclarationId(VarDeclaration):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitVarDeclarationId(self)

def VarDeclarationParam(VarDeclaration):
    def __init__(self, param, expression):
        self.param = param
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitVarDeclarationParam(self)

def VarAssignment(VarAssignment):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitVarAssignment(self)
    
def WhileStatement(Statement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitWhileStatement(self)

def ForStatement(Statement):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitForStatement(self)

def ReturnStatement(Statement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitReturnStatement(self)
    
def StatementBlockStatement(Statement):
    def __init__(self, statementList):
        self.statements = statementList
    def accept(self, visitor):
        return visitor.visitStatementBlockStatement(self)
    
def ExpressionPlus(Expression):
    def __init__(self, expression, term):
        self.expression = expression
        self.term = term
    def accept(self, visitor):
        return visitor.visitExpressionPlus(self)