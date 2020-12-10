n = int(input())
A = [n]
i = 0
j = 0
k = 0
for i in range(n):
    A.append(int(input()))
    if i == 0:
        print(A[1])
    for j in range(n):
        A = sorted(A,reverse = True)
           
   
    if i == 1:
        print(A[1],A[2])
    if i == 2:
        print(A[1],A[2],A[3])
    if i == 3:
        print(A[1],A[2],A[3],A[4])
    if i == 4:
        print(A[1],A[2],A[3],A[4],A[5])
    if i > 4:
        k += 1
        for x in range(n-i):
            print(A[1+k],A[2+k],A[3+k],A[4+k],A[5+k])
            break