from sys import stdin
from copy import deepcopy

def printArr(arr):
    for a in arr:
        print(a)

def check(arr):
    for a in arr:
        if 0 in a:
            return False
    return True

def update(arr1, arr2):
    if arr1 == []:
        return arr2
    elif arr2 == []:
        return arr1
     
    tmp = []
    row,col = len(arr1), len(arr1[0])
    for i in range(row):
        tmp.append([])
        for j in range(col):
            tmp[i].append(min(arr1[i][j], arr2[i][j]))
    return tmp

    

go = [[0,1],[0,-1],[1,0],[-1,0]]
def searchBFS(arr:list, startInd:list, queue:list):
    row,col = len(arr), len(arr[0])
    queue.append(startInd)
    tmpArr = deepcopy(arr)

    while len(queue) != 0:
        ind = queue[0]
        del queue[0]

        for g in go:
            if ind[0]+g[0] <0 or ind[0]+g[0] >=row or ind[1]+g[1] <0 or ind[1]+g[1] >=col:
                continue
            if tmpArr[ind[0]+g[0]][ind[1]+g[1]] == 0:
                tmpArr[ind[0]+g[0]][ind[1]+g[1]] = tmpArr[ind[0]][ind[1]] + 1
                queue.append([ind[0]+g[0],ind[1]+g[1]])
    return tmpArr
    

    

col, row = map(int, stdin.readline().split())
arr=[]
for _ in range(row):
    arr.append(list(map(int, stdin.readline().split())))

ans = []
ansArr=[]
for i in range(row):
    for j in range(col):
        if arr[i][j] == 1:
            ans.append(searchBFS(arr, [i,j],[]))

for i in range(len(ans)):
    ansArr = update(ansArr,ans[i])

tmp = []
if not check(ansArr):
    print(-1)
else:
    print(max(max(ansArr))-1)