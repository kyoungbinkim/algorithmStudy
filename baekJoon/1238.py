from sys import stdin

def update(arr, ans, node, visit):
    visit.add(node)
    
    for i in range(len(arr[node])):
        if i in visit or arr[i]==0:
            continue
        ans[node] = min(ans[node], )

def dijkstra(arr, start, n):
    ans = [float("inf")]*n
    visit = set([start])
    
    
    
    

n,m,x = map(int, stdin.readline().split())

dist = []
for _ in range(n):
    dist.append([0]*n)

for _ in range(m):
    x,y,d = map(int, stdin.readline().split())
    dist[x-1][y-1] = d
    dist[y-1][x-1] = d

