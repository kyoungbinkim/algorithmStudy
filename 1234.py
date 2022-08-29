import math
import sys
sys.setrecursionlimit(10**9)

def calc(rbg, n):
    ret = 0
    r,b,g = rbg
    if min(rbg) < 0:
        return 0

    if n==1:
        for i in rbg:
            if i>0:
                ret +=1
        return ret

    if n%2 == 0:
        halfn = n//2
        c = math.comb(n, halfn)
        ret += c * (calc([r-halfn, b-halfn, g], n-1) \
            +  calc([r-halfn, b, g-halfn], n-1)  \
                + calc([r, b-halfn, g-halfn], n-1))
    
    if n%3 == 0:
        treen = n//3
        c = math.comb(n, treen) * math.comb(n-treen, treen)
        ret += c * calc([r-treen, b-treen, g-treen], n-1)
    
    ret += (calc([r-n,b,g], n-1) + calc([r,b-n,g], n-1) + calc([r,b,g-n], n-1))

    return ret


N,R,B,G = map(int, input().split())
print(calc([R,B,G],N))

print(123, end=" ")