
list = [10, 32, 27, 4, 21, 3]

def somaLista(list):
    l = len(list)
    i = 0
    soma = 0
    while i < l:
        soma += list[i]
        i += 1

    return(soma)


print(somaLista(list))
