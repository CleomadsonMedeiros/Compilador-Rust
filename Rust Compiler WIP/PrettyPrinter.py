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
#stR
  def visitParamListParams(self, paramListParams):
    paramListParams.param.accept(self)
    print(', ', end='') 
    paramListParams.paramlist.accept(self)
    
  def visitParamListParam(self, paramListParam):
    paramListParam.param.accept(self) 

  def visitParamIdI32(self, paramIdI32):
    paramIdI32.typename32.accept(self)
    print(': i32')

  def visitParamIdF64(self, paramIdF64):
    paramIdF64.typename64.accept(self)
    print(': f64')

  def visitParamIdBool(self, paramIdBool):
    paramIdBool.typenamebool.accept(self)
    print(': bool')

  def visitStatementFunctionDef(self, statementFunctionDef):

    statementFunctionDef.function_def.accept(self)
    # print('fn ', end='')
    # statementFunctionDef.name.accept(self)
    # print('(', end='')
    # statementFunctionDef.params.accept(self)
    # print(') -> ', end='')
    # statementFunctionDef.return_type.accept(self)
    # print(' {') 
    # statementFunctionDef.body.accept(self)
    # print('}')  

  def visitStatementFunctionCall(self, statementFunctionCall):
    statementFunctionCall.function_call.accept(self)  
    # print('(', end='')  
    # statementFunctionCall.arguments.accept(self) 
    # print(')', end='') 

  def visitStatementExpressionStatement(self, statementExpressionStatement):
    statementExpressionStatement.expression_statement.accept(self) 
    

  def visitStatementVarDeclaration(self, statementVarDeclaration):
    statementVarDeclaration.var_declaration.accept(self)

  def visitStatementVarAssignment(self, statementVarAssignment):
    statementVarAssignment.var_assignment.accept(self) 
    

  def visitStatementIf(self, statementIf):
    print('if ', end='') 
    statementIf.condition.accept(self)  
    print(' {') 
    statementIf.block.accept(self) 
    print('}') 

  def visitStatementIfElse(self, statementIfElse):
    print('if ', end='')
    statementIfElse.condition.accept(self)
    print(' {')
    statementIfElse.blockLeft.accept(self)
    print('}')
    print('else {') 
    statementIfElse.statemElse.accept(self)
    print('}')

  def visitStatementElseBlock(self, statementElseBlock):
    print('else {', end='') 
    statementElseBlock.blockStatem.accept(self) 
    print('}') 

  def visitReturnTypeI32(self, returnTypeI32):
    print(returnTypeI32.typename32)  

  def visitReturnTypeF64(self, returnTypeF64):
    print(returnTypeF64.typename64)  

  def visitReturnTypeBool(self, returnTypeBool):
    print(returnTypeBool.typenamebool)  
 #endR
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
    
  def visitExpressionAnd(self, expressionAnd): pass 
    
  def visitExpressionOr(self, expressionOr): pass 
    
  def visitExpressionNot(self, expressionNot): pass
  
  def visitConditionTerm(self, conditionTerm): pass
  
  def visitExpressionStatement(self, expressionStatement): pass   
  
  def visitVarDeclarationMutId(self, varDeclaration): pass 
  
  def visitVarDeclarationMutParam(self, varDeclarationMutParam): pass

  def visitVarDeclarationId(self, varDeclarationId): pass

  def visitVarDeclarationParam(self, varDeclarationParam): pass
  
  def visitVarAssignment(self, varAssignment): pass
  
  def visitWhileStatement(self, whileStatement): pass 
  
  def visitForStatement(self, forStatement): pass  
    
  def visitReturnStatement(self, returnStatement): pass   
  
  def visitBlockStatement(self, blockStatement): pass
    
  def visitExpressionPlus(self, expressionPlus): pass
        
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