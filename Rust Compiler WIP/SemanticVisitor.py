from AbstractVisitor import *
import SymbolTable as st

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = AbstractVisitor()
        self.n_errors = 0
        st.beginScope('main')

    def visitProgram(self, program):
      program.main.accept(self)

    def visitMainFunction(self, mainFunction): 
      mainFunction.blockStatement.accept(self)
    
    def visitStatementListStatement(self, statementListStatement):
      statementListStatement.statement.accept(self)

    def visitStatementListStatementStatementList(self, statementListStatementStatementList):
      statementListStatementStatementList.statement.accept(self)
      statementListStatementStatementList.statementList.accept(self)

    def visitDefFunction(self, defFunction):
      params = {}

      if(defFunction.paramList != None):
        params = defFunction.paramList.accept(self)
        st.addFunction(defFunction.id, params, defFunction.returnType.accept(self))
      else:
        st.addFunction(defFunction.id, params, defFunction.returnType.accept(self))

      st.beginScope(defFunction.id)
      for k in range(0, len(params), 2):
        st.addVar(params[k], params[k+1])
      
      defFunction.blockStatement.accept(self)

    def visitDefFunctionUnit(self, defFunctionUnit):
      st.addFunction(defFunctionUnit.id)
      defFunctionUnit.blockStatement.accept(self)

    def visitFunctionCall(self, functionCall):
      bindable = st.getBindable(functionCall.id)
      if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
        return bindable[st.TYPE]
      functionCall.accept(self.printer)
      self.n_errors += 1
      print("\n\t[Erro] Chamada de função inválida.")
      return None
      
    def visitFunctionCallIdList(self, functionCallIdList):
      bindable = st.getBindable(functionCallIdList.id)
      if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
        typeParams = functionCallIdList.params.accept(self)
        if (list(bindable[st.PARAMS][1::2]) == typeParams):
          return bindable[st.TYPE]
        
        functionCallIdList.accept(self.printer)
        self.n_errors += 1
        print("\n\t[Erro] Chamada de função inválida.")
        return None

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
      st.beginScope('if')
      statementIf.condition.accept(self)
      statementIf.block_statement.accept(self)

    def visitStatementIfElse(self, statementIfElse):
      st.beginScope('if')
      statementIfElse.expression.accept(self)
      statementIfElse.block_statement.accept(self)
      statementIfElse.statement_else.accept(self)

    def visitStatementElseBlock(self, statementElseBlock):
      st.beginScope('else')
      statementElseBlock.block_statement.accept(self)

    def visitStatementIfWithElse(self, statementIfWithElse):
      st.beginScope('if')
      statementIfWithElse.expression.accept(self)
      statementIfWithElse.block_statement.accept(self)
      statementIfWithElse.statement_else.accept(self)

    def visitReturnTypeI32(self, returnTypeI32):
      return st.I32

    def visitReturnTypeF64(self, returnTypeF64):
      return st.F64

    def visitReturnTypeBool(self, returnTypeBool):
      return st.BOOL

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
      conditionNotEqual.condition.accept(self)
      
    def visitConditionGreaterEqual(self, conditionGreaterEqual):
      conditionGreaterEqual.expression.accept(self)
      conditionGreaterEqual.condition.accept(self)      
    
    def visitConditionLessEqual(self, conditionLessEqual):
      conditionLessEqual.expression.accept(self)
      conditionLessEqual.condition.accept(self)
    
    def visitConditionGreater(self, conditionGreater):
      conditionGreater.expression.accept(self)
      conditionGreater.condition.accept(self)
      
    def visitConditionLess(self, conditionLess):
      conditionLess.expression.accept(self)
      conditionLess.condition.accept(self)
          
    def visitConditionEquals(self, conditionEquals):
      conditionEquals.expression.accept(self)
      conditionEquals.condition.accept(self)
      
    def visitExpressionAnd(self, expressionAnd):
      expressionAnd.expression.accept(self)
      expressionAnd.condition.accept(self)
      
    def visitExpressionOr(self, expressionOr):
      expressionOr.expression.accept(self)
      expressionOr.condition.accept(self)
      
    def visitExpressionNot(self, expressionNot):
      expressionNot.condition.accept(self)
    
    def visitConditionTerm(self, conditionTerm):
      conditionTerm.term.accept(self)
    
    def visitExpressionStatement(self, expressionStatement):
      expressionStatement.expression.accept(self)
    
    def visitVarDeclarationMutId(self, varDeclaration):
      st.addVar(varDeclaration.id, multable=True)
      varDeclaration.expression.accept(self)
    
    def visitVarDeclarationMutParam(self, varDeclarationMutParam):
      st.addVar(varDeclarationMutParam.param.accept(self), multable=True)
      varDeclarationMutParam.expression.accept(self)

    def visitVarDeclarationId(self, varDeclarationId):
      st.addVar(varDeclarationId.id)
      varDeclarationId.expression.accept(self)

    def visitVarDeclarationParam(self, varDeclarationParam):
      st.addVar(varDeclarationParam.param.accept(self))
      varDeclarationParam.expression.accept(self)
    
    def visitVarAssignment(self, varAssignment):
      id = st.getBindable(varAssignment.id)
      if(id != None):
        varAssignment.expression.accept(self)
      else:
        print("Variável não declarada")
    
    def visitWhileStatement(self, whileStatement):
      whileStatement.expression.accept(self)
      whileStatement.block_statement.accept(self)
    
    def visitForStatement(self, forStatement):
      st.addVar(forStatement.id, multable=True)
      forStatement.expression.accept(self)
      forStatement.block_statement.accept(self)  
      
    def visitReturnStatement(self, returnStatement):
      returnStatement.expression.accept(self)
    
    def visitBlockStatement(self, blockStatement):
      blockStatement.statementList.accept(self)
      
    def visitExpressionPlus(self, expressionPlus):
      expressionPlus.expression.accept(self)
      expressionPlus.term.accept(self)
          
    def visitExpressionMinus(self, expressionMinus):
      expressionMinus.expression.accept(self)
      expressionMinus.term.accept(self)
    
    def visitExpressionTerm(self, expressionTerm):
      expressionTerm.term.accept(self)

    def visitExpressionRange(self, expressionRange): 
      expressionRange.expression.accept(self)
      expressionRange.term.accept(self)

    def visitTermModulo(self, termModulo):
      termModulo.term.accept(self)
      termModulo.factor.accept(self)
    
    def visitTermTimes(self, termTimes):
      termTimes.term.accept(self)
      termTimes.factor.accept(self)      
    
    def visitTermDivide(self, termDivide):
      termDivide.term.accept(self)
      termDivide.factor.accept(self)

    def visitTermFactor(self, termFactor):
      termFactor.factor.accept(self)   
      
    def visitFactorNumber(self, factorNumber):
      return factorNumber.number
      
    def visitFactorParen(self, factorParen):
      factorParen.expression.accept(self)
    
    def visitFactorBooleanTrue(self, factorBooleanTrue):
      return st.BOOL

    def visitFactorBooleanFalse(self, factorBooleanFalse):
      return st.BOOL
      
    def visitFactorID(self, factorID):
      return factorID.id
    
    def visitError(self, error): pass