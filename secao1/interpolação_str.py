'''interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
'''

nome = 'Suel'
preco = 100.54489
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %i é %08X' % (123456789, 123456789))