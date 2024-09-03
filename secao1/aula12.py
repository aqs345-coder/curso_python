#função input
num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

print(f'A soma dos números é: {num_1 + num_2}')

#a função input apenas recebe dados do tipo str
#para resolver este problema:

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

numero_1 = int(num1)
numero_2 = int(num2)

print(f'A soma dos números é: {numero_1 + numero_2}\n')


