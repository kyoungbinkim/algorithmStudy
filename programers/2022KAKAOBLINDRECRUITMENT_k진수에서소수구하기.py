import math

def trans(n, k):
    ret = []
    s = ''
    while n > k:
        ret.append(str(n % k))
        n = n//k
    ret.append(str(n))
    ret.reverse()
    return ret

def isPrime(num):
    if len(num) == 0:
        return 0
    n = int(num)
    if n == 2:
        return 1
    elif n ==1:
        return 0
    elif n % 2 == 0:
        return 0
    for i in range(3,int(math.sqrt(n))+2):
        if n % i == 0:
            return 0
    return 1

def Search(num):
    tmp = ''
    ret = 0
    for n in num:
        if n == '0':
            ret += isPrime(tmp)
            tmp = ''
        else:
            tmp += n
    
    ret += isPrime(tmp)
    return ret
    
def solution(n, k):
    m = trans(n,k)
    ans = Search(m)
    
    return ans