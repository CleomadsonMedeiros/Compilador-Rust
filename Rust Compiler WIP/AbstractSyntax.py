from abc import abstractmethod
from abc import ABCMeta

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
  
class Statement(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

class FunctionDef(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

class FunctionCall(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

class IdList(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

class StatementListStatement(Statement):
  def __init__(self, statement):
    self.statement = statement
  def accept(self, visitor):
    return visitor.visitStatementListStatement(self)

class StatementListStatementStatementList(Statement):
  def __init__(self, statement, statementList):
    self.statement = statement
    self.statementList = statementList
  def accept(self, visitor):
    return visitor.visitStatementListStatementStatementList(self)

class DefFunction(FunctionDef):
  def __init__(self, id, paramList, returnType, blockStatement):
    self.id = id
    self.paramList = paramList
    self.returnType = returnType
    self.blockStatement = blockStatement
  def accept(self, visitor):
    return visitor.visitDefFunction(self)

class DefFunctionUnit(FunctionDef):
  def __init__(self, id, blockStatement):
    self.id = id
    self.blockStatement = blockStatement
  def accept(self, visitor):
    return visitor.visitDefFunctionUnit(self)

class FunctionCall(FunctionCall):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitFunctionCall(self)

class FunctionCallIdList(FunctionCall):
  def __init__(self, id, idList):
    self.id = id
    self.idList = idList
  def accept(self, visitor):
    return visitor.visitFunctionCallIdList(self)

class IdListIdComma(IdList):
  def __init__(self, id, idList):
    self.id = id
    self.idList = idList
  def accept(self, visitor):
    return visitor.visitIdListIdComma(self)
  
class IdListNumComma(IdList):
  def __init__(self, num, idList):
    self.num = num
    self.idList = idList
  def accept(self, visitor):
    return visitor.visitIdListNumComma(self)
  
class IdListFunctionCallComma(IdList):
  def __init__(self, function, idList):
    self.function = function
    self.idList = idList
  def accept(self, visitor):
    return visitor.visitIdListFunctionCallComma(self)

class IdListId(IdList):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitIdListId(self)
  
class IdListNum(IdList):
  def __init__(self, num):
    self.num = num
  def accept(self, visitor):
    return visitor.visitIdListNum(self)
  
class IdListFunctionCall(IdList):
  def __init__(self, function):
    self.function = function
  def accept(self, visitor):
    return visitor.visitIdListFunctionCall(self)

class Expression(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

class Condition(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

class VarDeclaration(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

class AbstractVarAssignment(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
    pass

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
  
class BlockStatement(Statement):
  def __init__(self, statement_list):
    self.statement_list = statement_list
  def accept(self, visitor):
    return visitor.visitBlockStatement(self)

class ConditionNotEqual(Condition):
  def __init__(self, expression, condition):
    self.expression = expression
    self.condition = condition
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

class VarAssignment(AbstractVarAssignment):
  def __init__(self, id, expression):
    self.id = id
    self.expression = expression
  def accept(self, visitor):
    return visitor.visitVarAssignment(self)
  
class StatementIf(Statement):
    def __init__(self, condition, block_statement):
        self.condition = condition
        self.block_statement = block_statement
    def accept(self, visitor):
        return visitor.visitStatementIf(self)
    
class StatementIfElse(Statement):
    def __init__(self, expression, block_statement, statement_else):
        self.condition = expression
        self.if_block = block_statement
        self.else_block = statement_else
    def accept(self, visitor):
        return visitor.visitStatementIfElse(self)
    
class StatementElseBlock(Statement):
    def __init__(self, block_statement):
        self.block = block_statement
    def accept(self, visitor):
        return visitor.visitStatementElseBlock(self)
    
class StatementElseIfWithElse(Statement):
    def __init__(self, expression, block_statement, statement_else):
        self.condition = expression
        self.block = block_statement
        self.else_block = statement_else
    def accept(self, visitor):
        return visitor.visitStatementElseIfWithElse(self)
    
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
    
class Term(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
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

class Factor(metaclass=ABCMeta):
  @abstractmethod
  def accept(self):
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
  
class Param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
   
class ParamIdI32(Param):
    def __init__(self, id):
       self.id = id
    def accept(self, visitor):
        return visitor.visitParamIdI32(self)
    
class ParamIdF64(Param):
   def __init__(self, id):
       self.id = id
   def accept(self, visitor):
        return visitor.visitParamIdF64(self)
   
class ParamIdBool(Param):
   def __init__(self, id):
      self.id = id
   def accept(self, visitor):
         return visitor.visitParamIdBool(self)
   
class ReturnType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ReturnTypeI32(ReturnType):
   def __init__(self, id32):
      self.id32 = id32
   def accept(self, visitor):
         return visitor.visitReturnTypeI32(self)
   
class ReturnTypeF64(ReturnType):
   def __init__(self, f64):
      self.f64 = f64
   def accept(self, visitor):
      return visitor.visitReturnTypeF64(self)
   
class ReturnTypeBool(ReturnType):
   def __init__(self, bool):
      self.bool = bool
   def accept(self, visitor):
         return visitor.visitReturnTypeBool(self)
   
class ParamListParams(Param):
   def __init__(self, param, param_list):
      self.param = param
      self.param_list = param_list
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