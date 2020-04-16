file = open(r"2.txt", "r", encoding="utf-8")
content = file.readlines()
c_s = 0 # Счётчик строк
i = 1 # Нумерация строк
print(content)
for line in content:
    a = line.split() # Разделялем строку на список элементов, длина этого списка и будет количеством слов в строке
    print(f"В строке №{i} количество слов = {len(a)}")
    i += 1
    if line:
        c_s += 1
print(f"Колиичество строк: {c_s}")
file.close()
