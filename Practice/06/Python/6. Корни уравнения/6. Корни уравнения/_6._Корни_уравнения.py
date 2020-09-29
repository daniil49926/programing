import math
print ("Введите данные для уравнения ax^2+bx+c=0")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

D = (b * b - (4 * a * c))
if D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    print("x1=",x1)
    x2=(-b-math.sqrt(D))/(2*a)
    print("x2=",x2)
if D==0:
    x=-b/(2*a)
    print("x=",x)
else:
    print ("Корней нет")

