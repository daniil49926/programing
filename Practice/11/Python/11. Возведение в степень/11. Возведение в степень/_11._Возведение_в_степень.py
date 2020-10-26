import math
try:
    a=float(input("Введите число возводимое в степень: "))
    x=int(input("Введите степень: "))
    z=1
    z=a
    i=1
    while (i<abs(x)):
        z*=a
        i+=1
    if x>0:
        print("Результат = ",z)
    elif x<0:
        print("Результат = ",1/z)
    elif x==0:
        print("Результат = 1")
except ValueError:
    print("Ошибка ввода.")

