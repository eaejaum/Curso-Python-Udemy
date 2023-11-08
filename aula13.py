nome = 'João Pedro'
altura = 1.75
peso = 58
imc = peso // (altura * altura)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura.'
linha_2 = f'Pesa {peso} quilos e seu imc é de'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
