# Dia 6: Conversor de Unidades

## 🎯Desafio

Crie um programa que converta unidades de medida. Para este desafio o foco são as conversões de Quilômetros para Milhas, Milhas para Quilômetros, Metros para Pés, Pés para Metros, Graus Celsius para Fahrenheit e Graus Fahrenheit para Celsius.

## 📚Quais conhecimentos eu preciso adquirir para resolver este desafio?

- Operações Matemáticas: Reforce o conhecimento em operações matemáticas para realizar a conversão entre as unidades de medida mencionadas.
- Input/Output: Pratique receber dados do usuário e mostrar resultados.

## 🔔Dica importante

- Antes de iniciar a conversão, certifique-se de entender a relação entre as unidades de medida que deseja converter. Utilize as taxas de conversão fornecidas para realizar os cálculos corretamente: Quilômetros para Milhas (1 quilômetro = 0,621371 milhas), Milhas para Quilômetros (1 milha = 1,60934 quilômetros), Metros para Pés (1 metro = 3,28084 pés), Pés para Metros (1 pé = 0,3048 metros), Graus Celsius para Fahrenheit (Fahrenheit = Celsius * 9/5 + 32) e Graus Fahrenheit para Celsius (Celsius = (Fahrenheit - 32) * 5/9)
- Use operações matemáticas adequadas para realizar a conversão de uma unidade para outra, aplicando as taxas de conversão especificadas.
- Ao realizar operações matemáticas, o uso de parênteses ajuda a organizar e priorizar corretamente as operações que devem ser feitas antes. Faça bom uso dos parênteses para evitar erros de cálculo.

## 💡Resolução do Desafio

1. **Definição de Funções:**
   - Funções são definidas para realizar as conversões. Cada função recebe um valor e retorna o resultado da conversão.
   - Exemplos: `quilometros_para_milhas`, `milhas_para_quilometros`, `metros_para_pes`, `pes_para_metros`, `celsius_para_fahrenheit`, `fahrenheit_para_celsius`.
2. **Solicitar a Escolha da Conversão:**
   - O programa exibe opções de conversão para o usuário usando `print`.
   - O usuário escolhe uma opção digitando um número correspondente.
   - A escolha é armazenada na variável `opcao`.

```
pythonCopy code
opcao = int(input("Digite o número da opção desejada: "))
```

3. **Solicitar o Valor a ser Convertido:**

- O programa solicita ao usuário que insira o valor a ser convertido, que é armazenado na variável `valor`.

```
pythonCopy code
valor = float(input("Digite o valor a ser convertido: "))
```

4. **Realizar a Conversão com Base na Escolha do Usuário:**

- O código utiliza uma estrutura condicional (`if`, `elif`, `else`) para determinar qual conversão executar com base na opção escolhida pelo usuário.
- O resultado da conversão é armazenado em `resultado`, e as unidades de origem e destino são armazenadas em `unidade_origem` e `unidade_destino`.

```
pythonCopy codeif opcao == 1:
    resultado = quilometros_para_milhas(valor)
    unidade_origem = "quilômetros"
    unidade_destino = "milhas"
# ... (mesma lógica para as outras opções)
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    exit()
```

5. **Exibição do Resultado:**

- O resultado é exibido usando uma f-string, mostrando o valor original, a unidade de origem e o resultado convertido com a unidade de destino, com duas casas decimais.

``` 
pythonCopy code
print(f"{valor} {unidade_origem} = {resultado:.2f} {unidade_destino}")
```

## 🕵️‍♀️Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```



Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

```
TESTE 01: Converter 10 quilômetros para milhas -> Resultado da conversão: 6.21371
TESTE 02: Converter 20 milhas para quilômetros -> Resultado da conversão: 32.1868
TESTE 03: Converter 5 metros para pés -> Resultado da conversão: 16.4042
TESTE 04: Converter 100 pés para metros -> Resultado da conversão: 30.48
TESTE 05: Converter 0 graus Celsius para Fahrenheit -> Resultado da conversão: 32.0
TESTE 06: Converter 42 graus Celsius para Fahrenheit -> Resultado da conversão: 107.6
TESTE 07: Converter -3 graus Celsius para Fahrenheit -> Resultado da conversão: 26.6
TESTE 08: Converter 0 graus Fahrenheit para Celsius -> Resultado da conversão: -17.7778
TESTE 09: Converter 100 graus Fahrenheit para Celsius -> Resultado da conversão: 37.7778
TESTE 10: Converter -11 graus Fahrenheit para Celsius -> Resultado da conversão: -23.8889
```



Você pode fazer outros testes caso ache necessário.
