import math

def isPrime(n):
    if n == 2 or n==3:
        return True
    elif n%2 == 0 or n==1:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

def getPrimeList(n):
    ans = [2]
    if n==2:
        return ans
    
    for i in range(3,min([n//2+300,n]),2):
        if isPrime(i):
            ans.append(i)
    if isPrime(n):
        ans.append(n)
    return ans

def getAns(n, plist):
    ret = 0
    plen = len(plist)
    for i in range(plen):
        s = 0
        for j in range(i, plen):
            s += plist[j]
            if s==n:
                ret += 1
            if s>= n:
                break
    return ret

num = int(input())
primeList = getPrimeList(num)
print(getAns(num, primeList))
