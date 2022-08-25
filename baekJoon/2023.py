import math

def isPrime(n):
    if n== 2 or n==3:
        return True
    elif n%2 ==0 or n==1:
        return False
    for i in range(3, int(math.sqrt(n))+2, 2):
        if n % i ==0:
            return False
    return True

num = int(input())

numList = [[2,3,5,7]]
for i in range(1,num):
    numList.append([])
    for j in numList[i-1]:
        for k in range(1,10,2):
            if isPrime(j*10+k):
                numList[i].append(j*10+k)
for n in numList[num-1]:
    print(n)