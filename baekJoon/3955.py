from sys import stdin
import sys
import math
sys.setrecursionlimit(10**6)


def ext_euclid(a,b):
    if b==0:
        return [a, 1, 0]
    else:
        d,x_,y_ = ext_euclid(b, a%b)
        return [d, y_, x_ - (a//b)*y_]

for _ in range(int(stdin.readline())):
    a,b = map(int, stdin.readline().split())
    if b==1:
        if a<10**9:
            print(a+1)
        else:
            print("IMPOSSIBLE")
        continue
    
    ans = ext_euclid(a,b)
    # print(ans)
    if ans[0] != 1 or ans[2] > 10**9:
        print("IMPOSSIBLE")
    elif ans[2] >0:
        print(ans[2])
    else:
        while ans[2] <=0 :
            ans[2] += a
        if  ans[2] > 10**9:
            print("IMPOSSIBLE")
        else:
            print(ans[2])