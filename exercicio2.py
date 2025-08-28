import datetime
anonasc = int(
    input("Informe ano de nascimento: "))
#anoatual = int(
#    input("Informe ano atual: "))
anoatual = datetime.datetime.now().year
idadeAnos = anoatual - anonasc
idadeMeses = idadeAnos * 12
idadeDias = idadeAnos * 360
# idadeDias = idadeMeses * 30
print(f'''
Você tem {idadeAnos} anos 
Ou {idadeMeses} meses 
Ou {idadeDias} dias''')
print(f'Você tem {idadeAnos} anos\nOu {idadeMeses} meses\nOu {idadeDias} dias')