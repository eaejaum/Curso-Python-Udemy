'''Calculadora com While'''

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - / *): ')
    numero_validos = None
    num_1_float = 0
    num_2_float = 0


    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos os números digitados não são válidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta, confira o resultado abaixo: ')

    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'{num_1_float} + {num_2_float} = {soma}')
    elif operador == '-':
        subtracao = num_1_float - num_2_float
        print(f'{num_1_float} - {num_2_float} = {subtracao}')
    elif operador == '/':
        divisao = num_1_float / num_2_float
        print(f'{num_1_float} / {num_2_float} =  {divisao}')
    elif operador == '*':
        multiplicacao = num_1_float * num_2_float
        print(f'{num_1_float} * {num_2_float} =  {multiplicacao}')
    else:
        print('Chegou aqui como amigão??')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break