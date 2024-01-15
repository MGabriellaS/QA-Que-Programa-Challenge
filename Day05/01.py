import random


def gerar_numeros_mega_sena():
    numeros_mega_sena = []

    while len(numeros_mega_sena) < 6:
        numero_aleatorio = random.randint(1, 60)

        # Verifica se o número gerado já está na lista
        if numero_aleatorio not in numeros_mega_sena:
            numeros_mega_sena.append(numero_aleatorio)

    return numeros_mega_sena


# Chama a função para gerar os números da Mega Sena
numeros_gerados = gerar_numeros_mega_sena()

# Imprime a lista de números gerados
print("Números da Mega Sena:")
print(numeros_gerados)
