entrada = input('Digite um número inteiro: ')

try:
    numero = int(entrada)
    par_impar = numero % 2 == 0
    par_impar_texto = 'ímpar'
    
    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O número {entrada} é {par_impar_texto}.')

except:
    print('Você não digitou um número inteiro')


entrada = input('Digite um número inteiro: ')

# if entrada.isdigit():
#     numero = int(entrada)
#     par_impar = numero % 2 == 0
#     par_impar_texto = 'ímpar'
    
#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'O número {entrada} é {par_impar_texto}.')

# else:
    # print('Você não digitou um número inteiro')


