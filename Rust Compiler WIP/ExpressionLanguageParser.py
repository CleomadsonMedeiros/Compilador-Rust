import ply.yacc as yacc
from ExpressionLanguageLex import tokens

# Regras do analisador sintático (parser)
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3] if p[3] != 0 else print("Erro: Divisão por zero")

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Erro de sintaxe!")

parser = yacc.yacc()

# Teste do parser
resultado = parser.parse("3 * 2")
print(resultado)