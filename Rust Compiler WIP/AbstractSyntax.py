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
#RENNE  
class Param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
   
class ParamIdI32(Param):
    def __init__(self, idname32, typename32):
       self.idname = idname32
       self.typename = typename32
    
    def accept(self, visitor):
        return visitor.visitParamIdI32(self)
    
class ParamIdI64(Param):
   def __init__(self, idname64, typename64):
       self.idname = idname64
       self.typename = typename64
   def accept(self, visitor):
        return visitor.visitParamIdI64(self)
   
class ParamIdBool(Param):
   def __init__(self, idnamebool, typenamebool):
      self.idname = idnamebool
      self.typename = typenamebool
   def accept(self, visitor):
         return visitor.visitParamIdBool(self)
   
class ReturnType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ReturnTypeI32(ReturnType):
   def __init__(self, typename32):
      self.typename = typename32
   def accept(self, visitor):
         return visitor.visitReturnTypeI32(self)
   
class ReturnTypeF64(ReturnType):
   def __init__(self, typename64):
      self.typename = typename64
   def accept(self, visitor):
      return visitor.visitReturnTypeF64(self)
   
class ReturnTypeBool(ReturnType):
   def __init__(self, typenamebool):
      self.typename = typenamebool
   def accept(self, visitor):
         return visitor.visitReturnTypeBool(self)
   
class ParamListParams(Param):
   def __init__(self, param, paramlist):
      self.paramlist = param
      self.paramlist = paramlist
   def accept(self, visitor):
         return visitor.visitParamListParams(self)
   
class ParamListParam(Param):
   def __init__(self, param):
      self.param = param
   def accept(self, visitor):
         return visitor.visitParamListParam(self)
   

class StatementFunctionDef(Statement):
    def __init__(self, function_def):
        self.function_def = function_def
    def accept(self, visitor):
        return visitor.visitStatementFunctionDef(self)
    
class StatementFunctionCall(Statement):
   def __init__(self, function_call):
      self.function_call = function_call
   def accept(self, visitor):
         return visitor.visitStatementFunctionCall(self)
   
class StatementExpressionStatement(Statement):
   def __init__(self, expression_statement):
      self.expression_statement = expression_statement
   def accept(self, visitor):
         return visitor.visitStatementExpressionStatement(self)
   
class StatementVarDeclaration(Statement):
   def __init__(self, var_declaration):
      self.var_declaration = var_declaration
   def accept(self, visitor):
         return visitor.visitStatementVarDeclaration(self)

class StatementVarAssignment(Statement):
   def __init__(self, var_assignment):
      self.var_assignment = var_assignment
   def accept(self, visitor):
         return visitor.visitStatementVarAssignment(self)
   
class StatementIf(Statement):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block
    def accept(self, visitor):
        return visitor.visitStatementIf(self)
    
class StatementIfElse(Statement):
    def __init__(self, condition, blockLeft, statemElse):
        self.condition = condition
        self.if_block = blockLeft
        self.else_block = statemElse
    def accept(self, visitor):
        return visitor.visitStatementIfElse(self)
    
class StatementElseBlock(Statement):
    def __init__(self, blockStatem):
        self.block = blockStatem
    def accept(self, visitor):
        return visitor.visitStatementElseBlock(self)