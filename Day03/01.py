def formatar_texto(texto):
    # Remove espaços, vírgulas, interrogações, exclamações e pontos
    # e converte o texto para minúsculas
    caracteres_remover = [" ", ",", ".", "!", "?"]
       
    texto_formatado = ""
    for caractere in texto:
        if caractere.lower() not in caracteres_remover:
            texto_formatado += caractere.lower()

    return texto_formatado


def inverter_texto(texto):
    # Inverte o texto
    return texto[::-1]


def eh_palindromo(texto):
    # Verifica se o texto é um palíndromo
    return texto == inverter_texto(texto)


# Solicita ao usuário a entrada
entrada_usuario = input("Digite uma palavra ou frase: ")

# Formata e verifica se é um palíndromo
entrada_formatada = formatar_texto(entrada_usuario)
if eh_palindromo(entrada_formatada):
    print(f"{entrada_usuario} é um palíndromo!")
else:
    print(f"{entrada_usuario} não é um palíndromo.")
