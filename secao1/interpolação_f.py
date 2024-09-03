'''Formatação básica de f strings
s - string
d - int
f - float
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - direita
Sinal - + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a'''

variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: >10}')
print(f'{variavel: >10}')
print(f'{154.430716501105932:0=+10.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')