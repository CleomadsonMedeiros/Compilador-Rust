from AbstractVisitor import AbstractVisitor

class PrettyPrinter(AbstractVisitor):
  def visitProgram(self, program): pass

  def visitMainFunction(self, mainFunction): pass
  
  def visitStatementListStatement(self, statementListStatement): pass

  def visitStatementList(self, statementList): pass

  def visitDefFunction(self, defFunction): pass

  def visitDefFunctionUnit(self, defFunctionUnit): pass

  def visitFunctionCallSemicolon(self, functionCallSemicolon): pass

  def visitFunctionCallIdListSemicolon(self, functionCallIdListSemicolon): pass

  def visitFunctionCall(self, functionCall): pass

  def visitFunctionCallIdList(self, functionCallIdList): pass

  def visitIdListIdComma(self, idListIdComma): pass

  def visitIdListNumberComma(self, idListNumberComma): pass

  def visitIdListId(self, idListIdComma): pass

  def visitIdListNumber(self, idListNumber): pass

  def visitIdListFunctionCall(self, idListFunctionCall): pass

  def visitParamListParams(self, paramListParams):
    paramListParams.param.accept(self)
    print(', ', end='') 
    paramListParams.paramlist.accept(self)
    
  def visitParamListParam(self, paramListParam):
    paramListParam.param.accept(self) 

  def visitParamIdI32(self, paramIdI32):
    print(paramIdI32.ID, end='')
    print(': i32')
    paramIdI32.I32.accept(self)

  def visitParamIdF64(self, paramIdF64):
    paramIdF64.ID.accept(self)
    print(': f64')
    paramIdF64.F64.accept(self)

  def visitParamIdBool(self, paramIdBool):
    paramIdBool.ID.accept(self)
    print(': bool')
    paramIdBool.BOOL.accept(self)

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
    statementIf.expression.accept(self)  
    print(' {') 
    statementIf.block_statement.accept(self) 
    print('}') 

  def visitStatementIfElse(self, statementIfElse):
    print('if ', end='')
    statementIfElse.expression.accept(self)
    print(' {')
    statementIfElse.block_statement.accept(self)
    print('}')
    print('else {') 
    statementIfElse.statement_else.accept(self)
    print('}')

  def visitStatementElseBlock(self, statementElseBlock):
    print('else {', end='') 
    statementElseBlock.block_statement.accept(self) 
    print('}') 

  def visitReturnTypeI32(self, returnTypeI32):
    print(returnTypeI32.ID32)  

  def visitReturnTypeF64(self, returnTypeF64):
    print(returnTypeF64.F64)  

  def visitReturnTypeBool(self, returnTypeBool):
    print(returnTypeBool.BOOL)  

  def visitStatementElseIf(self, statementElseIf): pass

  def visitStatementElseIfBlock(self, statementElseIfBlock): pass

  def visitStatementIfWithElse(self, statementIfWithElse): pass

  def visitStatementWhileStatement(self, whileStatement): pass
  
  def visitStatementReturnStatement(self, returnStatement): pass
    
  def visitStatementForStatement(self, forStatement): pass      
  
  def visitStatementBlockStatement(self, blockStatement): pass
  
  def visitConditionNotEqual(self, notEqual): pass
    
  def visitConditionGreaterEqual(self, greaterEqual): pass      
  
  def visitConditionLessEqual(self, lessEqual): pass
  
  def visitConditionGreater(self, greater): pass
    
  def visitConditionLess(self, less): pass
        
  def visitConditionEquals(self, equals): pass
    
  def visitExpressionAnd(self, expressionAnd):
    expressionAnd.expression.accept(self)
    print(' && ', end='')
    expressionAnd.term.accept(self)
    
  def visitExpressionOr(self, expressionOr):
    expressionOr.expression.accept(self)
    print(' || ', end='')
    expressionOr.term.accept(self)
    
  def visitExpressionNot(self, expressionNot):
    print('!', end='')
    expressionNot.expression.accept(self)
  
  def visitConditionTerm(self, conditionTerm):
    conditionTerm.term.accept(self)
  
  def visitExpressionStatement(self, expressionStatement):
    expressionStatement.expression.accept(self)
    print(';')   
  
  def visitVarDeclarationMutId(self, varDeclaration):
    print('let mut ', end='')
    varDeclaration.id.accept(self)
    print(' = ', end='')
    varDeclaration.expression.accept(self)
    print(';', end='') 
  
  def visitVarDeclarationMutParam(self, varDeclarationMutParam):
    print('let mut ', end='')
    varDeclarationMutParam.param.accept(self)
    print(' = ', end='')
    varDeclarationMutParam.expression.accept(self)
    print(';', end='')

  def visitVarDeclarationId(self, varDeclarationId):
    print('let ', end='')
    varDeclarationId.id.accept(self)
    print(' = ', end='')
    varDeclarationId.expression.accept(self)
    print(';', end='')

  def visitVarDeclarationParam(self, varDeclarationParam):
    print('let ', end='')
    varDeclarationParam.param.accept(self)
    print(' = ', end='')
    varDeclarationParam.expression.accept(self)
    print(';', end='')
  
  def visitVarAssignment(self, varAssignment):
    varAssignment.id.accept(self)
    print(' = ', end='')
    varAssignment.expression.accept(self)
    print(';', end='')
  
  def visitWhileStatement(self, whileStatement):
    print('while ', end='')
    whileStatement.expression.accept(self)
    whileStatement.blockStatement.accept(self)
  
  def visitForStatement(self, forStatement):
    print('for ', end='')
    forStatement.id.accept(self)
    print(' in ', end='')
    forStatement.expression.accept(self)
    forStatement.blockStatement.accept(self)  
    
  def visitReturnStatement(self, returnStatement):
    print('return ', end='')
    returnStatement.expression.accept(self)
    print(';', end='')   
  
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
    print(factorNumber.number)
    
  def visitFactorParen(self, factorParen):
    print('(', end='')
    factorParen.expression.accept(self)
    print(')')
  
  def visitFactorBooleanTrue(self, factorBooleanTrue):
    print(factorBooleanTrue.true)

  def visitFactorBooleanFalse(self, factorBooleanFalse):
    print(factorBooleanFalse.false)
    
  def visitFactorID(self, factorID):
    print(factorID.id)
  
  def visitError(self, error): pass