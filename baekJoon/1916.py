import heapq
from sys import stdin


def update(dist,node,ans,visit,n, h ):
    visit.add(node)

    for i in range(n):
        if i in visit or dist[node][i] == float("inf"):
            continue

        ans[i] = min(ans[i], dist[node][i]+ans[node])
        if ans[i] == dist[node][i]+ans[node]:
            heapq.heappush(h, (ans[i], i))

def dijkstra(dist, start, end, n):
    maxHeap = []
    visit = set([start])
    ans = dist[start].copy()
    for (val, ind) in zip(ans, range(n)):
        heapq.heappush(maxHeap, (val, ind))
    
    while len(visit) < n:
        val, ind = heapq.heappop(maxHeap)
        if val > ans[ind] or ind in visit:
            continue
        update(dist, ind, ans, visit, n, maxHeap)
    return ans
         
n,m = int(stdin.readline()), int(stdin.readline())
dist = []
for _ in range(n):
    dist.append([float("inf")] * n)

for _ in range(m):
    a,b,d = map(int, stdin.readline().split())
    dist[a-1][b-1] = min(d, dist[a-1][b-1])
    

start, end = map(int, stdin.readline().split())
ans = dijkstra(dist, start-1, end-1, n)
print(ans[end-1])


