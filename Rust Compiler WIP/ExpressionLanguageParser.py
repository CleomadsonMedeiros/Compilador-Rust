import ply.yacc as yacc
import AbstractSyntax as sa
from ExpressionLanguageLex import tokens
# Regras do analisador sintático (parser)

# Pra executar apenas dentro da função main
def p_program_main(p):
    'program : main_function'
    p[0] = sa.Program(p[1])

def p_main_function(p):
    'main_function : FN MAIN LPAREN RPAREN block_statement'
    p[0] = sa.MainF(p[5])

def p_statement_list(p):
    '''statement_list : statement
                    | statement statement_list'''
    if len(p) == 2:
        p[0] = sa.StatementListStatement(p[1])
    elif len(p) == 3:
        p[0] = sa.StatementList(p[0], p[1])
    
# region funções
def p_def_function_with_params(p):
    'function_def : FN ID LPAREN param_list RPAREN ARROW return_type block_statement'
    p[0] = sa.DefFunction(p[2], p[4], p[7], p[8])

def p_def_function_no_params(p):
    'function_def : FN ID LPAREN RPAREN block_statement'
    p[0] = sa.DefFunctionUnit(p[2], p[5])
    
def p_function_call_no_params_semicolon(p):
    'function_call : ID LPAREN RPAREN SEMICOLON'
    p[0] = sa.FunctionCall(p[1])

def p_function_call_with_params_semicolon(p):
    'function_call : ID LPAREN id_list RPAREN SEMICOLON'
    p[0] = sa.FunctionCallIdList(p[1], p[3])

def p_function_call_no_params(p):
    'function_call : ID LPAREN RPAREN'
    p[0] = sa.FunctionCall(p[1])

def p_function_call_with_params(p):
    'function_call : ID LPAREN id_list RPAREN'
    p[0] = sa.FunctionCallIdList(p[1], p[3])
    
def p_id_list_id_comma(p):
    'id_list : ID COMMA id_list'
    p[0] = sa.IdListIdNumIdList(p[1], p[3])

def p_id_list_number_comma(p):
    'id_list : NUMBER COMMA id_list'
    p[0] = sa.IdListIdNumIdList(p[1], p[3])

def p_id_list_id(p):
    'id_list : ID'
    p[0] = sa.IdListIdNumFunctionCall(p[1])

def p_id_list_number(p):
    'id_list : NUMBER'
    p[0] = sa.IdListIdNumIdList(p[1])

def p_id_list_function_call(p):
    'id_list : function_call'
    p[0] = sa.IdListIdNumIdList(p[1])
    
def p_param_list_params(p):
    'param_list : param COMMA param_list'

def p_param_list_param(p):
    'param_list : param'
    
def p_param_id_i32(p):
    'param : ID COLON I32'

def p_param_id_f64(p):
    'param : ID COLON F64'

def p_param_id_bool(p):
    'param : ID COLON BOOL'
    
def p_return_type_i32(p):
    'return_type : I32'

def p_return_type_f64(p):
    'return_type : F64'

def p_return_type_bool(p):
    'return_type : BOOL'
#endregion
    
#region statements
def p_statement_function_def(p):
    'statement : function_def'

def p_statement_function_call(p):
    'statement : function_call'

def p_statement_expression_statement(p):
    'statement : expression_statement'

def p_statement_var_declaration(p):
    'statement : var_declaration'

def p_statement_var_assignment(p):
    'statement : var_assignment'

def p_statement_if(p):
    'statement : IF expression block_statement'

def p_statement_if_else(p):
    'statement : IF expression block_statement statement_else'

def p_statement_else_block(p):
    'statement_else : ELSE block_statement'

def p_statement_else_if(p):
    'statement_else : ELSE statement_else_if' 
    p[0] = sa.StatementElseIf(p[2])     

def p_statement_else_if_block(p):
    'statement_else_if : IF expression block_statement'
    p[0] = sa.StatementElseIfBlock(p[2])

def p_statement_else_if_with_else(p):
    'statement_else_if : IF expression block_statement statement_else'
    p[0] = sa.StatementElseIfWithElse(p[2],p[4])

def p_statement_while_statement(p):
    'statement : while_statement'
    p[0] = sa.StatementWhileStatement(p[1])     

def p_statement_return_statement(p):
    'statement : return_statement'
    p[0] = sa.StatementReturnStatement(p[1])

def p_statement_for_statement(p):
    'statement : for_statement'
    p[0] = sa.StatementForStatement(p[1])

def p_statement_block_statement(p):
    'statement : block_statement'
    p[0] = sa.StatementBlockStatement(p[1])
#endregion

