contatos = []
nome = 'Luis'
nome = 'Claúdio'
print(nome)
#Adiciona ao final da lista
contatos.append(nome)
contatos.append("Feliciano")

#Adiciona na posição e #desloca os demais
contatos.insert(0, "Paula")
print(contatos)

contatos.insert(99, "André")
print(contatos)

print(contatos[1]) 
contatos[1] = "Fernanda"

for i in contatos:
    print(i)

contatos.append(20)
contatos.append(4.5)
print(contatos)

contatos.append(["Renato", 20])
print(contatos)