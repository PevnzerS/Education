from sys import argv


script_name, first_param, second_param, third_param = argv

print('Имя скрипта - ', script_name)
print('Количество отработанных часов  - ', first_param)
print('Ставка (руб/час)  - ', second_param)
print('Премия  - ', third_param)

salary = int(first_param) * int(second_param) + int(third_param)
print(f"Итого зарплата равна {salary} руб.")