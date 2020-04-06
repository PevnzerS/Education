text = input('Введите несколько слов, разделяя их пробелами: ').split()
n = 1
for i in text:
    if len(i) <= 10:
        print(f"{n}. {i}")
    else:
        print(f"{n}. {i[0:10]}")
    n += 1