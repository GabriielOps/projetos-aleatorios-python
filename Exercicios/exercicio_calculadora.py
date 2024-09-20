"""CALCULADORA COM WHILE"""

while True:
    numero_1 = input ('Digite o primeiro numero:')
    numero_2 = input ('Digite o segundo numero:')
    operador = input ('Qual será a operação? (+-/*)')

    # Flag dos numeros validos
    numeros_validos = None

    operadores_permitidos = '+-/*'

    ## Declaração dos conversores
    num_1_float = 0
    num_2_float = 0

    
    ## Verificador e conversor de Numeros
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
      # Conversão da Flag = Output True
        numeros_validos = True
    except:
      # Caso os numeros não sejam validos a flag permanece a mesma  
        numeros_validos = None
        
    ## Mensagem de falha da flag verificadora.
    if numeros_validos is None:
        print ('Um ou mais digitos não são validos.')
        continue

    ## Verificador dos operadores

    if operador not in operadores_permitidos:
        print('Operador invalido. \n Operadores permitidos: +-/*')
        continue
    elif len(operador) > 1:
        print('Somente um operador permitido.')
        continue
    else:
        print('Realizando operação')

    ## Logica calculadora
    if operador == '+':
        print('O resultado da sua soma é ', num_1_float + num_2_float)
    elif operador == '-':
        print('O resultado da sua subtração é ', num_1_float - num_2_float)
    elif operador == '*':
        print('O resultado da sua multiplicação é ', num_1_float * num_2_float)
    elif operador == '/':
        print('O resultado da sua divisão é ', num_1_float / num_2_float)
        
    else:
        print('Shit Happens =^V')

    ## Sair

    sair = input('Quer sair? [S]im:').lower().startswith('s')

    if sair is True:
        break

