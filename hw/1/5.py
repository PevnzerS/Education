revenue = float(input("Введите выручку Вашей фирмы: "))
expenses = float(input("Введите затраты Вашей фирмы: "))
if revenue > expenses:
    print("Ваша фирма прибыльная!")
    profitability = (revenue - expenses) / revenue
    print((f"Рентабельность Вашей фирмы - {profitability}"))
    staff = int(input("Введите количество Ваших сотрудников: "))
    profit_per_employee = (revenue - expenses) / staff
    print(f"Средняя прибыль на сотрудника составляет {profit_per_employee} у.е.")
elif revenue < expenses:
    print("Ваша фирма убыточная!")
else:
    print("Ваша фирма работает в 0!")