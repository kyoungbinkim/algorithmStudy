import math


def isPrime(n):
    if n==2 or n==3:
        return True
    elif n%2 ==0 or n==1:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

def nextPrime(n):
    n +=1
    while not isPrime(n):
        n+=1
    return n

def factorization(x):
    d = 2
    ans = {}
    while d <= x:
        if x % d == 0:
            if ans.get(d) == None:
                ans.update({d:1})
            else:
                ans[d]+=1
            x = x // d
            if isPrime(x):
                if ans.get(x) == None:
                    ans.update({x:1})
                else:
                    ans[x] +=1
                break
        else:
            d += 1
    return ans

ans = 1
a = factorization(int(input()))
print(a)
for k in a.keys():
    ans = ans * k**(a[k]-1) * (k-1)
print(ans)
