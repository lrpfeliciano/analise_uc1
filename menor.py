# Fazer um programa que fará a leitura
# da idade de uma pessoa e programa informará
# se a pessoa é menor de idade
"""
    < 
    <=
    >
    >=
   * = (Atribuição, uma variável recebendo um 
    valor) *
    == 
    !=
"""
idade = int(input("Informe a idade: "))
if idade < 18:
    print("Menor de idade.")
    print("estou no if")
else:
    print("MAIOR DE IDADE.")
    
print("Fim do programa")
