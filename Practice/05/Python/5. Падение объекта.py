print ("x(t)=x0+v0t-at^2/2")

a=int(input("x0="))
b=int(input("v0="))
z=int(input("t="))

g=9.8
x=a+b*z-g*z*z/2

print("x(t)=",x)