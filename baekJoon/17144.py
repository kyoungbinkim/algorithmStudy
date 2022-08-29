from copy import deepcopy
from sys import stdin

def Diffusion(arr, n, m):
    tmp = []
    for _ in range(n):
        tmp.append([0]*m)
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                tmp[i][j] = arr[i][j]
                continue
            val = arr[i][j]
            val5 = val//5
            if i>0:
                if arr[i-1][j] != -1:
                    val -= val5
                    tmp[i-1][j] += val5
            if j>0:
                if arr[i][j-1] != -1:
                    val -= val5
                    tmp[i][j-1] += val5
            
            if i<n-1:
                if arr[i+1][j] != -1:
                    val -= val5
                    tmp[i+1][j] += val5
            if j<m-1:
                if arr[i][j+1] != -1:
                    val -= val5
                    tmp[i][j+1] += val5
            tmp[i][j] += val
    return tmp

def Clock(arr, n,m, ind):
    tmp = deepcopy(arr)
    r,c = ind

    for i in range(m-1):
        if arr[r][i] == -1:
            tmp[r][i+1] = 0
        else:
            tmp[r][i+1] = arr[r][i]
    
    for i in range(m-1,0,-1):
        tmp[0][i-1] = arr[0][i]
    
    for j in range(r-1):
        tmp[j+1][0] = arr[j][0]
    
    for j in range(r,0,-1):
        tmp[j-1][m-1] = arr[j][m-1]

    return tmp 

def unClock(arr, n,m,ind):
    tmp = deepcopy(arr)
    r,c = ind

    for i in range(m-1):
        if arr[r][i] == -1:
            tmp[r][i+1] = 0
        else:
            tmp[r][i+1] = arr[r][i]
    
    for i in range(m-1,0,-1):
        tmp[n-1][i-1] = arr[n-1][i]
    
    for j in range(r, n-1):
        tmp[j+1][m-1] = arr[j][m-1]
    
    for j in range(n-1, r+1,-1):
        tmp[j-1][0] = arr[j][0]

    return tmp

def arrSum(arr):
    ans = 0
    for a in arr:
        ans += sum(a)
    return ans + 2


row, col, t = map(int ,stdin.readline().split())
arr = []
for _ in range(row):
    arr.append(list(map(int,stdin.readline().split())))
c,uc = 0, 0
for i in range(row):
    for j in range(col):
        if arr[i][j] == -1:
            if type(c) == type(0):
                c=[i,j]
            else:
                uc=[i,j]
                break

for _ in range(t):
    arr = Diffusion(arr, row,col)
    arr= Clock(arr,row, col, c)
    arr = unClock(arr, row, col, uc)

print(arrSum(arr))

