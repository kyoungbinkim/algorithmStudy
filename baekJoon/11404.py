from sys import stdin

n,m = int(stdin.readline()), int(stdin.readline())
G = []
for i in range(n):
    G.append([float("inf")]*n)
    G[i][i] = 0

for _ in range(m):
    x,y,d = map(int, stdin.readline().split())
    G[x-1][y-1] = min(d, G[x-1][y-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            G[i][j] = min(G[i][j], G[i][k]+G[k][j])

for line in G:
    for l in line:
        if l == float("inf"):
            print(0, end=" ")
        else:
            print(l, end=" ")
    print("")