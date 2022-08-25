from sys import stdin
from itertools import combinations

def Diff(Base, subset):
    base= Base.copy()
    for s in subset:
        for i in range(len(base)):
            if s == base[i]:
                del base[i]
                break
    return base

def Calc(A,B):
    ans = 1
    A.sort(), B.sort()
    flag = True
    while flag:
        flag = False
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    del A[i]
                    del B[i]
                    ans += 1
                    flag = True
                    break
            if flag:
                break
    if len(A) == 0:
        ans -= 1
    return ans
        
datalen = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
if max(data) >50:
    print(0)
else:
    ans = float("inf")
    for num in range(1, datalen//2+1):
        comb = combinations(data, num)
        for subSet in comb:
            if sum(subSet) != 50:
                continue
            subSet2 = Diff(data, list(subSet))
            tmp = Calc(list(subSet), subSet2)
            if tmp < ans:
                ans = tmp
    print(ans)