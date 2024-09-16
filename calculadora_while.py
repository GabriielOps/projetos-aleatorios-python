while True:
    print('Bem-vindo a calculadora')
    num_1 = input ('Digite o primeiro numero:')
    num_2 =  input('Digite o segundo numero:')
    operador = input ('Digite o operador (+-/*):')

    numeros_validos = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None

    if numeros_validos is None:
        print('Numero(s) Invalidos.')
        continue


    

    sair = input ('Quer sair? [s]im:').lower().startswith('s')

    if sair is True:
        break