import random


def is_primo(numero):
    """Verifica se um número é primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def gerar_numero_aleatorio():
    """Gera um número aleatório entre 1 e 100."""
    return random.randint(1, 100)


def jogar_jogo():
    """Função principal do jogo."""
    pontos = 0

    while True:
        print("\n=== Menu ===")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            numero_aleatorio = gerar_numero_aleatorio()
            print(f"\nNúmero gerado: {numero_aleatorio}")

            resposta = input("O número é primo? (S/N): ").upper()
            if resposta == 'S' and is_primo(numero_aleatorio):
                pontos += 1
                print("Correto! +1 ponto.")
            elif resposta == 'N' and not is_primo(numero_aleatorio):
                pontos += 1
                print("Correto! +1 ponto.")
            else:
                print("Incorreto. O jogo acabou.")
                break

        elif escolha == '2':
            print(f"Pontuação atual: {pontos}")

        elif escolha == '3':
            pontos = 0
            print("Pontuação zerada.")

        elif escolha == '4':
            print("Saindo do jogo. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    jogar_jogo()
