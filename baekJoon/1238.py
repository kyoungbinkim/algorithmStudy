from sys import stdin
import heapq

<<<<<<< HEAD
def update(arr, ans, node, visit,n, h):
    visit.add(node)
    
    tmp = arr[node]
    for i in range(n):
        if i in visit or tmp[i]==0:
            continue
        val = ans[node]+arr[node][i]
        ans[i] = min(val, ans[i])
        if ans[i] ==val:
            heapq.heappush(h,(val, i))
    # print(ans, visit)
    return

def selectNode(ans, visit):
    minInd = None
    
    for i in range(len(ans)):
        if i in visit:
            continue
        elif minInd == None:
            minInd = i
            continue

        if ans[i] < ans[minInd]:
            minInd = i
    return minInd


def dijkstra(arr, start, n, dist=None):
    maxHeap = []
    ans = arr[start].copy()
    ans[start] = 0
    for (val,ind) in zip(ans, range(n)):
        heapq.heappush(maxHeap, (val, ind))

    visit = set([])
    while len(visit)<n:
        d,start = heapq.heappop(maxHeap)
        if ans[start] < d:
            continue
        update(arr, ans, start,visit, n, maxHeap)
        if dist in visit:
            return ans
        

    return ans
    

n,m,X = map(int, stdin.readline().split())
dist = []
for _ in range(n):
    dist.append([float("inf")]*n)

for _ in range(m):
    x,y,d = map(int, stdin.readline().split())
    dist[x-1][y-1] = d

ans = dijkstra(dist, X-1, n)

for i in range(n):
    if i == X-1:
        continue
    tmp = dijkstra(dist, i, n, dist=X-1)
    ans[i] += tmp[X-1]
print(max(ans))
=======
n,m,X = map(int, stdin.readline().split())

dist = []
for i in range(n):
    dist.append([float("inf")]*n)
    dist[i][i] = 0

for _ in range(m):
    x,y,d = map(int, stdin.readline().split())
    dist[x-1][y-1] = min(d, dist[x-1][y-1])
>>>>>>> 6111b361fd157218d249dcd93a67013dd4e27d79

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = 0
for i in range(n):
    if i == x:
        continue
    v = dist[i][X-1] + dist[X-1][i]
    if v > ans:
        ans = v
print(ans)
