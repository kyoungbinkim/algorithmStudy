from sys import stdin
from math import sqrt, floor

def constraintA(num):
    tmp = num // 2
    if num % 2 ==0:
        return tmp*(tmp - 1)
    else:
        return (tmp*tmp)
    

def constraintB(num):
    ans = 0
    divisorList = []
    for i in range(1, floor(sqrt(num))+1):
        if num % i == 0:
            if i != num//i:
                divisorList.append(i)
                divisorList.append(num // i)
            else:
                divisorList.append(i)
    for i in range(len(divisorList)):
        for j in range(i, len(divisorList)):
            if num % (divisorList[i] + divisorList[j]) == 0:
                ans += 1
    return ans

def constraintC(num):
    ans = 0
    primeList = [1 for _ in range(num+1)]
    primeList[0] = 0
    primeList[1] = 0
    primeNumList = []
    for i in range(2, num+1):
        if primeList[i] == 0:
            continue
        primeNumList.append(i)
        for j in range(i+i, num+1, i):
            primeList[j] = 0
    
    for i in range(1, len(primeNumList)-1):
        if primeNumList[i+1] - primeNumList[i] == 2:
            ans += 1

    return ans


num = int(stdin.readline())
print(constraintA(num))
print(constraintB(num))
print(constraintC(num))