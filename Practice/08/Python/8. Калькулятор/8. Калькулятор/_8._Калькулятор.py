x,oper,y=input ( "Доступные символы: " "\n" "1 2 3 4 5 6 7 8 9 0""\n" "+ - * /""\n""Введите через пробел""\n").split()

try:
    x=float(x)
    oper=='+'
    oper=='-'
    oper=='/'
    oper=='*'
    y=float(y)
    if oper =='+':
        print(x+y)
    elif oper == '-':
        print(x-y)
    elif oper == '*':
        print(x*y)
    elif oper == '/':
        if y != 0:
            print(x/y)
        else:
            print("Деление на ноль!")
except ValueError:
    print("Это не правильный ввод!")
