from sys import stdin
from copy import deepcopy

p = 1_000_000_007

def makeUnitMat(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def matmul(a,b):
    if b == None:
        return a
    ans = [[0 for _ in range(len(a))] for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                ans[i][j] += a[i][k] * b[k][j]
                ans[i][j] %= p
    return ans

def matpow(a,n):
    if n == 1:
        return a
    
    nbin = bin(n)[2:]
    
    square = deepcopy(a)
    ans = makeUnitMat(len(a))
    for i in nbin[::-1]:
        if i == '1':
            ans = matmul(ans, square)
        square = matmul(square, square)
    return ans
        

def sol():
    t,n,d = map(int, stdin.readline().split())
    
    r = d%t
    p = d//t
    
    batch = None
    rem = None
    
    for ti in range(t):
        m = int(stdin.readline())
        roads = [[0 for _ in range(n)] for _ in range(n)]
        
        for _ in range(m):
            s,e,cnt = map(int, stdin.readline().split())
            roads[s-1][e-1] = cnt
        
        batch = matmul(batch, roads) if batch else deepcopy(roads)
        if ti < r:
            rem = matmul(rem, roads) if rem else deepcopy(roads)
    
    ans = matmul(matpow(batch, p), rem)
    # print('\nans:')
    for i in ans:
        print(*i)

sol()
    