
def main(z):
    import logarithm.logarithm
    import exp_root.exponentiation
    import exp_root.root
    import factorial.factorial
    if z ==1:
        factorial.factorial.fact()
    if z == 2:
        exp_root.exponentiation.exp2()
    elif z ==3:
        exp_root.exponentiation.exp3()
    elif z ==4:
        exp_root.root.root2()
    elif z ==5:
        exp_root.root.root3()
    elif z ==6:
        logarithm.logarithm.log()
    elif z ==7:
        logarithm.logarithm.ln()
    elif z ==8:
        logarithm.logarithm.lg()

print("Оберіть одну із вказаних дій\n"
      "1 - обчислити факторіал\n"
      "2 - знайти квадрат числа\n"
      "3 - знйти куб числа\n"
      "4 - знайти квалратний корінь числа\n"
      "5 - знайти кубічний корінь числа\n"
      "6 - обчислити логарифм\n"
      "7 - обчислити натуральний логарифм\n"
      "8 - обчислити десятковий логарифм\n")


z = input("Оберіть номер: ")
main(z)