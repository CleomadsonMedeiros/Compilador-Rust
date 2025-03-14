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

  def visitParamListParamComma(self, paramListParamComma): pass

  def visitParamListParam(self, paramListParam): pass

  def visitParamIdI32(self, paramIDI32): pass

  def visitParamIdF64(self, paramIdF64): pass

  def visitParamIdBool(self, paramIdBool): pass

  def visitStatementFunctionDef(self, statementFunctionDef): pass

  def visitStatementFunctionCall(self, statementFunctionCall): pass

  def visitStatementExpressionStatement(self, statementExpressionStatement): pass

  def visitStatementVarDeclaration(self, statementVarDeclaration): pass

  def visitStatementVarAssignment(self, statementVarAssignment): pass

  def visitStatementIf(self, statementIf): pass

  def visitStatementIfElse(self, statementIfElse): pass

  def visitStatementElseBlock(self, statementElseBlock): pass

  def visitStatementElseIf(self, statementElseIf): 
    print('else if ', end='')
    statementElseIf.expression.accept(self)

  def visitStatementElseIfBlock(self, statementElseIfBlock):
    print('else if ', end='')
    statementElseIfBlock.expression.accept(self)
    print('{')
    print('}')

  def visitStatementIfWithElse(self, statementIfWithElse): 
    print('if ', end='')
    statementIfWithElse.expression.accept(self)
    print('{')
    print('}')
    print('else', end='')
    print('{')
    print('}')

  def visitStatementWhileStatement(self, whileStatement): 
    print('while ', end='') 
    whileStatement.expression.accept(self)
    print('{')
    print('}')
  
  def visitStatementReturnStatement(self, returnStatement): 
    print('return ', end='')
    returnStatement.expression.accept(self)
    print(';')
    
  def visitStatementForStatement(self, forStatement): 
    print('for ', end='')
    forStatement.id.accept(self)
    print(' in ', end='')
    forStatement.expression.accept(self)
    print('{')
    print('}')      
  
  def visitStatementBlockStatement(self, blockStatement):
    print('{')
    print('}')
  
  def visitConditionNotEqual(self, notEqual):
    notEqual.expression.accept(self)
    print(' != ', end='')
    notEqual.condition.accept(self)
    
  def visitConditionGreaterEqual(self, greaterEqual):
    greaterEqual.expression.accept(self)
    print(' >= ', end='')
    greaterEqual.condition.accept(self)
  
  def visitConditionLessEqual(self, lessEqual): 
    lessEqual.expression.accept(self)
    print(' <= ', end='')
    lessEqual.condition.accept(self)
  
  def visitConditionGreater(self, greater): 
    greater.expression.accept(self)
    print(' > ', end='')
    greater.condition.accept(self)
    
  def visitConditionLess(self, less): 
    less.expression.accept(self)
    print(' < ', end='')
    less.condition.accept(self) 
        
  def visitConditionEquals(self, equals): 
    equals.expression.accept(self)
    print(' == ', end='')
    equals.condition.accept(self)
    
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
    expressionNot.expression.accept(self)
  
  def visitConditionTerm(self, conditionTerm):
    conditionTerm.term.accept(self)
  
  def visitExpressionStatement(self, expressionStatement):
    expressionStatement.expression.accept(self)   
  
  def visitVarDeclarationMutId(self, varDeclaration):
    print('let mut ', end='')
    varDeclaration.id.accept(self)
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
    varDeclarationId.id.accept(self)
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
    varAssignment.id.accept(self)
    print(' = ', end='')
    varAssignment.expression.accept(self)
    print(';')
  
  def visitWhileStatement(self, whileStatement):
    print('while ', end='')
    whileStatement.expression.accept(self)
    print('{')
    print('}') 
  
  def visitForStatement(self, forStatement):
    print('for ', end='')
    forStatement.id.accept(self)
    print(' in ', end='')
    forStatement.expression.accept(self)
    print('{')
    print('}')
    
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