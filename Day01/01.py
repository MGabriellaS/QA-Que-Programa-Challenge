# Solicita ao usuário inserir um número
try:
    # Solicita ao usuário inserir um número como uma string e
    # Converte a string para um número inteiro
    numero = int(input("Digite um número: "))
except ValueError:
    # Captura uma exceção caso a conversão não seja possível
    # (por exemplo, se o usuário inserir um texto não numérico)
    print("Por favor, insira um número inteiro válido.")
    # Demonstra para o usuário que o valor inserido não está
    # em um formato válido.
else:
    # Se nenhum erro ocorrer durante a entrada do usuário:
    # Verifica se o número é par ou ímpar e exibe a mensagem correspondente
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
