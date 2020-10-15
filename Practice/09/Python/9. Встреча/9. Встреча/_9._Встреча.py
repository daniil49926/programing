import math
try:
    h1,m1=input("Введите время прихода первого человека:""\n").split(":")
    h2,m2=input("Введите время прихода второго человека:""\n").split(":")
    h1=int()
    h2=int()
    m1=int()
    m2=int()
    if (h1*60+m1)==(h2*60+m2):
        print("Встреча состоится")
    else:
        print("Встреча не состоится")
except ValueError:
    print("Ошибка ввода")