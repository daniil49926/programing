try:
    a=int(input("Введите число: "))
    rez=0
    multiplicand=1
    while multiplicand <= a:
        multiplicand *=2
        rez+=1
    print(rez)
except ValueError:
    print("Ошибка ввода.")


