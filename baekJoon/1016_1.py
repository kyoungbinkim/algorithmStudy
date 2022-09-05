from sys import stdin
import math

def isPrime(n):
    if n==2 or n==3:
        return True
    elif n%2 == 0 or n==1:
        return False
    
    for i in range(5, int(math.sqrt(n)+1),2):
        if n % i ==0:
            return False
    return True

def nextPrime(n):
    tmp = n+1
    while not isPrime(tmp):
        tmp += 1
    return tmp

def update(ans,start, end, p):
    sq = p **2
    for i in range(start, end+1):
        if i % sq == 0:
            ans[i-start] = 0
    


start, end = map(int, stdin.readline().split())
ans = [1] * (end - start + 1)

Prime = nextPrime(1)
endRoot = int(math.sqrt(end))+1
plist = list(range(1, endRoot+1))

while Prime < endRoot:
    update(ans,start, end, Prime)
    Prime = nextPrime(Prime)
print(sum(ans))




