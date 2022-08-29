from sys import stdin
import math
import copy
from itertools import combinations

def Sum(plist, nCr):
    tmp = copy.deepcopy(plist)
    sum = [0,0]

    for i in range(len(tmp)):
        if i in nCr:
            sum[0] -= int(plist[i][0])
            sum[1] -= int(plist[i][1])
        else:
            sum[0] += int(plist[i][0])
            sum[1] += int(plist[i][1])
    return math.sqrt(sum[0]**2 + sum[1]**2)

if __name__ ==  "__main__":
    readline = stdin.readline
    for _ in range(int(readline())):
        ans = float("inf")
        plist = []
        pSize = int(readline())
        nCr = list(combinations(range(pSize), pSize//2))
        for _ in range(pSize):
            p = list(map(int, readline().split()))
            plist.append(p)
        
        for minus in nCr:
            ret = Sum(plist, set(minus))
            if ret < ans:
                ans = ret

        print(ans)