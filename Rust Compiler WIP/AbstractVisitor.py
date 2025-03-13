from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitProgram(self, program): pass

    @abstractmethod
    def visitMainFunction(self, mainFunction): pass
    
    @abstractmethod
    def visitStatementListStatement(self, statementListStatement): pass

    @abstractmethod
    def visitStatementList(self, statementList): pass

    @abstractmethod
    def visitDefFunction(self, defFunction): pass

    @abstractmethod
    def visitDefFunctionUnit(self, defFunctionUnit): pass

    @abstractmethod
    def visitFunctionCallSemicolon(self, functionCallSemicolon): pass

    @abstractmethod
    def visitFunctionCallIdListSemicolon(self, functionCallIdListSemicolon): pass

    @abstractmethod
    def visitFunctionCall(self, functionCall): pass

    @abstractmethod
    def visitFunctionCallIdList(self, functionCallIdList): pass

    @abstractmethod
    def visitIdListIdComma(self, idListIdComma): pass

    @abstractmethod
    def visitIdListNumberComma(self, idListNumberComma): pass

    @abstractmethod
    def visitIdListId(self, idListIdComma): pass

    @abstractmethod
    def visitIdListNumber(self, idListNumber): pass

    @abstractmethod
    def visitIdListFunctionCall(self, idListFunctionCall): pass

    @abstractmethod
    def visitParamListParamComma(self, paramListParamComma): pass

    @abstractmethod
    def visitParamListParam(self, paramListParam): pass

    @abstractmethod
    def visitParamIdI32(self, paramIDI32): pass

    @abstractmethod
    def visitParamIdF64(self, paramIdF64): pass

    @abstractmethod
    def visitParamIdBool(self, paramIdBool): pass

    @abstractmethod
    def visitStatementFunctionDef(self, statementFunctionDef): pass

    @abstractmethod
    def visitStatementFunctionCall(self, statementFunctionCall): pass

    @abstractmethod
    def visitStatementExpressionStatement(self, statementExpressionStatement): pass

    @abstractmethod
    def visitStatementVarDeclaration(self, statementVarDeclaration): pass

    @abstractmethod
    def visitStatementVarAssignment(self, statementVarAssignment): pass

    @abstractmethod
    def visitStatementIf(self, statementIf): pass

    @abstractmethod
    def visitStatementIfElse(self, statementIfElse): pass

    @abstractmethod
    def visitStatementElseBlock(self, statementElseBlock): pass

    @abstractmethod
    def visitStatementElseIf(self, statementElseIf): pass

    @abstractmethod
    def visitStatementElseIfBlock(self, statementElseIfBlock): pass

    @abstractmethod
    def visitStatementIfWithElse(self, statementIfWithElse): pass

    @abstractmethod
    def visitStatementWhileStatement(self, whileStatement): pass
    
    @abstractmethod
    def visitStatementReturnStatement(self, returnStatement): pass
    
    @abstractmethod 
    def visitStatementForStatement(self, forStatement): pass      
    
    @abstractmethod
    def visitStatementBlockStatement(self, blockStatement): pass
    
    @abstractmethod
    def visitConditionNotEqual(self, notEqual): pass
    
    @abstractmethod 
    def visitConditionGreaterEqual(self, greaterEqual): pass      
    
    @abstractmethod
    def visitConditionLessEqual(self, lessEqual): pass
    
    @abstractmethod
    def visitConditionGreater(self, greater): pass
    
    @abstractmethod 
    def visitConditionLess(self, less): pass
    
    @abstractmethod     
    def visitConditionEquals(self, equals): pass
    
    @abstractmethod 
    def visitExpressionAnd(self, expressionAnd): pass 
    
    @abstractmethod 
    def visitExpressionOr(self, expressionOr): pass 
    
    @abstractmethod 
    def visitExpressionNot(self, expressionNot): pass
    
    @abstractmethod
    def visitConditionTerm(self, conditionTerm): pass
    
    @abstractmethod
    def visitExpressionStatement(self, expressionStatement): pass   
    
    @abstractmethod
    def visitVarDeclarationMutId(self, varDeclaration): pass 
    
    @abstractmethod
    def visitVarDeclarationMutParam(self, varDeclarationMutParam): pass

    @abstractmethod
    def visitVarDeclarationId(self, varDeclarationId): pass

    @abstractmethod
    def visitVarDeclarationParam(self, varDeclarationParam): pass
    
    @abstractmethod
    def visitVarAssignment(self, varAssignment): pass
    
    @abstractmethod
    def visitWhileStatement(self, whileStatement): pass 
    
    @abstractmethod
    def visitForStatement(self, forStatement): pass  
    
    @abstractmethod 
    def visitReturnStatement(self, returnStatement): pass   
    
    @abstractmethod
    def visitBlockStatement(self, blockStatement): pass
    
    @abstractmethod 
    def visitExpressionPlus(self, expressionPlus): pass
    
    @abstractmethod     
    def visitExpressionMinus(self, expressionMinus): pass       
    
    @abstractmethod     
    def visitTermModulo(self, termModulo): pass
    
    @abstractmethod
    def visitTermTimes(self, termTimes): pass
    
    @abstractmethod 
    def visitTermDivide(self, termDivide): pass
    
    @abstractmethod
    def visitExpressionTerm(self, expressionTerm): pass 
    
    @abstractmethod
    def visitExpressionRange(self, expressionRange): pass       
    
    @abstractmethod
    def visitTermFactor(self, termFactor): pass   
    
    @abstractmethod 
    def visitFactorNumber(self, factorNumber): pass 
    
    @abstractmethod 
    def visitFactorParen(self, factorParen): pass
    
    @abstractmethod
    def visitFactorBooleanTrue(self, factorBoolean): pass

    @abstractmethod
    def visitFactorBooleanFalse(self, factorBoolean): pass
    
    @abstractmethod 
    def visitFactorID(self, factorID): pass
    
    @abstractmethod
    def visitError(self, error): pass