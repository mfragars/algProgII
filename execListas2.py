
list1 = [10,32,27,4,21,3]
list2 = [7,12,9,13,67, 4]

def produto(l1, l2):
    len1 = len(l1)
    len2 = len(l2)

    if len1 != len2:
        return("Lista com tamanhos diferentes")
    else:
        i = 0 
        prod = 0   
        while i < len1:
            a = l1[i]
            b = l2[i]

            prod += (a * b)

            i += 1

        return(prod)


print(produto(list1, list2))