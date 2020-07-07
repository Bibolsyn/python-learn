a = [3, 15, 20]
print(a)
a.append(15)
print(a)
a.append("hi")
print(a)


def is_year_leap(year_leap):
    result = year_leap % 400

    if result != 0:
        print(year_leap, 'Год не високосный!')
    else:
        print(year_leap, 'Високосный год!')
    
is_year_leap(year_leap)