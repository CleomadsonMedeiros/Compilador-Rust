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
    print("Análise sintática concluída.")

def p_expressao(p):
    '''expressao : termo expressao_linha'''
    pass

def p_expressao_linha(p):
    '''expressao_linha : PLUS termo expressao_linha
                       | MINUS termo expressao_linha
                       | vazio'''
    pass

def p_termo(p):
    '''termo : fator termo_linha'''
    pass

def p_termo_linha(p):
    '''termo_linha : TIMES fator termo_linha
                   | DIVIDE fator termo_linha
                   | vazio'''
    pass

def p_fator(p):
    '''fator : LPAREN expressao RPAREN
             | ID
             | NUMBER'''
    pass

def p_vazio(p):
    'vazio :'
    pass

def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}'")
    else:
        print("Erro de sintaxe no final da entrada")

# Construção do parser
parser = yacc.yacc()

parser.parse(data)