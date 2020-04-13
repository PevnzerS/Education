def fibo_gen(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        yield fact


c = 1
for i in fibo_gen(17):
    if c == 16:
        break
    print(f"{c}! = {i}")
    c += 1
