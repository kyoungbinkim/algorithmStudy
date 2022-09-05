from sys import stdin

n,m,X = map(int, stdin.readline().split())

dist = []
for i in range(n):
    dist.append([float("inf")]*n)
    dist[i][i] = 0

for _ in range(m):
    x,y,d = map(int, stdin.readline().split())
    dist[x-1][y-1] = min(d, dist[x-1][y-1])

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
