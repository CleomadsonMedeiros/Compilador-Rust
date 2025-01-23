import ply.lex as lex

# Reservadas
reservadas = {
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN',
    'fn': 'FN', # Função
    'let': 'LET', # Variável Imutável
    'mut': 'MUT', # Variável Mutável
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'i32': 'I32',
    'f64': 'F64'
}

# Tokens
tokens = (
    "PLUS", 
    "MINUS", 
    "TIMES", 
    "DIVIDE", 
    "EQUAL",
    "LPAREN", 
    "RPAREN",
    "LBRACKET",
    "RBRACKET",
    "LBRACE",
    "RBRACE",
    "COMMA", 
    "NUMBER", 
    "ID",
    "SEMICOLON",
    "COLON",
    "DOT",
    "ARROW",
    "AND",
    "OR",
    "NOT",
    "LT", #Less Than
    "GT", #Greater Than
    "LE", #Less or Equal
    "GE", #Greater or Equal
    "EQ", #Equal
    "NE", #Not Equal
) + tuple(reservadas.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_ARROW = r'->'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

def t_NUMBER_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Identificador, caso seja uma palavra reservada, retorna a palavra reservada
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

# Ignorar espaços em branco
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comentários com // ou /* */
def t_COMMENT(t):
    r'//.*|/\*(.|\n)*?\*/'
    pass # Faz nada

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("if else")

print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
for tok in lexer:
  print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, tok.value, str(tok.lineno), str(tok.lexpos)))