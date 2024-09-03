"""
Exercício
Exiba os índices antes de cada nome
Ex: 
    0 Maria
    1 João
    2 Carlos
"""


lista = ['Maria', 'João', 'Carlos']
lista.append('Suel')
lista.append('Iadja')
lista.append('Alan')
lista.pop()
del lista[0]

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))