def log():
    import math
    while True:
        a = input("Введіть оcнову а(а > 0 і а не дорівнює 0): ")
        b = input("Введіть число: ")
        if not a.isnumeric() or not b.isnumeric():
            print("Ви ввели не число. Спробуйте знову: ")
        elif float(a) <=0 or float(a)==1:
            print("Лише додатні значення, які не дорівнюють 1.")
        elif float(b)<= 0:
            print("Лише додатні значення")

        else:
            a = float(a)
            b = float(b)
            return print(math.log(b,a))

def lg():
    import math

    while True:
        a = input("Введіть число: ")
        if not a.isnumeric():
            print("Ви ввели не число. Спробуйте знову: ")
        elif float(a) <=0:
            print("Лише додатні значення")
        else:
            a = float(a)
            return print(math.log10(a))
def ln():
    import math
    while True:
        a = input("Введіть число: ")
        if not a.isnumeric():
            print("Ви ввели не число. Спробуйте знову: ")
        elif float(a) <= 0:
            print("Лише додатні значення")
        else:
            a = float(a)
            return print(math.log(a))
ln()