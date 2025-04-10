from AbstractVisitor import AbstractVisitor

class PrettyPrinter(AbstractVisitor):
  def visitProgram(self, program):
    program.main.accept(self)

  def visitMainFunction(self, mainFunction): 
    print('fn main()')
    mainFunction.blockStatement.accept(self)
  
  def visitStatementListStatement(self, statementListStatement):
    statementListStatement.statement.accept(self)

  def visitStatementListStatementStatementList(self, statementListStatementStatementList):
    statementListStatementStatementList.statement.accept(self)
    statementListStatementStatementList.statementList.accept(self)

  def visitDefFunction(self, defFunction):
    print('fn ', end='')
    print(defFunction.id)
    print('(', end='')
    defFunction.paramList.accept(self)
    print(') -> ', end='')
    defFunction.returnType.accept(self)
    defFunction.blockStatement.accept(self)

  def visitDefFunctionUnit(self, defFunctionUnit):
    print('fn ', end='')
    print(defFunctionUnit.id, end='')
    print('()')
    defFunctionUnit.blockStatement.accept(self)

  def visitFunctionCall(self, functionCall):
    print(functionCall.id, end='')
    print('()')

  def visitFunctionCallIdList(self, functionCallIdList):
    print(functionCallIdList.id, end='')
    print('(', end='')
    functionCallIdList.idList.accept(self)
    print(')', end='')
    print(';')

  def visitIdListIdComma(self, idListIdComma):
    print(idListIdComma.id, end='')
    print(', ', end='')
    idListIdComma.idList.accept(self)

  def visitIdListNumComma(self, idListNumComma):
    print(idListNumComma.num, end='')
    print(', ', end='')
    idListNumComma.idList.accept(self)

  def visitIdListFunctionCallComma(self, idListFunctionCallComma):
    idListFunctionCallComma.function.accept(self)
    print(', ', end='')
    idListFunctionCallComma.idList.accept(self)

  def visitIdListId(self, idListId):
    print(idListId.id, end='')

  def visitIdListNum(self, idListNum):
    print(idListNum.num,end='')

  def visitIdListFunctionCall(self, idListFunctionCall):
    idListFunctionCall.function.accept(self)

  def visitParamListParams(self, paramListParams):
    paramListParams.param.accept(self)
    print(', ', end='') 
    paramListParams.param_list.accept(self)
    
  def visitParamListParam(self, paramListParam):
    paramListParam.param.accept(self) 

  def visitParamIdI32(self, paramIdI32):
    print(paramIdI32.id, end='')
    print(': i32', end="")

  def visitParamIdF64(self, paramIdF64):
    print(paramIdF64.id, end='')
    print(': f64', end="")

  def visitParamIdBool(self, paramIdBool):
    print(paramIdBool.id, end='')
    print(': bool', end="")

  def visitStatementFunctionDef(self, statementFunctionDef):
    statementFunctionDef.function_def.accept(self)

  def visitStatementFunctionCall(self, statementFunctionCall):
    statementFunctionCall.function_call.accept(self)  

  def visitStatementExpressionStatement(self, statementExpressionStatement):
    statementExpressionStatement.expression_statement.accept(self) 
    
  def visitStatementVarDeclaration(self, statementVarDeclaration):
    statementVarDeclaration.var_declaration.accept(self)

  def visitStatementVarAssignment(self, statementVarAssignment):
    statementVarAssignment.var_assignment.accept(self) 
    
  def visitStatementIf(self, statementIf):
    print('if ', end='')
    statementIf.condition.accept(self)
    statementIf.block_statement.accept(self)

  def visitStatementIfElse(self, statementIfElse):
    print('if ', end='')
    statementIfElse.expression.accept(self)
    statementIfElse.block_statement.accept(self)
    statementIfElse.statement_else.accept(self)

  def visitStatementElseBlock(self, statementElseBlock):
    print('else ', end='')
    statementElseBlock.block_statement.accept(self)

  def visitStatementIfWithElse(self, statementIfWithElse):
    print('if ', end='')
    statementIfWithElse.expression.accept(self)
    statementIfWithElse.block_statement.accept(self)
    statementIfWithElse.statement_else.accept(self)

  def visitReturnTypeI32(self, returnTypeI32):
    print(returnTypeI32.id32, end='')  

  def visitReturnTypeF64(self, returnTypeF64):
    print(returnTypeF64.f64, end='')  

  def visitReturnTypeBool(self, returnTypeBool):
    print(returnTypeBool.bool, end='')  

  def visitStatementWhileStatement(self, whileStatement):
    whileStatement.while_statement.accept(self)
  
  def visitStatementReturnStatement(self, returnStatement):
    returnStatement.return_statement.accept(self)
    
  def visitStatementForStatement(self, forStatement):
    forStatement.for_statement.accept(self)    
  
  def visitStatementBlockStatement(self, blockStatement):
    blockStatement.block_statement.accept(self)
  
  def visitConditionNotEqual(self, conditionNotEqual):
    conditionNotEqual.expression.accept(self)
    print(' != ', end='')
    conditionNotEqual.condition.accept(self)
    
  def visitConditionGreaterEqual(self, conditionGreaterEqual):
    conditionGreaterEqual.expression.accept(self)
    print(' >= ', end='')
    conditionGreaterEqual.condition.accept(self)      
  
  def visitConditionLessEqual(self, conditionLessEqual):
    conditionLessEqual.expression.accept(self)
    print(' <= ', end='')
    conditionLessEqual.condition.accept(self)
  
  def visitConditionGreater(self, conditionGreater):
    conditionGreater.expression.accept(self)
    print(' > ', end='')
    conditionGreater.condition.accept(self)
    
  def visitConditionLess(self, conditionLess):
    conditionLess.expression.accept(self)
    print(' < ', end='')
    conditionLess.condition.accept(self)
        
  def visitConditionEquals(self, conditionEquals):
    conditionEquals.expression.accept(self)
    print(' == ', end='')
    conditionEquals.condition.accept(self)
    
  def visitExpressionAnd(self, expressionAnd):
    expressionAnd.expression.accept(self)
    print(' && ', end='')
    expressionAnd.condition.accept(self)
    
  def visitExpressionOr(self, expressionOr):
    expressionOr.expression.accept(self)
    print(' || ', end='')
    expressionOr.condition.accept(self)
    
  def visitExpressionNot(self, expressionNot):
    print('!', end='')
    expressionNot.condition.accept(self)
  
  def visitConditionTerm(self, conditionTerm):
    conditionTerm.term.accept(self)
  
  def visitExpressionStatement(self, expressionStatement):
    expressionStatement.expression.accept(self)
    print(';')   
  
  def visitVarDeclarationMutId(self, varDeclaration):
    print('let mut ', end='')
    print(varDeclaration.id, end='')
    print(' = ', end='')
    varDeclaration.expression.accept(self)
    print(';') 
  
  def visitVarDeclarationMutParam(self, varDeclarationMutParam):
    print('let mut ', end='')
    varDeclarationMutParam.param.accept(self)
    print(' = ', end='')
    varDeclarationMutParam.expression.accept(self)
    print(';')

  def visitVarDeclarationId(self, varDeclarationId):
    print('let ', end='')
    print(varDeclarationId.id, end="")
    print(' = ', end='')
    varDeclarationId.expression.accept(self)
    print(';')

  def visitVarDeclarationParam(self, varDeclarationParam):
    print('let ', end='')
    varDeclarationParam.param.accept(self)
    print(' = ', end='')
    varDeclarationParam.expression.accept(self)
    print(';')
  
  def visitVarAssignment(self, varAssignment):
    print(varAssignment.id, end="")
    print(' = ', end='')
    varAssignment.expression.accept(self)
    print(';')
  
  def visitWhileStatement(self, whileStatement):
    print('while ', end='')
    whileStatement.expression.accept(self)
    whileStatement.block_statement.accept(self)
  
  def visitForStatement(self, forStatement):
    print('for ', end='')
    print(forStatement.id, end='')
    print(' in ', end='')
    forStatement.expression.accept(self)
    forStatement.block_statement.accept(self)  
    
  def visitReturnStatement(self, returnStatement):
    print('return ', end='')
    returnStatement.expression.accept(self)
    print(';')   
  
  def visitBlockStatement(self, blockStatement):
    print('{')
    blockStatement.statementList.accept(self)
    print('}')
    
  def visitExpressionPlus(self, expressionPlus):
    expressionPlus.expression.accept(self)
    print(' + ', end='')
    expressionPlus.term.accept(self)
        
  def visitExpressionMinus(self, expressionMinus):
    expressionMinus.expression.accept(self)
    print(' - ', end='')
    expressionMinus.term.accept(self)
  
  def visitExpressionTerm(self, expressionTerm):
    expressionTerm.term.accept(self)

  def visitExpressionRange(self, expressionRange): 
    expressionRange.expression.accept(self)
    print(' .. ', end='')
    expressionRange.term.accept(self)

  def visitTermModulo(self, termModulo):
    termModulo.term.accept(self)
    print(' % ', end='')
    termModulo.factor.accept(self)
  
  def visitTermTimes(self, termTimes):
    termTimes.term.accept(self)
    print(' * ', end='')
    termTimes.factor.accept(self)      
  
  def visitTermDivide(self, termDivide):
    termDivide.term.accept(self)
    print(' / ', end='')
    termDivide.factor.accept(self)

  def visitTermFactor(self, termFactor):
    termFactor.factor.accept(self)   
    
  def visitFactorNumber(self, factorNumber):
    print(factorNumber.number, end="")
    
  def visitFactorParen(self, factorParen):
    print('(', end='')
    factorParen.expression.accept(self)
    print(')')
  
  def visitFactorBooleanTrue(self, factorBooleanTrue):
    print(factorBooleanTrue.true, end="")

  def visitFactorBooleanFalse(self, factorBooleanFalse):
    print(factorBooleanFalse.false, end="")
    
  def visitFactorID(self, factorID):
    print(factorID.id, end="")
  
  def visitError(self, error): pass