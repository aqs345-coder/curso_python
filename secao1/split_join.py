"""
split e join com list e str
spli - divide uma string (list)
join - une uma string
"""

frase = 'Olha só como este jovem,\
 perde a vida idiotamente'

lista_frases = frase.split(' ')

lista_frases_fixed = []
for i, frases in enumerate(lista_frases):
    lista_frases_fixed.append(lista_frases[i].strip())

frases_unidas = '-'.join(lista_frases_fixed)
print(frases_unidas)
# print(lista_frases_fixed)