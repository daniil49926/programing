import math
print("Выберите:")
print("1)Найти S через длины сторон.")
print("2)Найти S через координаты вершин.")
a=int(input())
if a==1:
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    if a>=(b+c) or b>=(a+c) or c>=(b+a):
        print("Такого треугольника не существует!")
    else:
        p = (a + b + c) / 2
        S =math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S=",S)
elif a==2:
    print("A[x,y]")
    x1=float(input("x="))
    y1=float(input("y="))
    print("B[x,y]")
    x2=float(input("x="))
    y2=float(input("y="))
    print("C[x,y]")
    x3=float(input("x="))
    y3=float(input("y="))
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    c = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    if a>=(b+c) or b>=(a+c) or c>=(b+a):
        print("Такого треугольника не существует!")
    else:
        p = (a + b + c) / 2
        S =math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S=",S)