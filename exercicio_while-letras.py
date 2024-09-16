frase = input('digite uma frase:')
i = 0
maior_valor_letra_guardada = 0
letra_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]

    # se a letra for espaço
    if letra_atual == ' ':
        i += 1
        continue

    
    contador_letra_atual = frase.count(letra_atual)

    if contador_letra_atual > maior_valor_letra_guardada:
        maior_valor_letra_guardada = contador_letra_atual
        letra_mais_vezes = letra_atual
    else:
        ...
    
    i += 1
    
print (f' A letra que apareceu mais vezes foi "{letra_mais_vezes}" com {maior_valor_letra_guardada} aparições')