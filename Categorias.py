categoria = int(input("Informe o número: "))

if categoria == 1:
    print("Alimentos")
elif categoria == 2:
    print("Bebidas")
elif categoria == 3 or categoria == 4:
    print("Comésticos")
elif categoria == 5 or categoria == 6:
    print("Produtos de limpeza")
else:
    print("Categoria não encontrada")