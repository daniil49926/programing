import math
print ("Введите данные для уравнения ax^2+bx+c=0")

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

D = (b * b - (4 * a * c))
if a==0:
    x=(-c/b)
    print("x=",x)
elif D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    print("x1=",x1)
    x2=(-b-math.sqrt(D))/(2*a)
    print("x2=",x2)
elif D==0:
    x=-b/(2*a)
    print("x=",x)
else:
    print ("Корней нет")

