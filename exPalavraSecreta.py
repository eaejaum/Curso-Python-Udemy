"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

secreta = 'caminhar'
letras_corretas = '' 
numero_tentativas = 0

while True:
    print('>>> ADVINHE QUAL É A PALAVRA SECRETA! <<<\n')
    letra = input('Digite uma letra: ')
    numero_tentativas += 1
    
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra in secreta:
        letras_corretas += letra

    palavra_formada = ''

    for letra_secreta in secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == secreta:
        os.system('clear')
        print('VOCÊ GANHOU !!')
        print('A palavra era', secreta)
        print('Tentativas:', numero_tentativas)
        letras_corretas = '' 
        numero_tentativas = 0   