from sys import stdin
import sys

sys.setrecursionlimit(10**9)
dfs = []
def DFS(arr, ind, visit):
    dfs.append(ind+1)
    visit.add(ind)
    tmp = arr[ind]
    for i in range(len(tmp)):
        if not i in visit and tmp[i]== 1:
            DFS(arr, i, visit)

bfs = []
def BFS(arr,ind,queue, visit):
    visit.add(ind)
    queue.append(ind)
    while len(queue) != 0:
        tmp = queue[0]
        del queue[0]
        line = arr[tmp]
        bfs.append(tmp+1)
        for i in range(len(line)):
            if not i in visit and line[i] == 1:
                queue.append(i)
                visit.add(i)

arr = []
arrSize, inputSize, startInd = map(int, stdin.readline().split())
tmp = [0] * arrSize
for _ in range(arrSize):
    arr.append(tmp.copy())

for _ in range(inputSize):
    r,c = map(int, stdin.readline().split())
    arr[r-1][c-1] = 1
    arr[c-1][r-1] = 1

DFS(arr,startInd-1,set([]))
BFS(arr, startInd-1,[], set([]))

for i in range(len(dfs)-1):
    print(dfs[i], end=" ")
print(dfs[len(dfs)-1])

for i in range(len(bfs)-1):
    print(bfs[i], end=" ")
print(bfs[len(bfs)-1])