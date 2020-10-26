import math
try:
    h1, m1 = map(int, input("Время прихода первого:""\n").split(':'))
    h2, m2 = map(int, input("Время прихода второго:""\n").split(':'))

    0 <= h1, h2 <= 23
    0 <= m1, m2 <= 59
    time1 = h1 + (m1/60)
    time2 = h2 + (m2/60)
    if (0 <= abs(time2 - time1) <= 0.25):
        print("Встреча состоится.")
    else:
        print("Встреча не состоится.")
except ValueError:
    print("Ошибка ввода.")