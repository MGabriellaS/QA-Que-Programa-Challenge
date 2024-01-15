# Dia 5: Geração de Números Aleatórios

## 🎯Desafio

Desenvolva um script que gere e exiba uma lista com 6 números aleatórios entre 1 e 60, sem repetições (ou seja, dentre os seis números selecionados, não podem existir números repetidos), para que você possa fazer um jogo da Mega Sena.

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?

- Laços de repetição (while)
- Módulo random: Você precisará aprender como usar o módulo random em Python para gerar números aleatórios.
- Listas em Python: É importante entender como criar e adicionar dados em listas (pode usar o método append() para adicionar) de maneira a armazenar os números aleatórios gerados.

## 🔔Dica importante

- Você pode usar o módulo random para gerar números aleatórios entre 1 e 60, e em seguida, adicionar esses números a uma lista.
- Certifique-se de verificar se o número gerado não está na lista antes de adicioná-lo para evitar repetições. Continue gerando números até ter uma lista com 6 números aleatórios não repetidos.

## 💡Resolução do Desafio

1. `import random`: Importa o módulo random, que é necessário para gerar números aleatórios.
2. `gerar_numeros_mega_sena()`: Define uma função que retorna uma lista com 6 números aleatórios não repetidos.
3. `numeros_mega_sena = []`: Inicializa uma lista vazia para armazenar os números gerados.
4. `while len(numeros_mega_sena) < 6:`: Inicia um loop que continua até ter 6 números na lista.
5. `numero_aleatorio = random.randint(1, 60)`: Gera um número aleatório entre 1 e 60.
6. `if numero_aleatorio not in numeros_mega_sena:`: Verifica se o número gerado já está na lista.
7. `numeros_mega_sena.append(numero_aleatorio)`: Adiciona o número à lista se não estiver lá.
8. `return numeros_mega_sena`: Retorna a lista completa.
9. `numeros_gerados = gerar_numeros_mega_sena()`: Chama a função para gerar os números e armazena o resultado em uma variável.

## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```



Você pode executar seu código várias vezes para ver que, de fato, os 6 números são gerados aleatoriamente e sem repetições.
