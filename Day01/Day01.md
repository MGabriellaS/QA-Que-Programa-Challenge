# Dia 1: Identificador de Números Pares e Ímpares

## 🎯Desafio

Desenvolver um programa que solicita ao usuário para inserir um número, e então verifica se o número é par ou ímpar e exibindo uma mensagem informativa para o usuário.

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?

- Entrada de dados em Python: Aprenda a usar funções como input() para coletar dados do usuário.
- Estruturas de controle (if/else): Entenda como utilizar if/else para implementar a lógica de verificação de números pares e ímpares.
- Operadores matemáticos em Python: Conheça o operador de módulo (%) para determinar se um número é divisível por outro (neste caso, por 2).

## 💡Resolução do desafio

1. Na primeira(arquivo:**01.py**) opção de código foi projetado para lidar com a entrada do usuário, fornecendo feedback apropriado em caso de erro, e então verificar se o número inserido é par ou ímpar.

   Nesse caso além de aprender a coletar dados com a função **input()** , aprendi também o uso de:

   - **`try` e `except`:**Ambos são usados para manipulação de exceções (erros) em Python. Basicamente, quando você coloca um bloco de código dentro de `try`, o Python tenta executar esse bloco. Caso uma exceção do tipo`ValueError` ocorra durante a execução, o controle do programa é transferido para o bloco `except` correspondente. Isso é útil para lidar com situações em que você espera que ocorram erros e deseja fornecer um tratamento específico para esses casos.
   - **`if numero % 2 == 0:`**Verifica se o número é par usando o operador `%` (módulo), que retorna o resto da divisão por 2. Se o resto for zero, o número é par.
   - **`else:`:**Este bloco é executado se nenhum erro ocorrer durante a execução do bloco `try`. Aqui, você tem a lógica principal após a obtenção bem-sucedida do número.
   - **`print(f"{numero} é um número par.")` e `print(f"{numero} é um número ímpar.")`:** Exibe mensagens indicando se o número é par ou ímpar, usando f-string para incluir o valor de `numero` nas mensagens.

   

2. No segundo código do arquivo:**02.py** adicionei a seguinte mudança:

   - **`def verificar_paridade(numero):`:**Define uma função chamada `verificar_paridade` que recebe um número como parâmetro e utiliza o operador ternário para retornar "par" se o número for divisível por 2 e "ímpar" caso contrário.
   - Nesse caso no **`else`** se nenhuma exceção ocorrer no bloco `try`, o código dentro dele é executado. Então ele chamará a função `verificar_paridade` com o número inserido. E irá imprimir uma mensagem indicando se o número é par ou ímpar.

## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```



Você pode então realizar alguns testes em seu script. Execute seu script várias vezes para ver se ele se comporta como esperado para cada um dos valores abaixo:

```
TESTE 01: 5 -> ímpar 
TESTE 02: 898 -> par
TESTE 03: -5 -> ímpar
TESTE 04: -4 -> par
TESTE 05: 0 -> par
```



Você pode fazer outros testes caso ache necessário.

