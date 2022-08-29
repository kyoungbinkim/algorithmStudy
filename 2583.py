from sys import stdin
import sys
sys.setrecursionlimit(10000)
def update(arr, rec):
    for i in range(min([rec[0],rec[2]]), max([rec[0], rec[2]])+1 ):
        for j in range(min([rec[1],rec[3]]), max([rec[1], rec[3]])+1):
            arr[i][j] = 1
    # for a in arr:
    #     print(a)

    
def search(arr, ind):
    if arr[ind[0]][ind[1]] == 1:
        return 0
    arr[ind[0]][ind[1]] = 1
    tmp = 1

    for i in range(ind[1]+1, len(arr[0])):
        if arr[ind[0]][i] == 0:
            tmp += search(arr, [ind[0],i])
        else:
            break
    for i in range(ind[0]+1, len(arr)):
        if arr[i][ind[1]] == 0:
            tmp += search(arr, [i, ind[1]])
        else:
            break
    
    if ind[0] > 0:
        if arr[ind[0]-1][ind[1]] == 0:
            tmp += search(arr, [ind[0]-1,ind[1]])
    if ind[1] > 0:
        if arr[ind[0]][ind[1]-1] == 0:
            tmp += search(arr, [ind[0],ind[1]-1])
    # if ind[0] < len(arr)-1:
    #     if arr[ind[0]+1][ind[1]] == 0:
    #         tmp += search(arr, [ind[0]+1,ind[1]])
    # if ind[1] < len(arr[0])-1:
    #     if arr[ind[0]][ind[1]+1] == 0:
    #         tmp += search(arr, [ind[0],ind[1]+1])
    
    return tmp

m,n,k = map(int, stdin.readline().split())
arr= []
tmp = []
for _ in range(n):
    tmp.append(0)
for _ in range(m):
    arr.append(tmp.copy())

for _ in range(k):
    rect = list(map(int, stdin.readline().split()))
    update(arr, [m-rect[1]-1, rect[0], m-rect[3], rect[2]-1])

ans = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            tmp = search(arr, [i,j])
            ans.append(tmp)
ans.sort()
print(len(ans))
for a in ans[:len(ans)-1]:
    print(a,end=" ")
print(ans[len(ans)-1])