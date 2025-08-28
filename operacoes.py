# Um programa que fará a leitura de dois 
# números e o programa informará a soma
# Entrada 
numero1 = int(
    input("Informe o primeiro número: ")
    )
numero2 = int(
    input("Informe o segundo número: ")
    )
#Processamento
soma=numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
#Saída
print(f'{numero1} + {numero2} = {soma}')
print(f'{numero1} - {numero2} = {subtracao}')
print(f'{numero1} * {numero2} = {multiplicacao}')
print(f'{numero1} / {numero2} = {divisao}')
