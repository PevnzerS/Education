file = open(r"6.txt", "r", encoding="utf-8")
content = file.readlines()
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
my_dict = {}
for line in content:
    sum = 0
    words = line.split()
    for word in words:
        my_num = ''
        for num in word:
            if num in numbers:
                my_num += num
        try:
            my_num = int(my_num)
            sum += my_num
        except ValueError:
            continue
    my_dict[words[0][:-1]] = sum
print(my_dict)
file.close()