def my_func(x, y):
    y = abs(y)
    degree = x
    k = 1
    while k < y:
        x = x * degree
        k += 1
    return (1 / x)


print(my_func(2, -3))