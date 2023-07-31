""" calculadora com while """
while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite o operador (+-/*): ')
    
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são inválidos.')
        continue
    
    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('realizando sua conta, confira o resultado abaixo')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    else:
        print('erro raro')
    #####
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    # Lower é um método que retorna a string com as letras minusculas
    # start swith é um metodo que checa se a string começa com uma letra especifica
    if sair is True:
        break
