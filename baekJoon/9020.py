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

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    i,j = math.floor(n/2), math.ceil(n/2)
    # print(i,j)
    
    while not (isPrime(i) and isPrime(j)):
        i -= 1
        j +=1
    print(i,j)