"""Listas em Python
Tipo list - mutável
Suporta vários valores de qualaquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete - CRUD
"""


lista = [10, 20, 40, 50, 60]
lista.append(70)
del lista[1]
lista.append(80)
lista.append(90)
lista.append('Iadja')
lista.insert(0, 'Suel')
ultimo_valor = lista.pop(1)
print(lista, 'Removido:', ultimo_valor)