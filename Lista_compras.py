
"""
exercicio - criar lista de compras

o usuário pode adicionar, apagar e listar valores na sua lista
não permita que o programa quebre com erros de indices inexistentes na lista
"""

import os

compras = []
while True:
    os.system('cls')
    sel = input('1. adicionar item\n'\
                '2. apagar item\n'\
                '3. ver todos os itens\n'\
                'sair\n'\
                'Selecione uma opção: ')
    if sel == '1':
        os.system('cls')
        n = input('Digite o nome do item que você deseja adicionar:\n')
        compras.append(n)
        input(f'o item "{n}" foi adicionado no fim da lista!\n')
        while True:
            n = input('Deseja adicionar outro item? sim ou não\n')
            if n == 'sim':
                n = input('Digite o nome do item que você deseja adicionar:\n')
                compras.append(n)
                input(f'o item "{n}" foi adicionado no fim da lista!\n')
            else:
                break
    elif sel == '2':
        if compras == []:
            input('você não adicionou nenhum item na lista!')
        else:
            while True:
                try:
                    os.system('cls')
                    n = input('digite o número do item que você deseja remover: ')
                    n = int(n)
                    del compras[n]
                    print(f'o item {n} foi removido da sua lista!')
                    input()
                    break
                except:
                    print('Digite um numero válido!')
                    input()
    elif sel == '3':
        if compras == []:
            input('você não adicionou nenhum item na lista!')
        else:
            os.system('cls')
            for i, n in enumerate(compras):
                print(i, n)
            input()
    elif sel == 'sair':
        os.system('cls')
        break
    else:
        os.system('cls')
        print('Selecione uma opção válida!')
        input()
