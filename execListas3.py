
list1 = [10,31,27,4,21,3]

i = 0
while i < len(list1):
    if i == 0:
        if list1[i]%2 == 0 and list1[i+1]%2 != 0:
            print(list1[i])
    else:
        if list1[i-1]%2 != 0 and list1[i]%2 == 0 and list1[i+1]%2 != 0:
            print(list1[i])

    i += 1