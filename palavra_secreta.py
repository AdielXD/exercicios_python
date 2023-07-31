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

palavra = ''
palavra_sec = ' '
while palavra != palavra_sec:
    palavra = input('Escolha uma palavra para ser a palavra secreta: ')
    if palavra == 'sair':
        break
    os.system('cls')
    acerto = ''
    tentativas = 0
    while True:
        letra = input('digite uma letra: ')
        if letra == 'sair':
            break
        tentativas += 1
        if len(letra) > 1:
            os.system('cls')
            print('digite apenas uma letra!')
            continue
        palavra_sec = ''
        if letra in palavra:
            acerto += letra
            for i in palavra:
                if i in acerto:
                    palavra_sec += i
                else:
                    palavra_sec += '*'
            if palavra_sec == palavra:
                os.system('cls')
                print(f'Parabens, você acertou a palavra secreta ({palavra_sec})!\ncom o total de {tentativas} tentativas!')
                break
            else:
                os.system('cls')
                print(palavra_sec)
        else:
            os.system('cls')
            for i in palavra:
                if i in acerto:
                    palavra_sec += i
                else:
                    palavra_sec += '*'
            print(palavra_sec)
