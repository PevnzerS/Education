import json


my_list = []
i = 0
profit = 0
av_prof = 0
my_dict = {}
my_dict1 = {}
with open("7.txt", encoding="utf-8") as file:
    for lane in file:
        profit = int(lane.split()[2]) - int(lane.split()[3])
        if profit > 0:
            print(f"Прибыль {lane.split()[0]} составила {profit} у.е.")
            i += 1
            av_prof += profit
        elif profit < 0:
            print(f"Убыток {lane.split()[0]} составил {-profit} у.е.")
        else:
            print(f"{lane.split()[0]} имеет нулевую доходность")
            i += 1
        my_dict[lane.split()[0]] = profit
my_list.append(my_dict)
my_dict1['av_profit'] = av_prof / i
my_list.append(my_dict1)
print(my_list)

with open("json_m.json", "w") as f_cool:
    json.dump(my_list, f_cool)