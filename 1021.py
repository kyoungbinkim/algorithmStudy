from sys import stdin
import sys

sys.setrecursionlimit(10**9)

def Get(wid, ans):
    if len(ans) == 3:
        if max(ans) < sum(ans)-max(ans):
            return sum(ans)
        return -1
    
    tmp = -1
    for i in range(len(wid)):
        a = Get(wid[i+1:], ans+[wid[i]])
        if a > tmp:
            tmp = a
    return tmp

lSize = int(stdin.readline())
wid = []
for _ in range(lSize):
    wid.append(int(stdin.readline()))
wid.sort()

print(Get(wid, []))

