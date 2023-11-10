'''
Operador Lógico "not"

É usado para inverter expressões

not True = False
not False = True
'''

senha = input('Senha: ')

if not senha:
    print('Sem senha!')

print(not True) #False
print(not False) #True