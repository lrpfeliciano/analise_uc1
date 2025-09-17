"""
2) Uma empresa almeja um programa que fará a 
leitura de 5 preços de produtos e a no final 
irá exibir apenas o somatório dos produtos 
que custam acima de 200 reais.
"""
soma = 0
for i in range(5):
    preco = float(input("Informe o preço: "))
    if preco >= 200:
        soma = soma + preco
print(f'''A soma dos produtos acima de 200 
      é {soma}''')