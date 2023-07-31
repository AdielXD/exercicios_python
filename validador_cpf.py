"""
Validador de CPF
"""
import re, os
while True:
    os.system('cls')
    cpf = input('Digite o seu cpf: ')
    cpf = re.sub(r'[^0-9]','',cpf)
    if len(cpf) == 0 or cpf == cpf[0] * len(cpf):
        print('\nDigite um cpf válido!')
        input('\npressione enter para continuar...')
        continue
    cpf_val = cpf[:9]
    d = 10
    alg = 0
    for i in cpf_val:
        i = int(i)
        alg += i * d
        d -= 1
    alg = (alg * 10) % 11
    alg = 0 if alg > 9 else alg
    alg = str(alg)
    cpf_val += alg
    d = 11
    alg = 0
    for i in cpf_val:
        i = int(i)
        alg += i * d
        d -= 1
    alg = (alg * 10) % 11
    alg = 0 if alg > 9 else alg
    alg = str(alg)
    cpf_val += alg
    if cpf_val == cpf:
        print('\nseu cpf é válido!')
        input('\npressione enter para continuar...')
        break
    else:
        print('\nseu cpf não é válido!')
        input('\npressione enter para continuar...')
        break
