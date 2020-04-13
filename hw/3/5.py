def my_func(a):
    global sum
    sum += a
    return sum

k = 1
sum = 0
while k == 1:
    my_str = input('Введите числа через пробел, а я их буду складывать. Для завершения программы введите Q: ').split()
    for i in my_str:
        if i != 'Q':
            i = int(i)
            my_func(i)
        else:
            k += 1

    print(sum)





