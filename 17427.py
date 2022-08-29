import math
from sys import stdin
def isPrime(n):
    if n == 1:
        False,-1,-1
    elif n==2 or n ==3:
        return True,0,0
    elif n%2 == 0:
        return False, n//2, 2
    for i in range(3, int(math.sqrt(n)+3),2):
        if n % i == 0:
            return False, n//i, i
    return True,0,0

flist= [1]
num=int(stdin.readline())
for i in range(2, num+1):
    flag, m, ind= isPrime(i)
    if flag:
        flist.append(i+1)
    else:
        tmp = flist[m-1]*ind
        
        while m%ind == 0:
            m = m//ind
        tmp += flist[m-1]
        flist.append(tmp)
print(sum(flist))