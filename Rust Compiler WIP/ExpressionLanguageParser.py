import ply.yacc as yacc
from ExpressionLanguageLex import tokens

def p_program(p):
    'program : statement'
    p[0] = p[1]

def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]

def p_statement_if(p):
    'statement : if_statement'
    p[0] = p[1]

def p_if_statement(p):
    'if_statement : IF LPAREN condition RPAREN LBRACE expression RBRACE'
    p[0] = p[6] if p[3] else False

def p_if_else_statement(p):
    'if_statement : IF LPAREN condition RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE'
    p[0] = p[6] if p[3] else p[10]

def p_condition_greater(p):
    'condition : expression GREATER expression'
    p[0] = p[1] > p[3]

def p_condition_less(p):
    'condition : expression LESS expression'
    p[0] = p[1] < p[3]

def p_condition_equals(p):
    'condition : expression EQUALS expression'
    p[0] = p[1] == p[3]

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    if p[3] == 0:
        print("Erro: Divisão por zero")
        p[0] = None
    else:
        p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_boolean(p):
    '''factor : TRUE
              | FALSE'''
    p[0] = True if p[1] == 'true' else False

def p_factor_paren(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Erro de sintaxe")

parser = yacc.yacc()

print(parser.parse("if (1 < 2) { 3*4 } else { 4 }"))