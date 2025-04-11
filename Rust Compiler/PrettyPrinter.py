from AbstractVisitor import AbstractVisitor

class PrettyPrinter(AbstractVisitor):
  def __init__(self):
    self.indent_level = 0

  def write(self, text='', end='\n'):
    print('  ' * self.indent_level + text, end=end)

  def visitProgram(self, program):
    program.main.accept(self)

  def visitMainFunction(self, mainFunction): 
    self.write('fn main()')
    mainFunction.blockStatement.accept(self)

  def visitStatementListStatement(self, statementListStatement):
    statementListStatement.statement.accept(self)

  def visitStatementListStatementStatementList(self, statementListStatementStatementList):
    statementListStatementStatementList.statement.accept(self)
    statementListStatementStatementList.statementList.accept(self)

  def visitDefFunction(self, defFunction):
    self.write(f'fn {defFunction.id}(', end='')
    defFunction.paramList.accept(self)
    print(') -> ', end='')
    defFunction.returnType.accept(self)
    defFunction.blockStatement.accept(self)

  def visitDefFunctionUnit(self, defFunctionUnit):
    self.write(f'fn {defFunctionUnit.id}()')
    defFunctionUnit.blockStatement.accept(self)

  def visitFunctionCall(self, functionCall):
    self.write(f'{functionCall.id}();')

  def visitFunctionCallIdList(self, functionCallIdList):
    self.write(f'{functionCallIdList.id}(', end='')
    functionCallIdList.idList.accept(self)
    print(');')

  def visitIdListIdComma(self, idListIdComma):
    print(idListIdComma.id, end=', ')
    idListIdComma.idList.accept(self)

  def visitIdListNumComma(self, idListNumComma):
    print(idListNumComma.num, end=', ')
    idListNumComma.idList.accept(self)

  def visitIdListFunctionCallComma(self, idListFunctionCallComma):
    idListFunctionCallComma.function.accept(self)
    print(', ', end='')
    idListFunctionCallComma.idList.accept(self)

  def visitIdListId(self, idListId):
    print(idListId.id, end='')

  def visitIdListNum(self, idListNum):
    print(idListNum.num, end='')

  def visitIdListFunctionCall(self, idListFunctionCall):
    idListFunctionCall.function.accept(self)

  def visitParamListParams(self, paramListParams):
    paramListParams.param.accept(self)
    print(', ', end='')
    paramListParams.param_list.accept(self)

  def visitParamListParam(self, paramListParam):
    paramListParam.param.accept(self)

  def visitParamIdI32(self, paramIdI32):
    print(f"{paramIdI32.id}: i32", end='')

  def visitParamIdF64(self, paramIdF64):
    print(f"{paramIdF64.id}: f64", end='')

  def visitParamIdBool(self, paramIdBool):
    print(f"{paramIdBool.id}: bool", end='')

  def visitStatementFunctionDef(self, statementFunctionDef):
    statementFunctionDef.function_def.accept(self)

  def visitStatementFunctionCall(self, statementFunctionCall):
    statementFunctionCall.function_call.accept(self)

  def visitStatementExpressionStatement(self, statementExpressionStatement):
    self.write('', end='')
    statementExpressionStatement.expression_statement.accept(self)

  def visitStatementVarDeclaration(self, statementVarDeclaration):
    statementVarDeclaration.var_declaration.accept(self)

  def visitStatementVarAssignment(self, statementVarAssignment):
    statementVarAssignment.var_assignment.accept(self)

  def visitStatementIfStatement(self, statementIfStatement):
    statementIfStatement.if_statement.accept(self)

  def visitStatementIf(self, statementIf):
    self.write('if ', end='')
    statementIf.expression.accept(self)
    statementIf.block_statement.accept(self)

  def visitStatementIfElse(self, statementIfElse):
    self.write('if ', end='')
    statementIfElse.expression.accept(self)
    statementIfElse.block_statement_esq.accept(self)
    self.write('else')
    statementIfElse.block_statement_dir.accept(self)

  def visitStatementIfElseIf(self, statementIfElseIf):
    self.write('if ', end='')
    statementIfElseIf.expression.accept(self)
    statementIfElseIf.block_statement.accept(self)
    statementIfElseIf.if_statement.accept(self)

  def visitReturnTypeI32(self, returnTypeI32):
    print('i32', end='')

  def visitReturnTypeF64(self, returnTypeF64):
    print('f64', end='')

  def visitReturnTypeBool(self, returnTypeBool):
    print('bool', end='')

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

  def visitExpressionFunctionCall(self, functionCall):
    functionCall.function.accept(self)
    print(';')

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
    self.write(f'let mut {varDeclaration.id} = ', end='')
    varDeclaration.expression.accept(self)
    print(';')

  def visitVarDeclarationMutParam(self, varDeclarationMutParam):
    self.write('let mut ', end='')
    varDeclarationMutParam.param.accept(self)
    print(' = ', end='')
    varDeclarationMutParam.expression.accept(self)
    print(';')

  def visitVarDeclarationId(self, varDeclarationId):
    self.write(f'let {varDeclarationId.id} = ', end='')
    varDeclarationId.expression.accept(self)
    print(';')

  def visitVarDeclarationParam(self, varDeclarationParam):
    self.write('let ', end='')
    varDeclarationParam.param.accept(self)
    print(' = ', end='')
    varDeclarationParam.expression.accept(self)
    print(';')

  def visitVarAssignment(self, varAssignment):
    self.write(f'{varAssignment.id} = ', end='')
    varAssignment.expression.accept(self)
    print(';')

  def visitWhileStatement(self, whileStatement):
    self.write('while ', end='')
    whileStatement.expression.accept(self)
    whileStatement.block_statement.accept(self)

  def visitForStatement(self, forStatement):
    self.write(f'for {forStatement.id} in ', end='')
    forStatement.expression.accept(self)
    forStatement.block_statement.accept(self)

  def visitReturnStatement(self, returnStatement):
    self.write('return ', end='')
    returnStatement.expression.accept(self)
    print(';')

  def visitBlockStatement(self, blockStatement):
    self.write('{')
    self.indent_level += 1
    blockStatement.statement_list.accept(self)
    self.indent_level -= 1
    self.write('}')

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
    print(factorNumber.number, end='')

  def visitFactorParen(self, factorParen):
    print('(', end='')
    factorParen.expression.accept(self)
    print(')', end='')

  def visitFactorBooleanTrue(self, factorBooleanTrue):
    print(factorBooleanTrue.true, end='')

  def visitFactorBooleanFalse(self, factorBooleanFalse):
    print(factorBooleanFalse.false, end='')

  def visitFactorID(self, factorID):
    print(factorID.id, end='')

  def visitError(self, error): pass
