from PrettyPrinter import *
from ExpressionLanguageLex import *
from ExpressionLanguageParser import *
import SymbolTable as st

class SemanticVisitor(PrettyPrinter):

    def __init__(self):
        self.printer = PrettyPrinter()
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

      if defFunction.paramList != None:
          params = defFunction.paramList.accept(self)
          if not isinstance(params, list):
              print(f"\n\t[Erro] Lista de parâmetros inválida na função '{defFunction.id}'.")
              self.n_errors += 1
              params = []
          st.addFunction(defFunction.id, params, defFunction.returnType.accept(self))
      else:
          st.addFunction(defFunction.id, params, defFunction.returnType.accept(self))

      st.beginScope(defFunction.id)
      for k in range(0, len(params)):
          try:
              st.addVar(params[k][0], params[k][1])
          except Exception as e:
              print(f"\n\t[Erro] Parâmetro inválido: {params[k]}. Detalhes: {e}")
              self.n_errors += 1
      
      defFunction.blockStatement.accept(self)

    def visitDefFunctionUnit(self, defFunctionUnit):
      st.addFunction(defFunctionUnit.id)
      defFunctionUnit.blockStatement.accept(self)

    def visitFunctionCall(self, functionCall):
      bindable = st.getBindable(functionCall.id)
      if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
        return bindable[st.TYPE]
      print("Código com erro:", end=" ")
      functionCall.accept(self.printer)
      self.n_errors += 1
      print("\n[Erro] Chamada de função inválida.")
      return None
      
    def visitFunctionCallIdList(self, functionCallIdList):
      bindable = st.getBindable(functionCallIdList.id)
      if bindable is not None and bindable[st.BINDABLE] == st.FUNCTION:
          param_values = functionCallIdList.idList.accept(self)
          typeParams = []

          for val in param_values:
              if isinstance(val, int):
                  typeParams.append(st.I32)
              elif isinstance(val, float):
                  typeParams.append(st.F64)
              elif isinstance(val, bool):
                  typeParams.append(st.BOOL)
              elif isinstance(val, str):
                  # Verifica o tipo no escopo para variáveis
                  bind = st.getBindable(val)
                  if bind and st.TYPE in bind:
                      typeParams.append(bind[st.TYPE])
                  else:
                      print(f"\n[Erro] Identificador '{val}' não declarado ou sem tipo.")
                      self.n_errors += 1
                      typeParams.append(None)
              elif val is None:
                  typeParams.append(None)
              else:
                  print(f"\n[Erro] Tipo não reconhecido para valor: {val}")
                  self.n_errors += 1
                  typeParams.append(None)
          expected = [param[1] for param in bindable[st.PARAMS]]
          if typeParams == expected:
              return bindable[st.TYPE]
          else:
              print("Código com erro:", end=" ")
              functionCallIdList.accept(self.printer)
              print(f"\n[Erro] Tipos de parâmetros incompatíveis na chamada da função '{functionCallIdList.id}'. Esperado: {expected}, recebido: {typeParams}")
              self.n_errors += 1
              return None

      print("Código com erro:", end=" ")
      functionCallIdList.accept(self.printer)
      print(f"\n[Erro] Função '{functionCallIdList.id}' não declarada.")
      self.n_errors += 1
      return None

    def visitIdListIdComma(self, idListIdComma):
      return [idListIdComma.id] + idListIdComma.idList.accept(self)
    
    def visitIdListNumComma(self, idListNumComma):
      return [idListNumComma.num] + idListNumComma.idList.accept(self)

    def visitIdListFunctionCallComma(self, idListFunctionCallComma):
      tipoFuncao = idListFunctionCallComma.function.accept(self)
      return [tipoFuncao] + idListFunctionCallComma.idList.accept(self)

    def visitIdListId(self, idListId):
      return [idListId.id]

    def visitIdListNum(self, idListNum):
      return [idListNum.num]

    def visitIdListFunctionCall(self, idListFunctionCall):
      tipoFuncao = idListFunctionCall.function.accept(self)
      return [tipoFuncao]

    def visitParamListParams(self, paramListParams):
      return [paramListParams.param.accept(self)] + paramListParams.param_list.accept(self)
      
    def visitParamListParam(self, paramListParam):
      return [paramListParam.param.accept(self)]

    def visitParamIdI32(self, paramIdI32):
      return [paramIdI32.id, st.I32]

    def visitParamIdF64(self, paramIdF64):
      return [paramIdF64.id, st.F64]

    def visitParamIdBool(self, paramIdBool):
      return [paramIdBool.id, st.BOOL]

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

    def visitStatementIfStatement(self, statementIfStatement):
      statementIfStatement.if_statement.accept(self)
      
    def visitStatementIf(self, statementIf):
      st.beginScope('if')
      statementIf.expression.accept(self)
      statementIf.block_statement.accept(self)

    def visitStatementIfElse(self, statementIfElse):
      st.beginScope('if')
      statementIfElse.expression.accept(self)
      statementIfElse.block_statement_esq.accept(self)
      statementIfElse.block_statement_dir.accept(self)

    def visitStatementIfElseIf(self, statementIfElseIf):
      st.beginScope('if')
      statementIfElseIf.expression.accept(self)
      statementIfElseIf.block_statement.accept(self)
      statementIfElseIf.if_statement.accept(self)

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

    def visitExpressionFunctionCall(self, functionCall):
      functionCall.function_call.accept(self)
      
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
       try:
        nome, tipo = varDeclarationMutParam.param.accept(self)
        st.addVar(nome, multable=True, type=tipo)
        varDeclarationMutParam.expression.accept(self)
       except Exception as e:
        print(f"\n\t[Erro] Declaração de variável mutável inválida. Detalhes: {e}")
        self.n_errors += 1

    def visitVarDeclarationId(self, varDeclarationId):
      st.addVar(varDeclarationId.id)
      varDeclarationId.expression.accept(self)

    def visitVarDeclarationParam(self, varDeclarationParam):
      st.addVar(varDeclarationParam.param.accept(self)[0], type=varDeclarationParam.param.accept(self)[1])
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
      if returnStatement.expression is None:
        print("\n\t[Erro] Retorno de função sem valor.")
        self.n_errors += 1
      else:
          returnStatement.expression.accept(self)
      
    def visitBlockStatement(self, blockStatement):
      blockStatement.statement_list.accept(self)
      
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
      id_info = st.getBindable(factorID.id)
      if id_info is None:
          print(f"\n\t[Erro] Identificador '{factorID.id}' não declarado.")
          self.n_errors += 1
          return None
      return id_info[st.TYPE] if st.TYPE in id_info else None
    
    def visitError(self, error): pass

files = [
  "input_correto.rs",
  "input_com_erro_1.rs",
  "input_com_erro_2.rs"
]

for file_path in files:
  print(f"\nAnalisando arquivo: {file_path}")
  with open(file_path, "r") as f:
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)

    svisitor = SemanticVisitor()
    if result:
      result.accept(svisitor)
    else:
      print("[Erro] Árvore de sintaxe abstrata inválida.")


    if svisitor.n_errors > 0:
      print(f"\nNúmero total de erros no arquivo: {svisitor.n_errors}")
    else:
      print(f"\nAnálise semântica concluída com sucesso no arquivo. Nenhum erro encontrado.")