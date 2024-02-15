# Dia 7: Temporizador/Contador

## 🎯Desafio

Crie um programa que funcione como um temporizador (contagem progressiva) ou contador regressivo. O usuário vai poder escolher entre as duas opções.

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?

- Módulo time: Aprenda a usar o módulo time para criar um temporizador.
- Loops e Condições: Use loops e condições para controlar o tempo.

## 🔔Dica importante

- Você pode usar o módulo time para realizar contagens regressivas. Inicie um temporizador com um determinado tempo (em segundos) e crie um loop que decremente esse tempo a cada segundo até que atinja zero.
- Você pode oferecer opções ao usuário, como definir o tempo desejado para o temporizador ou escolher entre um temporizador regressivo e um contador progressivo.
- Mostre o tempo restante de forma clara para o usuário enquanto o temporizador estiver em andamento.

## 💡Resolução do Desafio

1. O temporizador é baseado em segundos e utiliza a biblioteca `time` para pausar a execução do programa.
2.  A função `time.sleep` é frequentemente usada para introduzir atrasos ou pausas no código. Ela aceita um argumento, que é o número de segundos pelo qual o programa deve ficar em pausa.
3. Foi criado as seguintes funções:
   1. **`temporizador_progressivo(tempo_total)`**
      - Esta função realiza uma contagem progressiva do tempo.
      - Recebe como parâmetro o tempo total em segundos.
      - Utiliza um loop `while` para imprimir o tempo passado a cada segundo, pausando por 1 segundo entre as iterações.
   2. **`temporizador_regressivo(tempo_total)`**
      - Esta função realiza uma contagem regressiva do tempo.
      - Recebe como parâmetro o tempo total em segundos.
      - Utiliza um loop `while` para imprimir o tempo restante a cada segundo, pausando por 1 segundo entre as iterações.
   3. **`main()`**
      - A função principal que inicia o programa.
      - Exibe uma mensagem de boas-vindas e solicita ao usuário escolher entre um temporizador progressivo (`'P'`) ou regressivo (`'R'`).
      - Com base na escolha, solicita ao usuário o tempo total desejado em segundos e chama a função correspondente (`temporizador_progressivo` ou `temporizador_regressivo`).
      - Lida com escolhas inválidas, exibindo uma mensagem de erro.


## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```



Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

```
TESTE 01: Crie um temporizador de 12 segundos e verifique se ele funciona corretamente.
TESTE 02: Crie um contador regressivo de 12 segundos e verifique se ele funciona corretamente.
```



Você pode fazer outros testes caso ache necessário.
