nome = 'Luis'
print(nome)
print(type(nome))
#Imprimir em minúscula sem alterar o conteúdo
print(nome.lower()) 

#Imprimir em maiúscula sem alterar o conteúdo
print(nome.upper())

nome2 = "Renato"
print(nome2)
print(type(nome2))

#Lista
contatos = []
#contatos[1] = 'Ricardo'
contatos.append('Ricardo')
contatos.append('Luis')
contatos.append("Renato")

print(contatos)
print(type(contatos))

frutas = ["Pêra", "Uva", "Morango"]
frutas = frutas + ["Abacaxi", "Ovo"]
print(frutas)
print(type(frutas))

frutas[4] = 'Kiwi'
print(frutas)

print(f"Qtde de letras de {nome} é {len(nome)}")
print(f"Tamanho 'frutas' é {len(frutas)}")

print(frutas)

for f in frutas:
    print(f)

#Eliminando elementos
frutas.pop(2) #Por posição
print(frutas) 
frutas.remove("Uva") #Pelo nome do objeto
print(frutas)

#frutas.pop(20)
#frutas.remove("Ovo")

#Ordenar em ordem crescente
frutas.sort()
print(frutas)

#Ordem decrescente
frutas.reverse()
print(frutas)
