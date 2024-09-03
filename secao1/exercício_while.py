'''
Iterando str com while
'''

nome = 'Aqsuel'
tamanho = len(nome)
ind = 0
novo_nome = ''
while ind < tamanho:
    letra = nome[ind]
    novo_nome += f'*{letra}'
    ind += 1

novo_nome += '*'
print(novo_nome)
