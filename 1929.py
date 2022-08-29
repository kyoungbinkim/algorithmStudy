import math

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n == 1:
        return False
    
    for i in range(3, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

m,n = map(int, input().split())
for i in range(m,n+1):
    if isPrime(i):
        print(i)