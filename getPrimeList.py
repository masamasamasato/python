import math
 
N = int(input())
stopPoint = int(math.sqrt(N))
numList = [i for i in range(2, N+1)]
primeList = []
 
j = 2
#　√Nまで計算していく
while j <= stopPoint:
    i = 0
    startPrime = numList[0]
    print(startPrime,end=" ")
    primeList.append(startPrime)
    lenList = len(numList)
    # 素数startPrimeの倍数を全削除
    while i <= lenList - 1:
        if numList[i] % startPrime == 0:
            numList.pop(i)
            lenList -= 1
        i +=1
    j += 1
 
for i in range(len(numList)):
    if i == len(numList) - 1:
        print(numList[i])
    else:
        print(numList[i],end=" ")