file = open(r"3.txt", "r", encoding="utf-8")
content = file.readlines()
sum = 0
i = 0
for line in content:
    words = line.split()
    for word in words:
        try:
            word = int(word)
            sum += word
            i += 1
            if word < 20000:
                print(f"Сотрудник {words[0]} зарабатывает меньше 20000 рублей - {word}")
        except ValueError:
            continue
print(f"Средняя зарплата = {round((sum / i), 2)} рублей")
file.close()