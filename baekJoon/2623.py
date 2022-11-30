from sys import stdin

## True : 싸이클 존재
def checkCycle(G, ind, visit, fin):
    ret = False
    visit[ind] = 1
    next = G[ind]

    for j in next:
        if visit[j] == 0:
            ret = checkCycle(G, j, visit, fin)
            if ret:
                return True
        elif fin[j] == 0:
            return True
    fin[ind] = 1
    return ret

n,m = map(int, stdin.readline().split())
Graph = [[] for _ in range(n)]
degree = [0] * n
ans = []

for _ in range(m):
    tmp = list(map(int, stdin.readline().split()))
    for i in range(1, len(tmp)-1):
        Graph[tmp[i]-1].append(tmp[i+1]-1)
        degree[tmp[i+1]-1] += 1

for i in range(n):
    if degree[i] == 0:
        flag=checkCycle(Graph, i, [0]*n, [0]*n)
        if flag:
            break

if flag:
    print(0)
else:
    while len(ans) < n:
        d = []
        for i in range(n):
            if degree[i] == 0:
                d.append(i)
                degree[i] = -1
                break
        ans += d
        for i in d:
            for ind in Graph[i]:
                degree[ind] -= 1

    for i in range(n-1):
        print(ans[i]+1, end=" ")
    print(ans[n-1]+1)
