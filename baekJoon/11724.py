from sys import stdin
import sys
sys.setrecursionlimit(10**9)
n,m = map(int , stdin.readline().split())
arr = []
ans = 0
visit = set()
for _ in range(n):
    arr.append([0]*n)

for _ in range(m):
    a,b =map(int, stdin.readline().split())
    arr[a-1][b-1] =1
    arr[b-1][a-1] =1

def DFS(arr, ind, visit:set):
    visit.add(ind)
    for i in range(len(arr)):
        if arr[ind][i] == 1 and i not in visit:
            DFS(arr, i, visit)

for i in range(n):
    if i not in visit:
        DFS(arr, i, visit)
        ans += 1
print(ans)


