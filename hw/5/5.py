file = open(r"5.txt", "w", encoding="utf-8")
content = file.write(input('Введите несколько чисел через пробел: '))
file.close()

file = open(r"5.txt", "r+", encoding="utf-8")
my_content = file.readlines()

sum = 0
for line in my_content:
    nums = line.split()
    for num in nums:
        try:
            num = int(num)
            sum += num
        except ValueError:
            break
    print(sum)
file.close()
