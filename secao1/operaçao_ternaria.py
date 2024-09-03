'''
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
'''

condicao = False
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = int(input('Digite o dígito: '))
novo_digito = digito if digito <= 9 else 0
print(f'{novo_digito}, este é seu valor.')

print('Valor' if True else 'Outro valor' if True else 'Fim')