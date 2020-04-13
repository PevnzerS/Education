def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return print('Делить на ноль нельзя!')


print(division(6, 0))