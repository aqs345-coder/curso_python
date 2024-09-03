#operadores de comparação

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 1 <= 1
igual = 'a' == 'a'
diferente = 'a' != 'b'

#operadores lógicos
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso, a expressão
# inteira será avaliada naquele valor
# são considerados falsy: 0, 0.0, '', False
# e existe o tipo None que é usado para representar um não valor

# entrada = input('[E]ntrar [S]sair: ')
# senha = input('Senha: ')

# senha_real = '123456'

# if entrada == 'E' and senha == senha_real:
#     print('Entrar')
# else:
#     print('Sair')


# or - qualquer condição verdadeira avalia toda a expressão
# como verdadeira
# se qualquer valor for considerado verdadeiro, a expressão 
# inteira será avaliada naquele valor

# senha = input('Senha: ') or 'Sem senha'
# print(senha)


# not - usado para inverter expressões
# not True = False
# not False = True

# senha = input('Senha: ')

# if not senha:
#     print('Você não digitou nada')
# elif senha != '123456':
#     print('Senha incorreta')
# elif senha == '123456':
#     print('Senha correta')


# operadores in e not in
# strings são iteráveis
#  0 1 2 3 4 5
#  A q s u e l
# -6-5-4-3-2-1

nome = input('Digite seu nome: ')
print('suel' in nome)
print('vio' in nome)
print('-' * 10)
print('suel' not in nome)
print('vio' not in nome)

encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
