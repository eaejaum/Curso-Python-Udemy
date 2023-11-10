"""
Exercício
x Peça ao usuário para digitar seu nome
x Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        x Seu nome é {nome}
        x Seu nome invertido é {nome invertido}
        x Seu nome contém (ou não) espaços
        x Seu nome tem {n} letras
        x A primeira letra do seu nome é {letra}
        x A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
         exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
tamanhonome = len(nome)

if nome and idade:
    print(f'Seu nome é "{nome}".')
    print(f'Seu nome invertido é "{nome[::-1]}".')
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:    
        print('Seu nome não contem espaços.')
    print(f'Seu nome contém {tamanhonome} letras.')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[-1]}"')
else:
    print('Desculpe, você deixou campos vazios.')