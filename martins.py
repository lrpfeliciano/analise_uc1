soma = 0

while True:
    codigo = int(input("Informe o código: "))
    quantidade = int(input("Quantidade: "))

    match (codigo):
        case 10:
            soma = soma + (40 * quantidade)
        case 11:
            soma = soma + (130 * quantidade)
        case 12:
            soma = soma + (80 * quantidade)
        case 13:
            soma = soma + (15 * quantidade)
        case 14:
            soma = soma + (20 * quantidade)
        case _:
            print("Código inválido")

    r = input("Deseja continuar? (s/n) ")
    if r == 'n' or r == 'N':
        break
print(f"O total é {soma:.2f}")

