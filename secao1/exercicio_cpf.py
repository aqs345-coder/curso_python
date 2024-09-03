import re, sys

entrada = input('Digite o seu CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada)
nove_digitos = cpf[:9]
dez_digitos = cpf[:10]
soma1 = 0
soma2 = 0
contador_regressivo = 10
contador_regressivo1 = 11

entrada_sequencial = entrada == entrada[0] * len(entrada)
if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

for i in nove_digitos:
    digitos_mult1 = int(i) * contador_regressivo
    soma1 += digitos_mult1
    contador_regressivo -= 1

digito1 = (soma1 * 10) % 11

digito1 = 0 if digito1 > 9 else digito1

if digito1 == int(cpf[9]):
    for j in dez_digitos:
        digitos_mult2 = int(j) * contador_regressivo1
        soma2 += digitos_mult2
        contador_regressivo1 -= 1
    digito2 = (soma2 * 10) % 11

    digito2 = 0 if digito2 > 9 else digito2

    if digito2 == int(cpf[10]):
        print('Este CPF é válido.')
    else:
        print('Este CPF não é válido.')
else:
    print('Este CPF não é válido.')
    

