# Dia 3: Verificador de Palíndromos

## 🎯Desafio
Crie um script que verifica se uma palavra ou frase fornecida pelo usuário é um palíndromo. Palíndromo é uma palavra ou uma frase que de frente pra trás e de trás pra frente são iguais, por exemplo, "ovo", "radar" e "Ame o poema".

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Manipulação de Strings: Entenda como manipular strings para verificar palíndromos, usando funções como upper(), lower(), replace().
- Condições (if-else): Aprenda a usar estruturas condicionais para verificar resultados.
- Laços de repetição (for ou while)

## 🔔Dica importante
- Lembre-se de remover espaços em branco, pontuação, caracteres especiais e converter toda a entrada em letras minúsculas ou maiúsculas antes de verificar se é um palíndromo.
- Você pode utilizar laços de repetição for ou while para verificar os caracteres da palavra ou frase.
- Caso deseje implementar algo mais avançado, poderia cuidar também de caracteres acentuados, substituíndo-os por caracteres sem acento.



## 💡Resolução do Desafio

1. **Função `formatar_texto`**:
   - **Entrada:** Recebe uma string (`texto`) como entrada.
   - **Saída:** Retorna uma versão formatada da string sem espaços, vírgulas, pontos, exclamações e interrogações, convertendo todos os caracteres para minúsculas.
   - Lógica:
     - Uma lista chamada `caracteres_remover` é criada, contendo os caracteres que desejamos remover da string.
     - Utiliza-se um loop `for` para percorrer cada caractere na string `texto`.
     - Verifica se o caractere (convertido para minúsculas) não está na lista `caracteres_remover`.
     - Se o caractere não estiver na lista, ele é adicionado à string `texto_formatado`.
     - A string `texto_formatado` é retornada como resultado.
2. **Função `inverter_texto`**:
   - **Entrada:** Recebe uma string (`texto`) como entrada.
   - **Saída:** Retorna uma versão invertida da string.
   - Lógica:
     - Utiliza-se o slicing (`texto[::-1]`) para inverter a string e retorna o resultado.
3. **Função `eh_palindromo`**:
   - **Entrada:** Recebe uma string (`texto`) como entrada.
   - **Saída:** Retorna `True` se a string for um palíndromo e `False` caso contrário.
   - Lógica:
     - Chama a função `inverter_texto` para obter a versão invertida da string.
     - Compara se a string original é igual à sua versão invertida.
     - Retorna o resultado da comparação.
4. **Código Principal**:
   - Solicita ao usuário uma entrada de palavra ou frase.
   - Chama a função `formatar_texto` para remover espaços e caracteres indesejados, convertendo para minúsculas.
   - Chama a função `eh_palindromo` para verificar se a entrada formatada é um palíndromo.
   - Imprime o resultado.

## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```



Você pode então realizar alguns testes em seu script. Execute seu script várias vezes para ver se ele se comporta como esperado para cada um dos valores abaixo:

```
TESTE 01: "ovo" -> É um palíndromo
TESTE 02: "arara" -> É um palíndromo
TESTE 03: "reconhecer" -> Não é um palíndromo
TESTE 04: "Python" -> Não é um palíndromo
TESTE 05: "A man, a plan, a canal, Panama!" -> É um palíndromo
TESTE 06: "Anita lava a tina" -> Não é um palíndromo
TESTE 07: "Was it a car or a cat I saw?" -> É um palíndromo
TESTE 08: "Hello, World!" -> Não é um palíndromo
```



Você pode fazer outros testes caso ache necessário.