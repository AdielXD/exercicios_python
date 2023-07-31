"""
Gerador de cpf
"""
import random

cpf_val = ''
for i in range(9):
    n = str(random.randint(0, 9))
    cpf_val += n
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
print(f'seu cpf é: {cpf_val[:3]}.{cpf_val[3:6]}.{cpf_val[6:9]}-{cpf_val[9:]}')
