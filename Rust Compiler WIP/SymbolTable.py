symbolTable = []
I32 = 'i32'
F64 = 'f64'
BOOL = 'bool'

TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
VARIABLE = 'var'
SCOPE = 'scope'
OFFSET = 'offset'
SP = 'sp'
MULTABLE = 'multable'

DEBUG = 0

curoffset = 0
def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', symbolTable)

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope
    printTable()

def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]
    printTable()

def addVar(name, type="dynamic", multable=False, offset=None):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE: type, MULTABLE: multable, OFFSET: offset}
    printTable()

def addFunction(name, params, type="dynamic"):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE: type}
    printTable()

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def getScope(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][SCOPE]
    return None

def main():
    global DEBUG
    DEBUG = -1
 
    print('\n# Criando escopo main')
    beginScope('main')

    print ('\n# Adicionando Vinculavel funcao some')
    addFunction('some', ['a', I32, 'b', I32], I32)
    print('\n# Criando escopo some')
    beginScope('some')

    print('\n# Adicionando var a do tipo I32')
    addVar('a', I32)
    print('\n# Pegar escopo de var a')
    print(getScope('a'))

    print('\n# Adicionando var b do tipo I32')
    addVar('b', I32)

    print('\n# Consultando bindable')
    print(str(getBindable('sumparabola')))

    print('\n# Consultando bindable')
    print(str(getBindable('some')))

    print('\n# Removendo escopo some')
    endScope()

if __name__ == "__main__":
    main()