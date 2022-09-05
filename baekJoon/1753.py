from sys import stdin

def update(dist,node,ans,visit,n):
    visit.add(node)
    flag = False
    for i in range(n):
        if i in visit or dist[node][i] == float("inf"):
            continue
        ans[i] = min(ans[i], dist[node][i]+ans[node])
        flag = True
    return flag
def dijkstra(dist, start, n):
    visit = set([start])
    ans = dist[start].copy()
    f = True
    while len(visit) < n and f:
        minInd = None
        for i in range(n):
            if i in visit:
                continue
            if minInd == None:
                minInd = i
                continue
            if ans[minInd] > ans[i]:
                minInd = i
        f = update(dist, minInd, ans, visit, n)
    return ans


n,m = map(int, stdin.readline().split())
start = int(stdin.readline())
dist = []
for _ in range(n):
    dist.append([float("inf")]*n)

for _ in range(m):
    x,y,d = map(int, stdin.readline().split())
    dist[x-1][y-1] = min(d, dist[x-1][y-1])

ans = dijkstra(dist, start-1, n)

for i in range(n):
    if i == start-1:
        print(0)
    elif type(ans[i]) == type(1):
        print(ans[i])
    else:
        print(str(ans[i]).upper())