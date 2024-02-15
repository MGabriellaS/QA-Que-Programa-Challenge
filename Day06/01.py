def quilometros_para_milhas(quilometros):
    return quilometros * 0.621371


def milhas_para_quilometros(milhas):
    return milhas * 1.60934


def metros_para_pes(metros):
    return metros * 3.28084


def pes_para_metros(pes):
    return pes * 0.3048


def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Solicitar ao usuário a escolha da conversão
print("Escolha a conversão:")
print("1. Quilômetros para Milhas")
print("2. Milhas para Quilômetros")
print("3. Metros para Pés")
print("4. Pés para Metros")
print("5. Celsius para Fahrenheit")
print("6. Fahrenheit para Celsius")

opcao = int(input("Digite o número da opção desejada: "))

# Solicitar ao usuário o valor a ser convertido
valor = float(input("Digite o valor a ser convertido: "))

# Realizar a conversão com base na opção escolhida
if opcao == 1:
    resultado = quilometros_para_milhas(valor)
    unidade_origem = "quilômetros"
    unidade_destino = "milhas"
elif opcao == 2:
    resultado = milhas_para_quilometros(valor)
    unidade_origem = "milhas"
    unidade_destino = "quilômetros"
elif opcao == 3:
    resultado = metros_para_pes(valor)
    unidade_origem = "metros"
    unidade_destino = "pés"
elif opcao == 4:
    resultado = pes_para_metros(valor)
    unidade_origem = "pés"
    unidade_destino = "metros"
elif opcao == 5:
    resultado = celsius_para_fahrenheit(valor)
    unidade_origem = "graus Celsius"
    unidade_destino = "graus Fahrenheit"
elif opcao == 6:
    resultado = fahrenheit_para_celsius(valor)
    unidade_origem = "graus Fahrenheit"
    unidade_destino = "graus Celsius"
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    exit()

# Exibir o resultado
print(f"{valor} {unidade_origem} = {resultado:.2f} {unidade_destino}")
