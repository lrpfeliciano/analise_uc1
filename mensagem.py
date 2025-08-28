print('Olá mundo')
print("luis")

nome = input("Informe o nome: ") #string
print(f"Olá, {nome}")

print("Olá, " + nome)
idade = 44 #inteiro
tarifa = 4.7 #float
#print("Olá, " + nome + ", você tem " + idade + 
#      "anos")
print(f'Olá, {nome}, você tem {idade} anos')
print('Olá, {nome}, você tem {idade} anos')
print('Olá, {0}, você tem {1} anos'.format(
    nome, idade))