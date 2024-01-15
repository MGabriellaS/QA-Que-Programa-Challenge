# Dia 4: Contador de Palavras

## 🎯Desafio
Desenvolva um programa que conte o número de palavras em um texto fornecido pelo usuário. O programa deve ser capaz de separar as palavras em um texto e determinar quantas palavras estão presentes.

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Manipulação de Strings: Você precisará entender como usar funções de strings, como split(), para separar o texto em palavras.
- Laços de repetição (for ou while)

## 🔔Dica importante
- Use a função split() para dividir o texto em palavras. Por padrão, essa função divide o texto em palavras separadas por espaços em branco.
- Considere que números e caracteres especiais são consideradas palavras, por exemplo "Oi , " e "18 anos" a vírgula e o número 18 são consideradas palavras, nestes dois exemplos, o seu código deveria retornar 2 palavras
- Relaxem em relação ao plural de "palavra" na saída do seu código (TESTE 09) no caso do número de palavras do texto ser 1, não precisa se preocupar em tratar o texto pra imprimir no singular caso a contagem der 1, mas pode ser um plus que você pode implementar no seu código caso deseje.



## 💡Resolução do Desafio

1. A função `contar_palavras` recebe um texto como entrada.
2. Utiliza a função `split()` para dividir o texto em palavras. Por padrão, `split()` usa espaços em branco para separar as palavras.
3. Retorna o número de palavras contadas usando a função `len()`.
4. O código principal solicita ao usuário inserir um texto, chama a função `contar_palavras` e imprime o resultado.

## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```



Você pode então realizar alguns testes em seu script. Execute seu script várias vezes para ver se ele se comporta como esperado para cada um dos valores abaixo:

```
TESTE 01: "Isso é um teste." -> O texto contém 4 palavras.
TESTE 02: "   Olá,    mundo!   " -> O texto contém 2 palavras.
TESTE 03: "Palavra Palavra palavra" -> O texto contém 3 palavras.
TESTE 04: "Este é um teste de contagem de palavras." -> O texto contém 8 palavras.
TESTE 05: "" -> Número de palavras: O texto contém 0 palavras.
TESTE 06: "Maria tem 10 anos." -> O texto contém 4 palavras.
TESTE 07: "Olá ,  Mundo" -> O texto contém 3 palavras.
TESTE 08: "Em uma tarde ensolarada, 3 crianças brincavam no parque. De repente, encontraram um mapa misterioso, com anotações enigmáticas: 'Vire à esquerda, depois à direita, e avance 100 passos!' Eles, empolgados, seguiram as instruções cuidadosamente, contando cada passo com atenção. No caminho , encontraram diversos obstáculos: pedras, galhos e até um riacho raso. O mapa os levou a uma árvore antiga, com raízes grossas e folhas densas. 'Aqui deve ser!', exclamou João, o mais velho. Mas,   sob a árvore, só encontraram uma caixa vazia e um bilhete: 'A verdadeira aventura está na jornada, não no destino. Parabéns por chegarem até aqui!' Desapontados, mas ainda animados, decidiram continuar explorando. 'Vamos ver o que mais podemos descobrir!', disse Maria, a mais aventureira do grupo. E assim, a busca por tesouros se transformou em uma tarde de descobertas e diversão. No final, o que realmente importava era a amizade e as memórias que criaram juntos." -> O texto contém 151 palavras.
TESTE 09: "Oi" -> O texto contém 1 palavras.
```



Você pode fazer outros testes caso ache necessário.