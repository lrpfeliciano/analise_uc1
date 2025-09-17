nome = "Luis"
print(len(nome))
if len(nome) < 5:
    print("nome curto")

try: 
    n = int(input("Numero: "))
except:
    print("Informação inválida")






i = 0
while True:
    i = i + 1

    if i == 3:
        continue
    elif i == 5:
        exit()

    print(i)
print("fim")