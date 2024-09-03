import os

lista = []

while True:
    print('Selecione uma opção', '[i]nserir [a]pagar [l]ista [e]ncerrar', sep="\n" )
    opcao = input(' ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor (item): ')
        lista.append(valor)

    elif opcao == 'a':
        
        try:
            os.system('cls')
            for x, y in enumerate(lista):
                print(x, y)
            indice = int(input('Digite o índice do item: '))
            del lista[indice] 
        except ValueError:
            print('Digite um valor válido.')            
        except IndexError:
            print('Digite um dos índices acima.')
            
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('A lista está vazia.')
        
        else:
            for x, y in enumerate(lista):
                print(x, y)
    
    elif opcao == 'e':
        os.system('cls')
        break
    
    else:
        os.system('cls')
        print('Escolha uma das três opções.')
        
  
