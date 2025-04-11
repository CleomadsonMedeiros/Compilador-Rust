
# 🦀 Documentação Sintática da Linguagem Rust

## 1. Estrutura do Programa

Um programa válido na linguagem **Rust** começa obrigatoriamente com uma função `main`, como mostra a seguinte regra:

```
program → main_function
main_function → "fn" "main" "(" ")" block_statement
```

O bloco principal e demais comandos são construídos a partir de listas de instruções (`statement_list`), que podem conter diversas formas de comandos (funções, variáveis, expressões, controle de fluxo etc.).

---

## 2. Comandos

Os comandos ou statements que a linguagem Rust suporta são os seguintes:

```
statement →
    function_def |
    function_call |
    expression_statement |
    var_declaration |
    var_assignment |
    if_statement |
    while_statement |
    return_statement |
    for_statement |
    block_statement
```

Cada um desses será detalhado a seguir.

---

### 2.1 Definições de Função

A linguagem suporta funções com ou sem parâmetros:

```
function_def →
    "fn" ID "(" param_list ")" "->" return_type block_statement |
    "fn" ID "(" ")" block_statement
```

Parâmetros são tipados, e o retorno também pode ser um dos seguintes tipos: `i32`, `f64` ou `bool`.

---

### 2.2 Chamadas de Função

Chamadas de função são suportadas com ou sem parâmetros e com ou sem ponto-e-vírgula:

```
function_call →
    ID "(" id_list ")" ";" |
    ID "(" ")" ";" |
    ID "(" id_list ")" |
    ID "(" ")"
```

---

### 2.3 Declarações e Atribuições de Variáveis

```
var_declaration →
    "let" "mut" ID "=" expression ";" |
    "let" "mut" param "=" expression ";" |
    "let" ID "=" expression ";" |
    "let" param "=" expression ";"

var_assignment →
    ID "=" expression ";"
```

---

### 2.4 Estruturas de Controle

#### If, Else e Else If

```
if_statement →
    "if" expression block_statement |
    "if" expression block_statement "else" block_statement |
    "if" expression block_statement if_statement
```

#### While

```
while_statement →
    "while" expression block_statement
```

#### For

```
for_statement →
    "for" ID "in" expression block_statement
```

#### Return

```
return_statement →
    "return" expression ";"
```

---

## 3. Expressões

A linguagem suporta as seguintes expressões aritméticas, relacionais e lógicas:

### 3.1 Aritméticas

```
expression →
    expression "+" term |
    expression "-" term |
    expression ".." term |
    term
term →
    term "*" factor |
    term "/" factor |
    term "%" factor |
    factor
factor →
    NUMBER |
    "(" expression ")" |
    TRUE |
    FALSE |
    ID
```

### 3.2 Relacionais

```
expression →
    expression "!=" condition |
    expression ">=" condition |
    expression "<=" condition |
    expression ">" condition |
    expression "<" condition |
    expression "==" condition
condition →
    term
```

### 3.3 Lógicas

```
expression →
    expression "&&" condition |
    expression "||" condition |
    "!" condition
```

---

## 4. Parâmetros e Tipos

Parâmetros tipados para funções e variáveis:

```
param →
    ID ":" I32 |
    ID ":" F64 |
    ID ":" BOOL

return_type →
    I32 | F64 | BOOL
```

---

## 5. Exemplo de Programa

```rust
fn main() {
  let mut x: i32 = 10;
  let y = 20;
  let resultado: f64 = 0.0;

  if x > y {
      x = x + 1;
  } else {
      x = x - 1;
  }

  while x < 20 {
      x = x + 2;
  }

  for i in 0..10 {
      let temp = i * 2;
  }

  fn soma(a: i32, b: f64, c: i32) -> f64 {
      return a + b;
  }
}
```