#region Operadores Relacionais
def p_condition_notequal(p):
    'expression : expression NOTEQUAL condition'
    p[0] = sa.ExpressionNotEqual(p[1], p[3])

def p_condition_greaterequal(p):
    'expression : expression GREATEREQUAL condition'
    p[0] = sa.ExpressionGreaterEqual(p[1], p[3])

def p_condition_lessequal(p):
    'expression : expression LESSEQUAL condition'
    p[0] = sa.ExpressionLessEqual(p[1], p[3])

def p_condition_greater(p):
    'expression : expression GREATER condition'
    p[0] = sa.ExpressionGreater(p[1], p[3])

def p_condition_less(p):
    'expression : expression LESS condition'
    p[0] = sa.ExpressionLess(p[1], p[3])    

def p_condition_equals(p):
    'expression : expression EQUALS condition'
    p[0] = sa.ExpressionEquals(p[1], p[3])
#endregion

#region Operadores Logicos

def p_expression_and(p):
    'expression : expression AND condition'
    p[0] = sa.ExpressionAnd(p[1], p[3])

def p_expression_and(p):
    'expression : expression OR condition'
    p[0] = sa.ExpressionOr(p[1], p[3])

def p_expression_and(p):
    'expression : NOT condition'
    p[0] = sa.ExpressionNot(p[2])

def p_condition_term(p):
    'condition : term'
    p[0] = sa.ConditionTerm(p[1])

#endregion

def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'
    p[0] = sa.ExpressionStatement(p[1])

def p_var_declaration_mut_id(p):
    'var_declaration : LET MUT ID ASSIGN expression SEMICOLON'
    p[0] = sa.VarDeclarationMutId(p[3], p[5])

def p_var_declaration_mut_param(p):
    'var_declaration : LET MUT param ASSIGN expression SEMICOLON'
    p[0] = sa.VarDeclarationMutParam(p[3], p[5])

def p_var_declaration_id(p):
    'var_declaration : LET ID ASSIGN expression SEMICOLON'
    p[0] = sa.VarDeclarationId(p[2], p[4])

def p_var_declaration_param(p):
    'var_declaration : LET param ASSIGN expression SEMICOLON'
    p[0] = sa.VarDeclarationParam(p[2], p[4])

def p_var_assignment(p):
    'var_assignment : ID ASSIGN expression SEMICOLON'
    p[0] = sa.VarAssignment(p[1], p[3])

def p_while_statement(p):
    'while_statement : WHILE expression block_statement'
    p[0] = sa.WhileStatement(p[2])

def p_for_statement(p):
    'for_statement : FOR ID IN expression block_statement'
    p[0] = sa.ForStatement(p[2], p[4])

def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'
    p[0] = sa.ReturnStatement(p[2])

def p_block_statement(p):
    'block_statement : LBRACE statement_list RBRACE'
    p[0] = sa.StatementBlockStatement(p[2])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = sa.ExpressionPlus(p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = sa.ExpressionMinus(p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = sa.ExpressionTerm(p[1])

def p_expression_range(p):
    'expression : expression RANGE term'
    p[0] = sa.ExpressionRange(p[1], p[3])

def p_term_modulo(p):
    'term : term MODULO factor'
    p[0] = sa.TermModulo(p[1], p[3])

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = sa.TermTimes(p[1], p[3])

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = sa.TermDivide(p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = sa.TermFactor(p[1])

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = sa.FactorNumber(p[1])

def p_factor_paren(p):
    'factor : LPAREN expression RPAREN'
    p[0] = sa.FactorParen(p[2])

def p_factor_boolean_true(p):
    '''factor : TRUE'''
    p[0] = sa.FactorBooleanTrue(p[1])

def p_factor_boolean_false(p):
    '''factor : FALSE'''
    p[0] = sa.FactorBooleanFalse(p[1])

def p_factor_id(p):
    'factor : ID'
    p[0] = sa.FactorID(p[1])

def p_error(p):
    print("Erro de sintaxe")
    print(p)

parser = yacc.yacc()

# Teste do parser
resultado = parser.parse('''                 
    fn main(){
        let mut x: i32 = 5;
        x + 1;
        let y = 4;
        1 + 1;
        3 - 2;
        x = y + 4;
        if !x {
          x = x + 1;
        }
        let a = 3 >= 5;
        3 != 3;
        while x > 2 && x < 0 {
        1 + 1;
        2 / 2;
        }
        fn soma(a: i32, b: f64, c: i32) -> f64 {
          return a + b;
        }
        fn show() { println(soma(3, soma(3,3)));}
        for x in 1..10 / 5 {
        0 + 1;
        }
        return x;                 
    }     
''')
print(resultado)
result = parser.parse(debug = True)
print(result)