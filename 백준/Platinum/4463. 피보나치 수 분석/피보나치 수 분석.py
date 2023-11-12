import math
from sys import stdin
from itertools import count


class fiboMat:
    def __init__(self):
        self.square = [[1,1], [1,0]]
        self.ans = [[1,0],[0,1]]
        self.p = None
    
    def __matMul__(self, m1, m2):
        tmp = [[0,0],[0,0]]
        tmp[0][0] = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0])
        tmp[0][1] = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1])
        tmp[1][0] = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) 
        tmp[1][1] = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) 
        return tmp

    def __matSquare__(self):
        self.square = self.__matMul__(self.square, self.square)
    
    def next(self):
        self.ans = self.__matMul__(self.ans, [[1,1], [1,0]])
        return self.ans[0][0]

    def pow(self, n):
        self.square = [[1,1], [1,0]]
        self.ans = [[1,0],[0,1]]
        if n==0:
            return 0
        elif n==1:
            return 1
        nbin = bin(n-1)[2:]

        for s in nbin[::-1]:
            
            if s=='1':
                self.ans = self.__matMul__(self.ans, self.square)
            self.__matSquare__()
        return self.ans[0][0]

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
    if n==0 or n%2==0 or n%3 ==0:
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
    pl = [2,3,5,7,11,13,17,19,23,29,31, 37]

    for p in pl:
        f = miller(n,p)
        if not f:
            return False
    return True 

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

def factorize3(n):
    if isPrime(n):
        return [n]
    num = n
    factor = 2 
    factors = []
    while num >= 2:
        factor = pollardRho(num)
        if isPrime(factor):
            factors.append(factor)
        else:
            factors += factorization(factor)
        num = num//factor
        if isPrime(num):
            factors.append(num)
            break

    factors.sort()
    return factors

def pollardRho(n):
    num,x = n,2
    if num%2==0:
        return 2
    for c in count(1):
        y = x
        for _ in range(2**c):
            x = (x*x+1) % num
            f = myGcd(x-y, num)
            if f>1:
                return f

def PrintArr(a):
    for i in range(len(a)-1):
        print("{}".format(a[i]), end=" ")
    print(a[len(a)-1])

f= fiboMat()
space = False
while True:
    try:
        a,b = [int(x,base=16) for x in stdin.readline().split()]
    except:
        break
    if b <= a:
        break
    if space:
        print()
    space = True
    print("Range {} to {}:".format(a,b))
    flag=False
    ind = 0
    tmp = f.pow(ind)

    while tmp <= b:
        if a<= tmp <=b:
            flag = True
            print("Fib({}) = {},".format(ind, tmp), end=" ")
            try:
                print("lg is {:.6f}".format(math.log2(tmp)))
            except:
                print("lg does not exist")

            fac = factorize3(tmp)
            if len(fac) == 0:
                print("No prime factors")
            else:
                print("Prime factors:",end=" ")
                PrintArr(fac)
        ind += 1
        tmp = f.pow(ind)
    if not flag:
        print("No Fibonacci numbers in the range")
    
