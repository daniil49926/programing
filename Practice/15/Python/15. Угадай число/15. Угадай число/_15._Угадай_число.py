from random import randint

try:
    a = randint(0, 100)
    print("Приветствую в игре\n\"Угадай число\"")
    pick=int(input("Начнем?\n\"ДА-1\"\n\"НЕТ-0\"\n"))
    i = 0
    while pick == 1:
        choice = int(input("Введи число: "))
        if choice < a:
            print("Загаданное число больше")
        elif choice > a:
            print("Загаданное число меньше")
        else:
            print("Поздравляю! Вы угадали")
            pick = int(input("Хотите попробовать еще раз?\nЕсли Да, введите - 1\nЕсли нет, введите - 0\n"))
            a = randint(0, 100)
            i = 0
        i += 1
        if i == 5:
            print("Вы проиграли,загаданное число:",a)
            pick = int(input("Хотите попробовать еще раз?\nЕсли Да, введите - 1\nЕсли нет, введите - 0\n"))
            a = randint(0, 100)
            i = 0
except ValueError:
    print ("Неверный ввод!")