import ply.yacc as yacc
from ExpressionLanguageLex import tokens, data

"""
Gramática

Inicio -> exp
exp -> T exp'
exp' -> + T exp'
      | - T exp'
      | ε
T -> F T'
T' -> * F T'
    | / F T'
    | ε
F -> ( exp )
    | id
    | num
"""

def p_inicio(p):
    'inicio : expressao'
    p[0] = p[1]
    print(f"Resultado do cálculo: {p[0]}")

def p_expressao(p):
    '''expressao : termo expressao_linha'''
    p[0] = p[1] + p[2]

def p_expressao_linha(p):
    '''expressao_linha : PLUS termo expressao_linha
                       | MINUS termo expressao_linha
                       | vazio'''
    if len(p) == 4:
        if p[1] == '+':
            p[0] = p[2] + p[3]
        elif p[1] == '-':
            p[0] = -p[2] + p[3]
    else:
        p[0] = 0

def p_termo(p):
    '''termo : fator termo_linha'''
    p[0] = p[1] * p[2]

def p_termo_linha(p):
    '''termo_linha : TIMES fator termo_linha
                   | DIVIDE fator termo_linha
                   | vazio'''
    if len(p) == 4:
        if p[1] == '*':
            p[0] = p[2] * p[3]
        elif p[1] == '/':
            p[0] = p[2] / p[3]
    else:
        p[0] = 1

def p_fator(p):
    '''fator : LPAREN expressao RPAREN
             | NUMBER'''
    if len(p) == 4:
        p[0] = p[2]
    elif isinstance(p[1], int):
        p[0] = p[1]
    else:
        p[0] = 0

def p_vazio(p):
    'vazio :'
    p[0] = 0

def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}'")
    else:
        print("Erro de sintaxe no final da entrada")

# Construção do parser
parser = yacc.yacc()

parser.parse(data)