# Dia 2: Calculadora Básica

## 🎯Desafio
Desenvolva um programa que realize operações básicas de matemática, como adição, subtração, multiplicação e divisão. 

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Operações Matemáticas em Python: Conheça como realizar operações matemáticas básicas usando os operadores +, -, * e /.
- Input e Output: Aprenda a receber entrada do usuário usando input() e mostrar resultados.

## 🔔Dica importante
- Você pode se deparar com um erro ao tentar usar o valor inserido pelo usuário na operação matemática... Tudo que o usuário insere vem como String, então, para fazer adição, subtração, multiplicação e divisão do número recebido, você vai precisar converter a String recebida para um inteiro ou para float (se quiser que sua calculadora faça contas com números decimais).
- Lembre-se que float em Python é utilizando . e não , (2.5 e não 2,5). Você pode fazer um tratamento extra no seu código se quiser evitar que o uso da , cause um erro de código, mas faça apenas se quiser tentar algo a mais, para o desafio não é necessário.
- Você pode fazer alguns tratamentos para lidar com casos do tipo divisão por 0.



## 💡Resolução do Desafio

### Função `realizar_operacao`:

- **Parâmetros:**
  - `operacao`: Operação desejada (+, -, *, /).
  - `num1` e `num2`: Números para a operação.
- **Lógica de Operação:**
  - Utiliza estruturas condicionais para determinar qual operação realizar.
  - Lida com casos especiais, como a divisão por zero.
- **Retorno:**
  - Retorna o resultado da operação ou `None` em caso de erro.

### Operadores Lógicos:

- `==`: Verifica igualdade.
- `!=`: Verifica diferença.
- `and`: Operador lógico "E". Retorna True se ambas as condições forem verdadeiras.
- `or`: Operador lógico "OU". Retorna True se pelo menos uma das condições for verdadeira.
- `not`: Operador lógico "NÃO". Inverte o valor de verdade de uma expressão.

### Função `main`:

- Lógica da Função `main`:
  - Solicita a operação e os números ao usuário.
  - Utiliza tratamento de erro para lidar com exceções.
  - Chama `realizar_operacao` para efetuar o cálculo.
  - Imprime o resultado, se houver.

### Chamada da Função Principal:

```
pythonCopy codeif __name__ == "__main__":
    main()
```

- Essa construção verifica se o script está sendo executado diretamente.
- Garante que o bloco de código dentro de `main()` seja executado apenas nesse caso.
- Facilita a modularidade e reutilização do código.

### Uso de F-Strings:

- F-strings são utilizadas para formatar a string de saída.
- Permitem a incorporação de variáveis diretamente na string, tornando-a concisa e legível.

## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script várias vezes para ver se ele se comporta como esperado para cada um dos valores abaixo:

```
TESTE 01: 1 + 5 -> 6
TESTE 02: 5 - 1 -> 4
TESTE 03: 2 x 30 -> 60
TESTE 04: 21 / 7 -> 3
TESTE 05: 10 / 0 -> Não é possível dividir por zero
TESTE 06: 1 + -5 -> -4
TESTE 07: 5 - -1 -> 6
TESTE 08: 2 x -30 -> -60
TESTE 09: -21 / 7 -> -3
TESTE 10: -10 / 0 -> Não é possível dividir por zero
```

Você pode fazer outros testes caso ache necessário.