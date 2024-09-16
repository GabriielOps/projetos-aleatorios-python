nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
qtd_letras = len(nome)

if nome and idade:
    print (f'Seu nome é {nome}')
    print (f'Seu nome invertido é {nome [::-1]}')
    if ' ' in nome:
        print(f'O seu nome tem espaços')
    else :
        print(f'O seu nome não tem espaços')
    print (f'Seu nome tem {qtd_letras} letras')
    print (f'A primeira letra do seu nome é {nome [0]}')
    print (f'A ultima letra do seu nome é {nome [-1]}')
else :
    
    print('Nada foi digitado em um dos campos')