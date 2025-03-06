from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):
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
    def visitExprAnd(self, exprAnd): pass 
    
    @abstractmethod 
    def visitExprOr(self, exprOr): pass 
    
    @abstractmethod 
    def visitExprNot(self, exprNot): pass
    
    @abstractmethod
    def visitConditionTerm(self, conditionTerm): pass
    
    @abstractmethod
    def visitExpressionStatement(self, expressionStatement): pass   
    
    @abstractmethod
    def visitVarDeclaration(self, varDeclaration): pass 
    
    @abstractmethod
    def visitVarDeclaration2(self, varDeclaration2): pass
    
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
    def visitFactorBoolean(self, factorBoolean): pass
    
    @abstractmethod 
    def visitFactorID(self, factorID): pass
    
    @abstractmethod
    def visitError(self, error): pass