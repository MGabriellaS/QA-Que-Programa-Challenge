def adicionar_tarefa(lista_tarefas, nova_tarefa):
    """Adiciona uma nova tarefa à lista."""
    lista_tarefas.append(nova_tarefa)
    print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')


def remover_tarefa(lista_tarefas, tarefa):
    """Remove uma tarefa da lista, se existir."""
    if tarefa in lista_tarefas:
        lista_tarefas.remove(tarefa)
        print(f'Tarefa "{tarefa}" removida com sucesso!')
    else:
        print(f'Tarefa "{tarefa}" não encontrada na lista.')


def listar_tarefas(lista_tarefas):
    """Lista todas as tarefas da lista."""
    if not lista_tarefas:
        print("Lista de tarefas vazia.")
    else:
        print("Lista de Tarefas:")
        for index, tarefa in enumerate(lista_tarefas, start=1):
            print(f"{index}. {tarefa}")


def main():
    lista_tarefas = []

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Listar Tarefas")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            nova_tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(lista_tarefas, nova_tarefa)
        elif escolha == '2':
            tarefa_a_remover = input("Digite a tarefa a ser removida: ")
            remover_tarefa(lista_tarefas, tarefa_a_remover)
        elif escolha == '3':
            listar_tarefas(lista_tarefas)
        elif escolha == '4':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
