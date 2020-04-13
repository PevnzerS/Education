def int_func(a):
    b = ''
    c = a.split()
    for i in c:
        b += i[0].upper() + i[1:len(i)] + ' '
    return b

print(int_func('1sdas asdasd asd'))



