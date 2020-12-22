def exp2():
    while True:
        a = input("Введіть число: ")
        if not a.isnumeric():
            print("Ви ввели не число. Спробуйте знову: ")
        else:
            a = float(a)
            return print(a**2)

def exp3():
    while True:
        a = input("Введіть число: ")
        if not a.isnumeric():
            print("Ви ввели не число. Спробуйте знову: ")
        else:
            a = float(a)
            return print(a ** 3)

exp3()