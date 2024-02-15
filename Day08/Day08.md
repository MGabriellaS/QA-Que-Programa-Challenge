# Dia 8: Lista de Tarefas

## 🎯Desafio

Desenvolva uma aplicação simples para gerenciar uma lista de tarefas, permitindo adicionar e remover itens.

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?

- Manipulação de Listas: Aprenda a adicionar (append()), remover (pop())e listar itens em uma lista.
- Input do usuário: Entenda como interagir com o usuário para gerenciar a lista de tarefas.
- Laços de repetição for usando enumerate.

## 🔔Dica importante

- Você pode usar uma lista em Python para armazenar as tarefas. Crie funções que permitam adicionar tarefas à lista, remover tarefas existentes e listar todas as tarefas.
- Ofereça um menu ao usuário com opções para adicionar uma nova tarefa, remover uma tarefa existente, listar todas as tarefas e sair.
- Lembre que você não pode encerrar seu programa ao realizar uma ação, ele tem sempre que ficar ativo pois ao ser encerrado, todos os dados inseridos anteriormente são perdidos, portanto, você pode contruir seu código num loop infinito (while True) até que o usuário escolha a opção de sair.
- Considere tratar casos em que o usuário tenta remover uma tarefa que não existe na lista.

## 💡Resolução do Desafio

### Funções:

1. **`adicionar_tarefa(lista_tarefas, nova_tarefa)`**
   - Adiciona uma nova tarefa à lista de tarefas.
   - Utiliza o método `append` da lista para adicionar `nova_tarefa` ao final da lista.
   - Imprime uma mensagem informando que a tarefa foi adicionada com sucesso.
2. **`remover_tarefa(lista_tarefas, tarefa)`**
   - Remove uma tarefa da lista de tarefas, se ela existir na lista.
   - Utiliza o método `remove` da lista para remover a primeira ocorrência de `tarefa`.
   - Imprime uma mensagem informando se a tarefa foi removida com sucesso ou se não foi encontrada na lista.
3. **`listar_tarefas(lista_tarefas)`**
   - Lista todas as tarefas presentes na lista.
   - Verifica se a lista de tarefas está vazia antes de tentar listar.
   - Utiliza um loop `for` para iterar sobre a lista e imprime cada tarefa numerada.
4. **`main()`**
   - Função principal que inicia o programa.
   - Cria uma lista vazia (`lista_tarefas`) para armazenar as tarefas.
   - Utiliza um loop infinito (`while True`) para manter o programa em execução até que o usuário escolha sair (`'4'`).
   - Apresenta um menu ao usuário com opções para adicionar, remover, listar tarefas ou sair.
   - Realiza as ações correspondentes com base na escolha do usuário.

### `append`:

A função `append` é um método de lista em Python. Quando chamado em uma lista, ele adiciona um elemento ao final da lista. No contexto do código:

```
pythonCopy codedef adicionar_tarefa(lista_tarefas, nova_tarefa):
    lista_tarefas.append(nova_tarefa)
    print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')
```

- `lista_tarefas.append(nova_tarefa)`: Adiciona a `nova_tarefa` ao final da lista `lista_tarefas`.
- `print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')`: Imprime uma mensagem indicando que a tarefa foi adicionada com sucesso.

### Fluxo do Programa:

- O programa inicia com uma lista vazia de tarefas.
- O usuário é apresentado a um menu com opções.
- Dependendo da escolha do usuário, as funções são chamadas para adicionar, remover, listar tarefas ou sair do programa.
- As tarefas são armazenadas em uma lista (`lista_tarefas`) que persiste durante a execução do programa.


## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```



Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

```
TESTE 01: Adicione várias tarefas à lista e verifique se elas são exibidas corretamente.
TESTE 02: Remova tarefas da lista e certifique-se de que a remoção seja bem-sucedida.
TESTE 03: Liste todas as tarefas e verifique se elas estão sendo exibidas corretamente.
TESTE 04: Teste situações em que o usuário tenta remover uma tarefa que não existe na lista.
TESTE 05: Teste situações em que o usuário tenta remover uma tarefa mas a lista está vazia.
TESTE 06: Teste situações em que o usuário tenta mostrar todas as tarefas mas a lista está vazia.
```



Você pode fazer outros testes caso ache necessário.
