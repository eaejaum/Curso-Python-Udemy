'''
OPERADORES LÓGICOS
and (e) or (ou) not (não).
and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
São considerados falsy (que vc já viu) 0 0.0 '' False.
Também existe o tipo None que é usado para representar um não valor.
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
'''

# entrada = input('[E]ntrar [S]air: ')

# senha_digitada = input('Senha: ')
# senha_permitida = 'jpdograu'

# if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
#     print('Entrou')
# else: 
#     print('Saiu')

# AVALIAÇÃO DE CURTO CIRCUITO

senha = input('Senha: ') or 'Sem senha'

print(senha)
