entrada = input('Digite a hora: ')

try:
    hora = int(entrada)
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('Boa noite!')
    else:
        print('Digite uma hora entre 0 e 23')

except:
    print('Digite apenas um número inteiro')