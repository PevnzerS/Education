my_list = []
k = 1
while True:
    my_dict = {}
    name = input('Введите название товара: ')
    my_dict['Название'] = name
    price = int(input('Введите цену товара: '))
    my_dict['Цена'] = price
    quantity = int(input('Введите кол-во товара: '))
    my_dict['Количество'] = quantity
    unit = input('Введите ед. измерения товара: ')
    my_dict['Ед. измерения'] = unit
    my_tuple = (k, my_dict)
    my_list.append(my_tuple)
    k += 1
    if input('Вы хотите продолжить? [Д/Н] ').lower() != 'д':
        break

print('Готовая структура: ')
print(my_list)

my_dict1 = {}
my_dict1['Название'] = []
my_dict1['Цена'] = []
my_dict1['Количество'] = []
my_dict1['Ед. измерения'] = []
for i in my_list:
    my_dict1['Название'].append(i[1]['Название'])
    my_dict1['Цена'].append(i[1]['Цена'])
    my_dict1['Количество'].append(i[1]['Количество'])
    my_dict1['Ед. измерения'].append(i[1]['Ед. измерения'])
print('Аналитика по товарам: ')
print(my_dict1)