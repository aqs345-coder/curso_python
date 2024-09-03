texto = "Python"

novo_texto = ''
for letra in texto:
    print(letra)



'''
Como o for funciona:
'''
iterador = iter(texto)
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break