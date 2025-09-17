numeros = []
while True:
    n = int(input("Informe número: "))

    numeros.append(n)
    if n == 0:
        break
print(f"Total de elementos é {len(numeros)}")
somaPares = 0
somaImpares = 0
quantImpares = 0
for i in numeros:
    if i % 2 == 1:
        print("Ímpar")
        somaImpares = somaImpares + i
        quantImpares = quantImpares + 1
    elif i % 2 == 0:
        print("Par")
        somaPares = somaPares + i
print(f'A soma dos números pares é {somaPares}')
mediaImpares = somaImpares / quantImpares
print(f'A média dos ímpares é {mediaImpares}')