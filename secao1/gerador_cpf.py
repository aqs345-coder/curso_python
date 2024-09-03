import random, sys

for _ in range(100):
    nove_digitos = ''
    soma = 0
    soma2 = 0
    contador_regressivo = 10
    contador_regressivo1 = 11

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    for digito in nove_digitos:
        digitos_mult1 = int(digito) * contador_regressivo
        soma += digitos_mult1
        contador_regressivo -= 1

    digito1 = (soma * 10) % 11
    digito1 = 0 if digito1 > 9 else digito1

    dez_digitos = nove_digitos + str(digito1)

    for j in (dez_digitos):
        digitos_mult2 = int(j) * contador_regressivo1
        soma2 += digitos_mult2
        contador_regressivo1 -= 1

    digito2 = (soma2 * 10) % 11
    digito2 = 0 if digito2 > 9 else digito2

    print(f'{nove_digitos}{digito1}{digito2}')
    

