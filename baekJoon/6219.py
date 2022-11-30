import math

def isPrime(n):
    if n==2 or n==3:
        return True
    elif n%2 ==0 or n==1:
        return False
    for i in range(3, int(math.sqrt(n)+1),2):
        if n%i == 0:
            return False
    return True



A,B,D = map(int, input().split())

ans = 0
for i in range(A, B+1):
    if str(D) in str(i):
        if isPrime(i):
            ans += 1
print(ans)
