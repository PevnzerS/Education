time = int(input('Введите любое количество секунд, а я переведу его в часы, минуты и секунды: '))
secs = int(time % 60)
mins = int(((time - secs) / 60) % 60)
hours = int((time / 60) // 60)
if 0 <= secs <= 9:
    secs = '0' + str(secs)
if 0 <= mins <= 9:
    mins = '0' + str(mins)
if 0 <= hours <= 9:
    hours = '0' + str(hours)
print(f"{hours}:{mins}:{secs}")