with open("text1234.txt", "r+") as f_cool:
    f_cool.write("Java")
    f_cool.write("GOGOGO")
    content = f_cool.read()
    print(content)
