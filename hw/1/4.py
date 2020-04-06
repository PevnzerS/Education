n = int(input("Введите целое положительное число, а я найду самую большую цифру в нем: "))
max = 0
while n > 0:
    a = n % 10
    if a == 9:
        max = a
        break
    elif a > max:
        max = a
    n = n // 10
print(max)