try:
    a=int(input("Введите число: "))
    rez=1
    if a>=0:
        for i in range(1,a+1):
            rez*=i
        print(rez)
    elif a<0:
        print("Введите целое положительное число")
except ValueError:
    print("Введите целое положительное число")

