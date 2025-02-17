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
#region statements
def p_statement_expression_statement(p):
    'statement : expression_statement'

def p_statement_var_declaration(p):
    'statement : var_declaration'

def p_statement_var_assignment(p):
    'statement : var_assignment'

def p_if_statement(p):
    'statement : IF LPAREN condition RPAREN LBRACE expression RBRACE'

def p_if_else_statement(p):
    'statement : IF LPAREN condition RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE'

def p_statement_while_statement(p):
    'statement : while_statement'

def p_statement_return_statement(p):
    'statement : return_statement'

def p_statement_for_statement(p):
    'statement : for_statement'

def p_statement_block_statement(p):
    'statement : block_statement'
#endregion

#Region Operadores Relacionais
def p_condition_notequal(p):
    'condition : expression NOTEQUAL expression'

def p_condition_greaterequal(p):
    'condition : expression GREATEREQUAL expression'

def p_condition_lessequal(p):
    'condition : expression LESSEQUAL expression'
#-END

#Region Operadores Logicos

def p_condition_and(p):
    'condition : condition AND condition'

def p_condition_or(p):
    'condition : condition OR condition'

def p_condition_not(p):
    'condition : NOT condition'

def p_condition_expr(p):
    'condition : expression'

def p_condition_paren(p):
    'condition : LPAREN condition RPAREN'
#endregion

def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'

def p_var_declaration(p):
    'var_declaration : LET MUT ID ASSIGN expression SEMICOLON'

def p_var_declaration2(p):
    'var_declaration : LET ID ASSIGN expression SEMICOLON'

def p_var_assignment(p):
    'var_assignment : ID ASSIGN expression SEMICOLON'

def p_while_statement(p):
    'while_statement : WHILE LPAREN expression RPAREN block_statement'

def p_for_statement(p):
    'for_statement : FOR ID IN expression block_statement'

def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'

def p_block_statement_braces(p):
    'block_statement : LBRACE statement_list RBRACE'

def p_condition_greater(p):
    'condition : expression GREATER expression'

def p_condition_less(p):
    'condition : expression LESS expression'

def p_condition_equals(p):
    'condition : expression EQUALS expression'

def p_expression_plus(p):
    'expression : expression PLUS term'
    # p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    # p[0] = p[1] - p[3]

def p_term_modulo(p):
    'term : term MODULO factor'

def p_term_times(p):
    'term : term TIMES factor'
    # p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    # p[0] = p[1] / p[3] if p[3] != 0 else print("Erro: Divisão por zero")

def p_expression_term(p):
    'expression : term'
    # p[0] = p[1]

def p_expression_range(p):
    'expression : expression RANGE term'

def p_term_factor(p):
    'term : factor'
    # p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    # p[0] = p[1]

def p_factor_paren(p):
    'factor : LPAREN expression RPAREN'
    # p[0] = p[2]

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
        let mut x = 5;
        x + 1;
        let y = 4;
        1 + 1;
        3 - 2;
        x = y + 4;
        while (1) {
        1 + 1;
        2 / 2;
        }
        for x in 1..10 / 5 {
        0 + 1;
        }
        return x;                 
    }     
''')
print(resultado)