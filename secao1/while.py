'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Operadores = += -= *= **= /= //= %=
'''
# contador = 0

# while contador < 100:
#     contador += 1 
    
#     if contador == 6:
#         print(f'Não vou mostrar o {contador}')
#         continue

#     if 20 <= contador <= 44:
#         print(f'Não vou mostrar o {contador}')
#         continue

#     print(f'{contador}')

# print(f'O processo acabou.')


'''
while + while
repetição de laços
'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}{coluna=}')
        coluna += 1
    linha += 1

print('Acabou.')

