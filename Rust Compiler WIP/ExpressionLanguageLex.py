import ply.lex as lex

# Palavras reservadas
reservadas = {
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN',
    'fn': 'FN',
    'let': 'LET',
    'mut': 'MUT',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    'main': 'MAIN'
}

# Tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'GREATER',
    'LESS',
    'EQUALS',
    'LBRACE',
    'RBRACE',
    'ID',
    'ASSIGN',
    'NOTEQUAL',
    'GREATEREQUAL',
    'LESSEQUAL',
    #'COMMA',
    #'ARROW',
    'SEMICOLON',
    'MODULO',
    'NOT',
    'OR',
    'AND'
) + tuple(reservadas.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATER = r'>'
t_LESS = r'<'
t_EQUALS = r'=='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
#t_COMMA = r','
#t_ARROW = r'->'
t_SEMICOLON = r';'
t_RANGE = r'\.\.'
t_NOTEQUAL = r'!='
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_MODULO = r'%'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)
    
lexer = lex.lex()