import math
from sys import stdin

def isPrime(n):
    if n== 2 or n==3:
        return True
    elif n%2 ==0 or n==1:
        return False
    
    for i in range(3, int(math.sqrt(n))+1,2):
        if n%i ==0:
            return False
    return True

def goldbach(n):
    i,j = math.floor(n/2), math.ceil(n/2)
    while not (isPrime(i) and isPrime(j)):
        i -= 1
        j +=1
    return [i,j]

n = int(stdin.readline())

if n<8:
    print(-1)
else:
    ans = []
    if n%2== 0:
        a,b = n//2, n//2
        if a%2 == 1:
            a -= 1
            b +=1
        ans += goldbach(a)
        ans += goldbach(b)
        ans.sort()
    else:
        ans = [2,3]
        ans += goldbach(n-5)
        ans.sort()    
    for i in range(len(ans)-1):
        print(ans[i], end=" ")
    print(ans[3])
    