from sys import stdin
import math

def isPrime(n):
    if n == 1 :
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

numSize = int(stdin.readline())
numList = list(map(int, stdin.readline().split()))
ans = 0
for num in numList:
    ans += isPrime(num)
print(ans)