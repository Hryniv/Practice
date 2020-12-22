def root2():
    while True:
        n = input("Введіть число: ")
        if not n.isnumeric():
            print("Ви ввели не число. Спробуйте знову: ")
        elif float(n) <=0:
            print("Лише додатні значення")
        else:
            n = float(n)
            return print(n ** 0.5)


def root3():
    while True:
        n = input("Введіть число: ")
        if not n.isnumeric():
            print("Ви ввели не число. Спробуйте знову: ")

        else:
            n = float(n)
            return print(n**(1/3))
