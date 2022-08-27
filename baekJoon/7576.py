from copy import deepcopy
from sys import stdin

def check(arr,row,col):
    for i in range(row):
        if 0 in arr[i]:
            return False
        
    return True

def update(arr, row, col):
    go = [[0,1],[0,-1],[1,0],[-1,0]]
    tmp = deepcopy(arr)
    flag = False
    for i in range(row):
        for j in range(col):
            if arr[i][j] != 1:
                continue
            for g in go:
                if i+g[0] <0 or i+g[0] >=row or j+g[1] <0 or j+g[1] >=col:
                    continue
                if arr[i+g[0]][j+g[1]] == 0:
                    tmp[i+g[0]][j+g[1]] = 1
                    flag = True
    return tmp,flag
                    

col, row = map(int, stdin.readline().split())
arr=[]
for _ in range(row):
    arr.append(list(map(int, stdin.readline().split())))

ans = 0
arr , f = update(arr, row,col)

while f:
    arr, f= update(arr, row,col)
    ans +=1

if check(arr,row,col):
    print(ans)
else:
    print(-1)
