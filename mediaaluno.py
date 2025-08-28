n1 = float(input("Informe nota 1: "))
n2 = float(input("Informe nota 2: "))
n3 = float(input("Informe nota 3: "))
n4 = float(input("Informe nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print(f"A média é {media:.2f}. Você está aprovado.")
else:
    rec = float(input("Nota de recuperação: "))
    novamedia = (media + rec) / 2
    print(f"A média final é {novamedia:.2f}")
    if novamedia >= 5:
#        print(f"A média final é {novamedia:.2f}")
        print("Você está aprovado")
    else:
#        print(f"A média final é {novamedia:.2f}")
        print("Você está reprovado")