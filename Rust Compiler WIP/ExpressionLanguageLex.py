import ply.lex as lex

reservadas = {
    # Exemplo de palavras reservadas (caso precise mais tarde)
    # 'while': 'WHILE',
    # 'true': 'TRUE',
    # 'false': 'FALSE',
    # 'return': 'RETURN',
    # 'fn': 'FN',
    # 'let': 'LET',
    # 'mut': 'MUT',
    # 'if': 'IF',
    # 'else': 'ELSE',
    # 'for': 'FOR',
    # 'in': 'IN',
}

# Tokens
tokens = (
    "PLUS", 
    "MINUS", 
    "TIMES", 
    "DIVIDE", 
    "LPAREN", 
    "RPAREN",
    "NUMBER",
    "ID"
) + tuple(reservadas.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificador (ID), se for uma palavra reservada, retorna a palavra reservada
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Se for uma palavra reservada, retorna o nome
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comentários (não geram tokens)
def t_COMMENT(t):
    r'//.*|/\*(.|\n)*?\*/'
    pass  # Simplesmente ignora os comentários

# Erro de token
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
3 + 4 * (2 - 1)
'''

lexer.input(data)

# Lendo os tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

