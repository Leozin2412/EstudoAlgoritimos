def soma(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + soma(lista[1:])

def conta(lista):
    if lista == []:
        return 0
    else:
        return 1+conta(lista[1:])


teste=[1,2,3,4,5]

print('SOMA RECURSIVA: ', soma(teste))
print('CONTAGEM RECURSIVA: ', conta(teste))