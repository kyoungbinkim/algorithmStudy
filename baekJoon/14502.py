from itertools import combinations
from copy import deepcopy
from sys import stdin
import sys

sys.setrecursionlimit(10**9)

go = [[-1,0],[1,0],[0,1],[0,-1]]
def dps(arr,p, row,col):
    x,y = p
    arr[x][y] = -1

    for (r,c) in go:
        if x+r<0 or x+r == row or y+c <0 or y+c==col:
            continue
        if arr[x+r][y+c] == 0:
            dps(arr, [x+r, y+c], row,col)

def getZero(arr, row,col):
    ans = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                ans +=1
    return ans

row,col = map(int, stdin.readline().split())
arr = []
zeroPoint = []
for _ in range(row):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(row):
    for j in range(col):
        if arr[i][j] == 0:
            zeroPoint.append([i,j])

zeroSelect = combinations(zeroPoint,3)

ans = -1
for z in zeroSelect:
    tmp = deepcopy(arr)
    for p in z:
        tmp[p[0]][p[1]] = 1
    for i in range(row):
        for j in range(col):
            if tmp[i][j]==2:
                dps(tmp, [i,j], row, col)
    
    k = getZero(tmp, row, col)
    if k > ans:
        ans = k
print(ans)


            