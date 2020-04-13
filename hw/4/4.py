my_list = [1, 2, 3, 2, 3, 5, 6, 5, 8, 9, 11, 123, 321, 123, 0]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)