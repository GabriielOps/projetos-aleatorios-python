## CONTINUAR DEPOIS ##



import os
lista = []
print("Lista De Compras")
adicionar_item = True
imprimir_list = None

while True:
    if adicionar_item == True:
        item = input("Qual produto quer adicionar?")
        lista.append(item) 
        print('Produto Adicionado com Sucesso!')
        adicionar_item == None
    elif adicionar_item == None:
        add_produto = input('Quer adicionar outro produto? [S]im ').lower().startswith('s')
        if add_produto is True:
            os.system('cls')
            adicionar_item == True
            continue
        else:
            sk
        
    elif adicionar_item == False:
        imprimir_lista = input('Quer ver a lista? [S]im ').lower().startswith('s') 
        if imprimir_lista is False:
            continue
        elif imprimir_lista is True:
            for indice,nome in enumerate(lista):
                  print(indice, nome)
    elif

    

    if add_produto is False:
        
        if imprimir_lista is False:
            break
        else:
            for indice,nome in enumerate(lista):
                  print(indice, nome)
    else:
        remover = input('Deseja remover algum item? [S]im ').lower().startswith('s')
        if remover is True:
            for indice,nome in enumerate(lista):
                  print(indice, nome)
            item_para_remover = input('Qual item deseja remover? Digite apenas o indice')
            try:
                 lista.remove(item_para_remover)
                 print
            except:
                 print('Somente numeros são permitidos, ou a lista não tem este indice!')
                 
                  
    