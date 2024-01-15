def contar_palavras(texto):
    # Usa a função split() para dividir o texto em palavras
    palavras = texto.split()

    # Retorna o número de palavras
    return len(palavras)


# Solicita ao usuário inserir um texto
texto_usuario = input("Digite um texto: ")

# Chama a função contar_palavras e imprime o resultado
numero_palavras = contar_palavras(texto_usuario)
print(f'O número de palavras no texto é: {numero_palavras}')
