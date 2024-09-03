"""
Introdução ao desempacotamento e tuples
Esta ação possibilita que vc retire valores de dentro
das listas
Para tal utilize uma variável para o "resto"
"""

nomes = ['Maria', 'Carlos', 'João']

nome, *_ = nomes
print(nome)

"""
Tuples:
Lista imutável
Formas de criar uma tupla-->
"""

numeros = 1, 2, 3, 5, 6
print(numeros)
numeros = (1, 2, 3, 5, 6)
print(numeros)
lista_numeros = [1, 2, 3, 5, 6]
tupla_numeros = tuple(lista_numeros)
print(tupla_numeros)
