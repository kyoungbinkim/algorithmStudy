import math

def isPrime(n):
    if n == 2 or n==3:
        return True
    elif n % 2 == 0 or n ==1:
        return False
    for i in range(3, int(math.sqrt(n))+2, 2):
        if n%i == 0:
            return False
    return True

ans = 0    
tmpAns = 0
a,b = map(int, input().split())
for n in range(2, int(math.sqrt(b))+2):
    if isPrime(n):
        # print(int(math.log(b,n)), math.ceil(math.log(a,n)))
        tmpAns+= int(math.log(b,n))- math.floor(math.log(a,n))
        if a== 1:
            tmpAns-=1
        # tmp = n*n
        # while tmp <= b:
        #     if tmp < a:
        #         ans -= 1
        #     ans +=1
        #     tmp = tmp * n
print(tmpAns)