file = open(r"text.txt", "x", encoding="utf-8")
while True:
    new_str = input('Введите новую строку: ')
    if new_str != "":
        file.write(new_str + '\n')
    else:
        break
file.close()