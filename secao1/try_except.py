'''Introdução try/except
try - tentar executar o codigo
except - ocorreu algum erro ao tentar executar'''

numero = input('Digite um número: ')

try:
    numero_float = float(numero)
    print(f'{numero} = {numero_float:.2f}')
    print(f'O dobro de {numero_float:.2f} é {numero_float * 2:.2f}')
except:
    print('Isto não é um número')