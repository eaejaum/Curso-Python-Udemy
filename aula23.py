'''
OPERADORES in E not in

Strings são iteráveis

  0 1 2 3 4 5
  O t á v i o
 -6-5-4-3-2-1 "Negativos"
'''

nome = 'Otávio'
# print(nome[0])
# print(nome[-6])

    #in
# print('á' in nome)
# print('1' in nome)


    #not in
# print('Z' not in nome)
# print('O' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'"{encontrar}" está em "{nome}"')
else: 
    print(f'"{encontrar}" não está em "{nome}"')