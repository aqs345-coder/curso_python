frase = 'O Python é uma linguagem de programação.'\
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum.'.lower()

vezes_q_apareceu = 0
letra_q_apareceu_mais = ''

i = 0
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue

    vezes_q_apareceu_atual = frase.count(letra_atual)

    if vezes_q_apareceu < vezes_q_apareceu_atual:
        vezes_q_apareceu = vezes_q_apareceu_atual
        letra_q_apareceu_mais = letra_atual

    i += 1

print('A letra que mais apareceu foi '
      f'"{letra_q_apareceu_mais}", que apareceu '
      f'{vezes_q_apareceu} vezes.')