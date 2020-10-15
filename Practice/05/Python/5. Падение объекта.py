import math
print ("x(t)=x0+v0t-at^2/2")

a=float(input("x0="))
b=float(input("v0="))
z=float(input("t="))
S=float
g=9.8
x=a+b*z-g*z*z/2
S=x-a
S=math.fabs(S)
print("Расстояние = ",S)