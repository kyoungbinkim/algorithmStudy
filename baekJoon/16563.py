from sys import stdin, setrecursionlimit
from itertools import count
setrecursionlimit(10**9)

def myGcd(num1,num2):
    a,b=num1, num2
    if a < b:
        a, b = b, a
    while b != 0:
        
        r = a % b
        a = b
        b = r
    return a

def miller(n,a):
    if n==0:
        return False
    if a%n ==0:
        return False

    k = n-1
    while True:
        tmp = pow(a,k,n)
        if tmp == n-1:
            return True
        if k%2 >0:
            return tmp==1 or tmp== n-1
        k = k//2

def isPrime(n):
    pl = [2,3,7,61]
    if n in pl:
        return True
    if n<=1:
        return False
    

    for p in pl:
        f = miller(n,p)
        if not f:
            return False
    return True 

def factorize2(n):
    factor = 2 
    factors = []
    while (factor**2 <= n):  
        while (n % factor == 0):  
            factors.append(factor)  
            n = n // factor  
        factor += 1
    if n > 1 : 
        factors.append(n)
    return factors

def factorization(n):
    N =n
    tmp = 2
    ans = []

    while tmp <= N:
        if N%tmp == 0:
            ans.append(tmp)
            N = int(N//tmp)
            if isPrime(N):
                ans.append(N)
                break
        else:
            tmp += 1
    return ans

def factorize3(n, inputX=1):
    if isPrime(n):
        return [n]
    num = n
    factor = 2 
    factors = []
    while num >= 2:
        factor = pollardRho(num, x=inputX)
        if isPrime(factor):
            factors.append(factor)
        else:
            # print("!", factor)
            factors = factors + factorize3(factor,inputX=inputX+1)
        num = num//factor
        if isPrime(num):
            factors.append(num)
            break

    factors.sort()
    return factors

def pollardRho(n, x=2):
    num = n
    if num%2==0:
        return 2
    for c in count(1):
        y = x
        for _ in range(2**c):
            x = (x*x+1) % num
            f = myGcd(x-y, num)
            if f>1:
                return f

def printArr(arr):
    for i in range(len(arr)-1):
        print(arr[i], end=" ")
    print(arr[len(arr)-1])

n = int(stdin.readline())
nlist = list(map(int, stdin.readline().split()))
for k in nlist:
    factors = factorization(k)
    printArr(factors)
