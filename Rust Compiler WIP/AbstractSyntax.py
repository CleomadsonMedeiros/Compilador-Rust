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

class Expression(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass

class Statement(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass

class Condition(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass

class VarDeclaration(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass

class VarAssignment(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass

class ExpressionAnd(Expression):
  def __init__(self, expression, condition):
      self.expression = expression
      self.condition = condition
  def accept(self, visitor):
      return visitor.visitExprAnd(self)
    
class ExpressionOr(Expression):
  def __init__(self, expression, condition):
      self.expression = expression
      self.condition = condition
  def accept(self, visitor):
      return visitor.visitExprOr(self)
    
class ExpressionNot(Expression):
  def __init__(self, condition):
      self.condition = condition
  def accept(self, visitor):
      return visitor.visitExprNot(self)

class ConditionTerm(Condition):
  def __init__(self, term):
      self.term = term
  def accept(self, visitor):
      return visitor.visitConditionTerm(self)
    
class ExpressionStatement(Expression):
  def __init__(self, expression):
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitExpressionStatement(self)
    
class VarDeclarationMutId(VarDeclaration):
  def __init__(self, id, expression):
      self.id = id
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitVarDeclarationMutId(self)

class VarDeclarationMutParam(VarDeclaration):
  def __init__(self, param, expression):
      self.param = param
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitVarDeclarationMutParam(self)

class VarDeclarationId(VarDeclaration):
  def __init__(self, id, expression):
      self.id = id
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitVarDeclarationId(self)

class VarDeclarationParam(VarDeclaration):
  def __init__(self, param, expression):
      self.param = param
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitVarDeclarationParam(self)

class VarAssignment(VarAssignment):
  def __init__(self, id, expression):
      self.id = id
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitVarAssignment(self)
    
class WhileStatement(Statement):
  def __init__(self, expression):
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitWhileStatement(self)

class ForStatement(Statement):
  def __init__(self, id, expression):
      self.id = id
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitForStatement(self)

class ReturnStatement(Statement):
  def __init__(self, expression):
      self.expression = expression
  def accept(self, visitor):
      return visitor.visitReturnStatement(self)
    
class StatementBlockStatement(Statement):
  def __init__(self, statementList):
      self.statements = statementList
  def accept(self, visitor):
      return visitor.visitStatementBlockStatement(self)
    
class ExpressionPlus(Expression):
  def __init__(self, expression, term):
      self.expression = expression
      self.term = term
  def accept(self, visitor):
      return visitor.visitExpressionPlus(self)
    
class ExpressionMinus(Expression):
  def __init__(self, expression, term):
      self.expression = expression
      self.term = term
  def accept(self, visitor):
      return visitor.visitExpressionMinus(self)
  
class ExpressionTerm(Expression):
  def __init__(self, term):
    self.term = term
  def accept(self, visitor):
    visitor.visitExpressionTerm(self)

class ExpressionRange(Expression):
  def __init__(self, expression, term):
    self.expression = expression
    self.term = term
  def accept(self, visitor):
    visitor.visitExpressionRange(self)
    
class Term(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class TermModulo(Term):
  def __init__(self, term, factor):
    self.term = term
    self.factor = factor
  def accept(self, visitor):
    visitor.visitTermModulo(self)

class TermTimes(Term):
  def __init__(self, term, factor):
    self.term = term
    self.factor = factor
  def accept(self, visitor):
    visitor.visitTermTimes(self)

class TermDivide(Term):
  def __init__(self, term, factor):
    self.term = term
    self.factor = factor
  def accept(self, visitor):
    visitor.visitTermDivide(self)

class TermFactor(Term):
  def __init__(self, factor):
    self.factor = factor
  def accept(self, visitor):
    visitor.visitTermFactor(self)

class Factor(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class FactorNumber(Factor):
  def __init__(self, number):
    self.number = number
  def accept(self, visitor):
    visitor.visitFactorNumber(self)

class FactorParen(Factor):
  def __init__(self, expression):
    self.expression = expression
  def accept(self, visitor):
    visitor.visitFactorParen(self)

class FactorBooleanTrue(Factor):
  def __init__(self, true):
    self.true = true
  def accept(self, visitor):
    visitor.visitFactorBooleanTrue(self)

class FactorBooleanFalse(Factor):
  def __init__(self, false):
    self.false = false
  def accept(self, visitor):
    visitor.visitFactorBooleanFalse(self)

class FactorBooleanFalse(Factor):
  def __init__(self, false):
    self.false = false
  def accept(self, visitor):
    visitor.visitFactorBooleanFalse(self)

class FactorID(Factor):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    visitor.visitFactorID(self)
