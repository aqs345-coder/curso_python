while True:
    entrada1 = input('Digite um número: ')
    entrada2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')
    operadores_permitidos = '+-/*'
    numeros_validos = None
    num_1 = 0
    num_2 = 0
    try:
        num_1 = float(entrada1)
        num_2 = float(entrada2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
          print('Um ou ambos os números são inválidos.')
          continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if operador == '+':
        print(f'{num_1} + {num_2} é: {num_1+num_2}')
    elif operador == '-':    
        print(f'{num_1} - {num_2} é: {num_1-num_2}')
    elif operador == '/':
        print(f'{num_1} / {num_2} é: {num_1/num_2}')
    elif operador == '*':
        print(f'{num_1} x {num_2} é: {num_1*num_2}')
    else:
        print('Erro desconhecido.')
    
    sair = input('Deseja sair? [s]air: ').lower().startswith('s')
    if sair:
        break
