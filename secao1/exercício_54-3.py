entrada = input('Digite seu primeiro nome: ')
tamanho_nome = len(entrada)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print(f'{entrada}, seu nome é curto.')
    elif tamanho_nome <= 6:
        print(f'{entrada}, seu nome é normal.')
    else:
        print(f'{entrada}, seu nome é muito grande.')
else:
    print('Por favor, digite um nome válido. ')
    