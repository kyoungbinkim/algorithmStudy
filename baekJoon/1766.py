from sys import stdin

n,m = map(int, stdin.readline().split())
Graph = [[] for _ in range(n)]
degree = [0] * n
ans = []

for _ in range(m):
    a,b = map(int, stdin.readline().split())
    Graph[a-1].append(b-1)
    degree[b-1] += 1

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
