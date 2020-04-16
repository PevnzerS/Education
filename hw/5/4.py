file = open(r"4.txt", "r+", encoding="utf-8")
new_file = open(r"new4.txt", "w", encoding="utf-8")
content = file.readlines()
my_dict = {'One': 'Один - 1', 'Two': 'Два - 2', 'Three': 'Три - 3', 'Four': 'Четыре - 4'}
for line in content:
    words = line.split()
    new_file.write(my_dict.get(words[0]) + '\n')
file.close()