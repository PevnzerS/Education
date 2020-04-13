from itertools import cycle

my_list = [1, 2, 3, 4]
new_list = []
for x in cycle(my_list):
    new_list.append(x)
print(new_list)