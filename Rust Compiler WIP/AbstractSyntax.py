from abc import abstractmethod
from abc import ABC

class Program():
  def __init__(self, main):
    self.main = main
  def accept(self, visitor):
    return visitor.visitProgram(self)

class MainF():
  def __init__(self, blockStatement):
    self.blockStatement = blockStatement
  def accept(self, visitor):
    return visitor.visitMainFunction(self)

class StatementListStatement():
  def __init__(self, statement):
    self.statement = statement
  def accept(self, visitor):
    return visitor.visitStatementListStatement(self)

class StatementList():
  def __init__(self, statement, statementList):
    self.statement = statement
    self.statementList = statementList
  def accept(self, visitor):
    return visitor.visitStatementList(self)

class DefFunction():
  def __init__(self, id, paramList, returnType, blockStatement):
    self.id = id
    self.paramList = paramList
    self.returnType = returnType
    self.blockStatement = blockStatement
  def accept(self, visitor):
    return visitor.visitDefFunction(self)

class DefFunctionUnit():
  def __init__(self, id, blockStatement):
    self.id = id
    self.blockStatement = blockStatement
  def accept(self, visitor):
    return visitor.visitDefFunctionUnit(self)

class FunctionCall():
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitFunctionCall(self)

class FunctionCallIdList():
  def __init__(self, id, idList):
    self.id = id
    self.idList = idList
  def accept(self, visitor):
    return visitor.visitFunctionCallIdList(self)

class IdListIdNumIdList():
  def __init__(self, idNum, idList):
    self.idNum = idNum
    self.idList = idList
  def accept(self, visitor):
    return visitor.visitIdListIdNumIdList()

class IdListIdNumFunctionCall():
  def __init__(self, idNumFunctionCall):
    self.idNumFunctionCall = idNumFunctionCall
  def accept(self, visitor):
    return visitor.visitIdListIdNumFunctionCall(self)

class Expression(ABC):
  @abstractmethod
  def print(self):
    pass

class Statement(ABC):
  @abstractmethod
  def print(self):
    pass

class Condition(ABC):
  @abstractmethod
  def print(self):
    pass

class VarDeclaration(ABC):
  @abstractmethod
  def print(self):
    pass

class VarAssignment(ABC):
  @abstractmethod
  def print(self):
    pass

class StatementElseIf(Statement):
  def __init__(self, expression, statement_else_if):
    self.expression = expression
    self.statement_else_if = statement_else_if
  def accept(self, visitor):
    return visitor.visitStatementElseIf(self)
  
class StatementElseIfBlock(Statement):
  def __init__(self, expression, block_statement):
    self.expression = expression
    self.block_statement = block_statement
  def accept(self, visitor):
    return visitor.visitStatementElseIfBlock(self)
  
class StatementIfWithElse(Statement):
  def __init__(self, expression, block_statement, statement_else):
    self.expression = expression
    self.block_statement = block_statement
    self.statement_else = statement_else
  def accept(self, visitor):
    return visitor.visitStatementIfWithElse(self)
  
class StatementWhileStatement(Statement):
  def __init__(self, while_statement):
    self.while_statement = while_statement
  def accept(self, visitor):
    return visitor.visitStatementWhileStatement(self)

class StatementReturnStatement(Statement):
  def __init__(self, return_statement):
    self.return_statement = return_statement
  def accept(self, visitor):
    return visitor.visitStatementReturnStatement(self)
  
class StatementForStatement(Statement):
  def __init__(self, for_statement):
    self.for_statement = for_statement
  def accept(self, visitor):
    return visitor.visitStatementForStatement(self)
  
class StatementBlockStatement(Statement):
  def __init__(self, block_statement):
    self.block_statement = block_statement
  def accept(self, visitor):
    return visitor.visitStatementBlockStatement(self)

class ConditionNotEqual(Condition):
  def __init__(self, expression, condition):
    self.expression = expression
    self.term = condition
  def accept(self, visitor):
    return visitor.visitConditionNotEqual(self)

class ConditionGreaterEqual(Condition):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitConditionGreaterEqual(self)
  
class ConditionLessEqual(Condition):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitConditionLessEqual(self)
  
class ConditionGreater(Condition):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitConditionGreater(self)
  
class ConditionLess(Condition):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitConditionLess(self)
  
class ConditionEquals(Condition):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitConditionEquals(self)

class ExpressionAnd(Expression):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitExpressionAnd(self)
    
class ExpressionOr(Expression):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitExpressionOr(self)
    
class ExpressionNot(Expression):
  def __init__(self, condition):
    self.condition = condition
  def accept(self, visitor):
    return visitor.visitExpressionNot(self)

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
  def __init__(self, expression, block_statement):
    self.expression = expression
    self.block_statement = block_statement
  def accept(self, visitor):
    return visitor.visitWhileStatement(self)

class ForStatement(Statement):
  def __init__(self, id, expression, block_statement):
    self.id = id
    self.expression = expression
    self.block_statement = block_statement
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
    return visitor.visitExpressionTerm(self)

class ExpressionRange(Expression):
  def __init__(self, expression, term):
    self.expression = expression
    self.term = term
  def accept(self, visitor):
    return visitor.visitExpressionRange(self)
    
class Term(ABC):
  @abstractmethod
  def print(self):
    pass

class TermModulo(Term):
  def __init__(self, term, factor):
    self.term = term
    self.factor = factor
  def accept(self, visitor):
    return visitor.visitTermModulo(self)

class TermTimes(Term):
  def __init__(self, term, factor):
    self.term = term
    self.factor = factor
  def accept(self, visitor):
    return visitor.visitTermTimes(self)

class TermDivide(Term):
  def __init__(self, term, factor):
    self.term = term
    self.factor = factor
  def accept(self, visitor):
    return visitor.visitTermDivide(self)

class TermFactor(Term):
  def __init__(self, factor):
    self.factor = factor
  def accept(self, visitor):
    return visitor.visitTermFactor(self)

class Factor(ABC):
  @abstractmethod
  def print(self):
    pass

class FactorNumber(Factor):
  def __init__(self, number):
    self.number = number
  def accept(self, visitor):
    return visitor.visitFactorNumber(self)

class FactorParen(Factor):
  def __init__(self, expression):
    self.expression = expression
  def accept(self, visitor):
    return visitor.visitFactorParen(self)

class FactorBooleanTrue(Factor):
  def __init__(self, true):
    self.true = true
  def accept(self, visitor):
    return visitor.visitFactorBooleanTrue(self)

class FactorBooleanFalse(Factor):
  def __init__(self, false):
    self.false = false
  def accept(self, visitor):
    return visitor.visitFactorBooleanFalse(self)

class FactorBooleanFalse(Factor):
  def __init__(self, false):
    self.false = false
  def accept(self, visitor):
    return visitor.visitFactorBooleanFalse(self)

class FactorID(Factor):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitFactorID(self)
