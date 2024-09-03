nome = input('Digite seu nome: ')
peso = int(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso/(altura * altura)

linha1 = f'{nome} tem {altura:.2f} de altura,'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'

print(linha1, linha2, linha3, sep= '\n')

if imc < 16:
    print('Você está com magreza grau III')
elif imc < 16.9:
    print('Você está com magreza grau II')
elif imc < 18.4:
    print('Você está com magreza grau I')
elif imc < 24.9:
    print('Você está em eutrofia (peso ideal)')
elif imc < 29.9:
    print('Você está com pré-obesidade')
elif imc < 34.9:
    print('Você está com obesidade moderada (grau I)')
elif imc < 39.9:
    print('Você está com obesidade severa (grau II)')
else:
    print('Você está com obesidade muito severa (grau III)')