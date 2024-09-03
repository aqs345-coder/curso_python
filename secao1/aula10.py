nome = "Iadja"
altura = 1.5
peso = 77
imc = peso/altura**2

'f-strings'
linha1 = f'{nome} tem {altura:.2f} de altura,'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'

print(linha1, linha2, linha3, sep= '\n')

"""utilizando as f-strings pode-se formatar str's
de forma alternativa e mais organizada"""