chars = [0] * 26
tochtoznaet = ("hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen")
stopslovo = str(input("Стоп слово: "))
a = ord('a')
for word in tochtoznaet:
    for char in word:
        chars[ord(char) - a] += 1
probability = 1
rez = sum(chars)

for char in stopslovo:
    probability *= chars[ord(char) - a] / rez
    if (probability == 0): 
        break
print(probability)
