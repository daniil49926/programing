import math
try:
    n = int(input("Введите число: "))
    i = 2
    limit = int(math.sqrt(n))
    flag=1
    if n < 2:
        print("Число должно быть больше 2")
    else:
        while i <= limit:
            if n % i == 0:
                print("Это составное число")
                flag=2
                
            i = i+1
        if flag==1:    
            print("Это простое число")
except ValueError:
    print("Ошибка ввода")
