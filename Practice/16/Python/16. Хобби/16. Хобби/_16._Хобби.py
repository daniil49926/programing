try:
    quantity=int(input("Введите кол-во билетов: "))
    ticket=input("Введите номера билетов(через пробел): ").split()
    i=0
    flag=1
    while i<=quantity:
        if i == quantity:
            break
        elif (ticket[i][0] == 'a') and ticket[i][4:] == "55661":
            print(ticket[i])
            flag=0
            
        i=i+1
    if flag==1:
        print("-1")
except ValueError:
    print("Ошибка ввода!")

