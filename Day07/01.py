import time


def temporizador_progressivo(tempo_total):
    tempo_passado = 0
    while tempo_passado <= tempo_total:
        print(f"Tempo passado: {tempo_passado} segundos")
        time.sleep(1)
        tempo_passado += 1


def temporizador_regressivo(tempo_total):
    while tempo_total > 0:
        print(f"Tempo restante: {tempo_total} segundos")
        time.sleep(1)
        tempo_total -= 1


def main():
    print("Bem-vindo ao Temporizador!")

    escolha = input("Escolha 'P' para temporizador progressivo ou \n\
        'R' para temporizador regressivo: ").upper()

    if escolha == 'P':
        tempo_total = int(input("Digite o tempo total desejado (em seg): "))
        temporizador_progressivo(tempo_total)
    elif escolha == 'R':
        tempo_total = int(input("Digite o tempo total desejado (em seg): "))
        temporizador_regressivo(tempo_total)
    else:
        print("Escolha inválida. Por favor, execute o programa novamente e \
            escolha 'P' ou 'R'.")


if __name__ == "__main__":
    main()
