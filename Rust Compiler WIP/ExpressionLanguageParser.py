import ply.yacc as yacc
from ExpressionLanguageLex import tokens



# Regras do analisador sintático (parser)

# Pra executar apenas dentro da função main
def p_program_main(p):
    'program : main_function'

def p_main_function(p):
    'main_function : FN MAIN LPAREN RPAREN block_statement'

def p_statement_list(p):
    '''statement_list : statement
                    | statement statement_list'''
    
# region funções

def p_def_function(p):
    '''function_def : FN ID LPAREN param_list RPAREN ARROW return_type block_statement
                | FN ID LPAREN RPAREN block_statement'''
    
def p_function_call(p):
    '''function_call : ID LPAREN RPAREN SEMICOLON
                      | ID LPAREN id_list RPAREN SEMICOLON
                      | ID LPAREN RPAREN
                      | ID LPAREN id_list RPAREN'''
    
def p_id_list(p):
    '''id_list : ID COMMA id_list
              | NUMBER COMMA id_list
              | ID
              | NUMBER
              | function_call'''
    
def p_param_list_params(p):
    '''param_list : param COMMA param_list
                  | param'''
    
def p_param_id(p):
    '''param : ID COLON I32
              | ID COLON F64
              | ID COLON bool'''
    
def p_return_type(p):
    '''return_type : I32
                  | F64
                  | bool'''
    
def p_bool_type(p):
    '''bool : TRUE 
            | FALSE'''
#endregion
    
#region statements
def p_statement_function(p):
    '''statement : function_def
                | function_call'''

def p_statement_expression_statement(p):
    'statement : expression_statement'

def p_statement_var_declaration(p):
    'statement : var_declaration'

def p_statement_var_assignment(p):
    'statement : var_assignment'

def p_statement_if(p):
    'statement : IF condition block_statement'

def p_statement_if_else(p):
    'statement : IF condition block_statement statement_else'

def p_statement_else_block(p):
    'statement_else : ELSE block_statement'

def p_statement_else_if(p):
    'statement_else : ELSE statement_else_if'

def p_statement_else_if_block(p):
    'statement_else_if : IF condition block_statement'

def p_statement_else_if_with_else(p):
    'statement_else_if : IF condition block_statement statement_else'

def p_statement_while_statement(p):
    'statement : while_statement'

def p_statement_return_statement(p):
    'statement : return_statement'

def p_statement_for_statement(p):
    'statement : for_statement'

def p_statement_block_statement(p):
    'statement : block_statement'
#endregion

#region Operadores Relacionais
def p_condition_notequal(p):
    'condition : expression NOTEQUAL expression'

def p_condition_greaterequal(p):
    'condition : expression GREATEREQUAL expression'

def p_condition_lessequal(p):
    'condition : expression LESSEQUAL expression'

def p_condition_greater(p):
    'condition : expression GREATER expression'

def p_condition_less(p):
    'condition : expression LESS expression'

def p_condition_equals(p):
    'condition : expression EQUALS expression'
#endregion

#Region Operadores Logicos

def p_condition_and(p):
    'condition : condition AND condition2'

def p_condition_or(p):
    'condition : condition OR condition2'

def p_condition_not(p):
    'condition : NOT condition2'

def p_condition_expr(p):
    'condition : expression'

def p_condition2_expr(p):
    'condition2 : expression'

#endregion

def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'

def p_var_declaration(p):
    '''var_declaration : LET MUT ID ASSIGN expression SEMICOLON
                      | LET MUT param ASSIGN expression SEMICOLON'''

def p_var_declaration2(p):
    '''var_declaration : LET ID ASSIGN expression SEMICOLON
                      | LET param ASSIGN expression SEMICOLON'''

def p_var_assignment(p):
    'var_assignment : ID ASSIGN expression SEMICOLON'

def p_while_statement(p):
    'while_statement : WHILE condition block_statement'

def p_for_statement(p):
    'for_statement : FOR ID IN expression block_statement'

def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'

def p_block_statement(p):
    'block_statement : LBRACE statement_list RBRACE'

def p_expression_plus(p):
    'expression : expression PLUS term'

def p_expression_minus(p):
    'expression : expression MINUS term'

def p_term_modulo(p):
    'term : term MODULO factor'

def p_term_times(p):
    'term : term TIMES factor'

def p_term_divide(p):
    'term : term DIVIDE factor'

def p_expression_term(p):
    'expression : term'

def p_expression_range(p):
    'expression : expression RANGE term'

def p_term_factor(p):
    'term : factor'

def p_factor_number(p):
    'factor : NUMBER'

def p_factor_paren(p):
    'factor : LPAREN expression RPAREN'

def p_factor_boolean(p):
    '''factor : TRUE
              | FALSE'''

def p_factor_id(p):
    'factor : ID'

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
        while x > 2 {
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