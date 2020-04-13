def profile(name, surname, date, city, email, phone):
    return print(f"Hi! My name is {surname} {name}. I was born on {date}. My hometown is {city}. To contact me, use {email} or my phone {phone}")


name = input('What`s your name? ')
surname = input('What`s your surname? ')
date = input('What`s tour date of birth? ')
city = input('What`s your hometown? ')
email = input('What`s your email? ')
phone = input('What`s your phone number? ')

profile(date=date, surname=surname, name=name, phone=phone, city=city, email=email)
