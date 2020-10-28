N = [0]*37
numblack = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
numred = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
drop = [0]*37
dropmax = 0
sumblack,sumred = 0,0
lastgame = 12
i = 0
while 1:
    n = int( input())
    if n < 0 or n > 36:
        break
    N[n] = N[n]+1
    for i in range(37):
        if N[i] > dropmax: 
            dropmax = N[i]
    for i in range(37):
        if N[i] == dropmax:
            print(i, end = ' ')
    print()
    drop[n] = i
    for i in range(37):
        if drop[i] == 0 or (i - drop[i]) > lastgame:
            print(i, end = ' ')
    print()
    for i in range(18):
        if n == numblack[i]:
           sumblack = sumblack+1
        elif n == numred[i]:
           sumred = sumred+1
    print(sumred,sumblack,'\n''\n')
    i=i+1

