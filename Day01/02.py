# Função que verifica a paridade de um número
def verificar_paridade(numero):
    # Utiliza operador ternário para retornar "par" se o número
    # for divisível por 2, senão retorna "ímpar"
    return "par" if numero % 2 == 0 else "ímpar"


try:
    # Solicita ao usuário inserir um número como uma string e
    # Converte a string para um número inteiro
    numero = int(input("Digite um número: "))
except ValueError:
    # Se ocorrer um erro durante a conversão, imprime uma mensagem de erro
    print("Por favor, insira um número inteiro válido.")
else:
    # Se a conversão for bem-sucedida, chama a função para verificar a paridade
    resultado = verificar_paridade(numero)
    # Imprime a mensagem indicando se o número é par ou ímpar
    print(f"{numero} é um número {resultado}.")
