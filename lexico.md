# 🦀 Compilador Rust - Elementos Léxicos

#### 1. Palavras reservadas.

 Apresenta as seguintes palavras reservadas: **while**, **true**, **false**, **return**, **fn**, **let**, **mut**, **if**, **else**, **for** e **in**.

#### 2. Precedência de expressões

 Apresenta os operadores aritméticos de **soma** (+), **multiplicação** (*), **subtração** (-), **divisão** (/) e **módulo** (%). Também apresenta o **operador** = para atribuições. Possui ainda os operadores unários **negação aritmética** (-), **negação lógica** (!). Bem como, os operadores relacionais de comparação **igualdade** (==), **não igualdade** (!=), **menor que** (<), **maior que** (>), **menor ou igual que** (<=) e **maior ou igual que** (>=); e os operadores lógicos **E** (&&) e **OU** (||). Estes possuem a seguinte tabela de precedência em ordem de força decrescente

| Operador                | Associatividade        |
|:-----------------------:|:----------------------:|
| Unário `- * !`          |                        |
| `* / %`                 | Esquerda para direita  |
| `+ -`                   | Esquerda para direita  |
| `== != < > <= >=`       | Requer parênteses      |
| `&&`                    | Esquerda para direita  |
| `\|\|`                    | Esquerda para direita  |
| `= += -= *= /= %=`      | Direita para esquerda  |


#### 3. Delimitadores

Comandos Rust utilizam ";" (ponto e vírgula) como delimitador. Parâmetros de funções utilizam "," (vírgula). Além disso,  utiliza os delimitadores ( ) (parênteses) para agrupamento de expressões. Por fim, também é utilizado o delimitador { } (chaves) para blocos de comando.

#### 4. Identificadores

Para identificadores, apresenta uma regra bastante empregada em diferentes linguagens de programação. Aceita como identificador válido qualquer sequência de símbolos iniciada por **letras** ou _ (underscore). Após esse símbolo inicial, o identificador pode conter **letras**, _ e **números**. Abaixo, alguns exemplos de identificadores válidos:

```rust
let nome = "válido";
let _comeca_underscore = "válido";
let minhaVar123 = "válido";
let CONSTANTE = "válido";
```

#### 5. Números

Rust dá suporte a números inteiros e com ponto flutuante. Os números inteiros têm variantes que basicamente indicam o número de bits suportados e cada variante pode ser não assinada ou assinada. As variantes não assinadas iniciam-se com a letra 'u', elas se referem a inteiros sem sinal, não suportando números negativos. Já as assinadas iniciam-se com a letra 'i' e se refere aos inteiros com sinal, ou seja, é capaz de suportar números negativos e positivos. Números assinados são armazenados utilizando a representação de complemento de dois. Em relação aos números de ponto flutuante existem dois tipos, o **f32** que tem 32bits e serve para números de ponto flutuantes de precisão simples, e o **f64** que tem 64bits e serve para números de ponto flutuante de precisão dupla. Eles são representados usando o padrão IEEE-754.

#### 6. Condicionais

**if-else**, avalia condições booleanas.
```rust
if x == 4 {
    println!("x é quatro");
} else if x == 3 {
    println!("x é três");
} else {
    println!("x é alguma coisa");
}
```

#### 7. Loops

**while**, continua a execução de determinado bloco de código enquanto a condição for verdadeira. 
```rust
let mut i = 0;

while i < 10 {
    println!("hello world");
    i = i + 1;
}
```
**for in**, continua a execução em determinada coleção iterando por todos elementos.
```rust
let v = &["maçãs", "bolo", "café"];

for text in v {
    println!("Eu gosto {}.", text);
}
```

#### 8. Erros
Qualquer coisa que não se enquadre em nenhum dos sete itens apresentados, é considerado como um erro léxico.

Adicionalmente,  ignora espaços em branco e tabulações. Além do mais,  também ignora quebras de linha, mas as utiliza para informar ao léxico em que ponto ele se encontra no processo de análise. Essa informação é recuperada através da variável **lineno**.
