from abc import abstractmethod
from abc import ABCMeta


class Program():
  def __init__(self, main):
    self.main = main
  def accept(self, visitor):
    visitor.visitProgram(self)

class MainF():
  def __init__(self, blockStatement):
    self.blockStatement = blockStatement
  def accept(self, visitor):
    visitor.visitMainFunction(self)

class StatementListStatement():
  def __init__(self, statement):
    self.statement = statement
  def accept(self, visitor):
    visitor.visitStatementListStatement(self)

class StatementList():
  def __init__(self, statement, statementList):
    self.statement = statement
    self.statementList = statementList
  def accept(self, visitor):
    visitor.visitStatementList(self)

class DefFunction():
  def __init__(self, id, paramList, returnType, blockStatement):
    self.id = id
    self.paramList = paramList
    self.returnType = returnType
    self.blockStatement = blockStatement
  def accept(self, visitor):
    visitor.visitDefFunction(self)

class DefFunctionUnit():
  def __init__(self, id, blockStatement):
    self.id = id
    self.blockStatement = blockStatement
  def accept(self, visitor):
    visitor.visitDefFunctionUnit(self)

class FunctionCall():
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    visitor.visitFunctionCall(self)

class FunctionCallIdList():
  def __init__(self, id, idList):
    self.id = id
    self.idList = idList
  def accept(self, visitor):
    visitor.visitFunctionCallIdList(self)

class IdListIdNumIdList():
  def __init__(self, idNum, idList):
    self.idNum = idNum
    self.idList = idList
  def accept(self, visitor):
    visitor.visitIdListIdNumIdList()

class IdListIdNumFunctionCall():
  def __init__(self, idNumFunctionCall):
    self.idNumFunctionCall = idNumFunctionCall
  def accept(self, visitor):
    visitor.visitIdListIdNumFunctionCall(self)

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