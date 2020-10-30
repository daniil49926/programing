money = int(input())
quantity = int(input())
flag = 1
sumV = int()
remainder = int()
chosen_name_of_the_alkashka = str()
for i in range(0, quantity):
    name_of_the_alkashka, price, size = input().split()
    price = int(price)
    size = int(size)
    pricelit = int
    pricelit = (price/size)
    n_alkaski = int(money / pricelit)
    if n_alkaski >= 1 and n_alkaski > sumV:
        chosen_name_of_the_alkashka = name_of_the_alkashka
        remainder = money - (n_alkaski * pricelit)
        sizen = size
        sumV = n_alkaski
        flag = 0
if flag == 0:
    print(chosen_name_of_the_alkashka, sizen)
    print(sumV)
    print(remainder)
else:
    print(-1)
