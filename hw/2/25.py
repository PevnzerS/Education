my_list = [8, 5, 3, 3, 3, 2, 2]
new_rating = int(input('Введите новый элемент рейтинга: '))
my_list.append(new_rating)
my_list.sort()
my_list.reverse()
print(my_list)
