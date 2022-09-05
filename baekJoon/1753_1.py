from sys import stdin
import heapq

def update(node, ind, ans, visit, n, h):
    visit.add(ind)
    # print(ans, ind, node[ind], visit)
    for k in node[ind].keys():
        if k in visit:
            continue
        ans[k] = min(ans[k], ans[ind]+node[ind][k])
        if ans[k] == ans[ind]+node[ind][k]:
            heapq.heappush(h, (ans[k], k))


def dijkstra(node, start, n):
    maxHeap = []
    ans = [float("inf")]*n
    for k in node[start].keys():
        ans[k] = node[start][k]
    visit = set([start])
    for (val, ind) in zip(ans, range(n)):
        heapq.heappush(maxHeap, (val, ind))
    
    while len(visit) < n:
        val, minInd = heapq.heappop(maxHeap)
        if val > ans[minInd] or minInd in visit:
            continue
        update(node, minInd, ans, visit, n, maxHeap)
    return ans
        

n,m = map(int, stdin.readline().split())
start = int(stdin.readline())
G = {}
for i in range(n):
    G.update({i:{}})
for _ in range(m):
    x,y,d = map(int, stdin.readline().split())
    if G[x-1].get(y-1) == None:
        G[x-1].update({y-1:d})
    else:
        G[x-1][y-1] = min(d, G[x-1][y-1])
# print(G)
ans = dijkstra(G, start-1, n)
for i in range(n):
    if i == start-1:
        print(0)
    elif type(ans[i]) == type(1):
        print(ans[i])
    else:
        print(str(ans[i]).upper())