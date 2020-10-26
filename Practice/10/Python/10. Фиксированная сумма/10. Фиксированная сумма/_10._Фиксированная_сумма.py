data = input("Введите данные в таком порядке s, l1, r1, l2, r2 через пробел\n")
try:
    s, l1, r1, l2, r2 = [int(i) for i in data.split(" ")]

    if l1 + r2 >= s:
        r2 = max(s-l1, l2)
    else:
        l1 = min(s-r2, r1)

    print((l1, r2) if l1 + r2 == s else -1)
except ValueError:
    print("Ошибка")