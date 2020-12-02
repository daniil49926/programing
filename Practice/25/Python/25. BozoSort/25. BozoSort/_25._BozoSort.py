from random import randint, shuffle


a = input()
s = a.split()
A = [int(x) for x in s]

def isSorted(A):
    for i in range(1, len(A)):
        if(A[i - 1] > A[i]):
            return False
    return True

sortList = A
while not isSorted(sortList):
    rand1 = randint(0, len(sortList) - 1)
    rand2 = randint(0, len(sortList) - 1)
    swap = sortList[rand1]
    sortList[rand1] = sortList[rand2]
    sortList[rand2] = swap
print(sortList)
def isSorted(A):
    for i in range(1, len(A)):
        if(A[i - 1] < A[i]):
            return False
    return True

sortList = A
while not isSorted(sortList):
    rand1 = randint(0, len(sortList) - 1)
    rand2 = randint(0, len(sortList) - 1)
    swap = sortList[rand1]
    sortList[rand1] = sortList[rand2]
    sortList[rand2] = swap
print(sortList)

B=[A[1],A[2],A[3]]
def isSorted(B):
    for i in range(1, len(B)):
        if(B[i - 1] > B[i]):
            return False
    return True

sortList = B
while not isSorted(sortList):
    rand1 = randint(0, len(sortList) - 1)
    rand2 = randint(0, len(sortList) - 1)
    swap = sortList[rand1]
    sortList[rand1] = sortList[rand2]
    sortList[rand2] = swap
print(sortList)

B=[A[1],A[2],A[3]]
def isSorted(B):
    for i in range(1, len(B)):
        if(B[i - 1] < B[i]):
            return False
    return True

sortList = B
while not isSorted(sortList):
    rand1 = randint(0, len(sortList) - 1)
    rand2 = randint(0, len(sortList) - 1)
    swap = sortList[rand1]
    sortList[rand1] = sortList[rand2]
    sortList[rand2] = swap
print(sortList)
