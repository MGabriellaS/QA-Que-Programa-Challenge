def calcular(operacao, num1, num2):
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return None
    else:
        print("Erro: Operação inválida.")
        return None

    return resultado


def main():
    # Solicita ao usuário a operação desejada
    operacao = input("Digite a operação (+, -, *, /): ").lower()

    try:
        # Solicita ao usuário os números para a operação
        # e converte as strings para floats
        num1 = float(input("Digite o primeiro número: ").replace(",", "."))
        num2 = float(input("Digite o segundo número: ").replace(",", "."))
    except ValueError:
        print("Erro: Insira números válidos.")
        return None

    # Chama a função para realizar a operação
    resultado = calcular(operacao, num1, num2)

    # Imprime o resultado, se houver
    if resultado is not None:
        print(f"O resultado da operação é: {resultado}")


# Chama a função principal
if __name__ == "__main__":
    main()
