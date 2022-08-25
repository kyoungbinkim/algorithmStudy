import math

def isNonoSquare(n, m):
    if n%m == 0:
        return False
    if 1<= n <=3:
        return True
    for i in range(3, int(math.sqrt(n))):
        if i%n == 0:
            return isNonoSquare(n//i , i)
    return True
    

def isPrime(n):
    if n==2 or n==3:
        return True
    elif n%2 == 0 or n==1:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return isNonoSquare(n//i, i)
    return True


Small, Big = map(int, input().split())
Len = Big - Small +1
ans = 0

for i in range(Small, Big+1):
    if isPrime(i):
        ans += 1
print(ans)


