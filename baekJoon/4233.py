from sys import stdin

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
    pl = [2,3,5,7,11,13,17,19,23,29,31,37]
    if n in pl:
        return True
    if n<=1:
        return False
    

    for p in pl:
        f = miller(n,p)
        if not f:
            return False
    return True     

while True:
    p,a = map(int, stdin.readline().split())
    if a==p==0:
        break
    
    if isPrime(p):
        print("no")
    elif pow(a,p,p) == a:
        print("yes")
    else:
        print("no")
