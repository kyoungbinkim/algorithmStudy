from sys import stdin

n,k = map(int, stdin.readline().split())

graph, ans = [[] for _ in range(n)], [[0 for _ in range (n)] for _ in range(n)]

for _ in range(k):
    i,j = map(int, stdin.readline().split())
    graph[i-1].append(j-1)

visit = [0 for _ in range(n)]
def update(start, i):
    visit[i] = 1
    if graph[i] == [] :
        return

    for j in graph[i]:
        ans[start][j] = -1
        # ans[i][j] = -1
        ans[j][start] = 1
        # ans[j][i] = 1
        update(start, j)

def upd(before, i):
    if visit[i]:
        return
    visit[i] = 1
    # print(before)

    for j in graph[i]:
        for b in before:
            ans[b][j] = -1
            ans[j][b] = 1
        upd(before+[j], j)

for i in range(n):
    if visit[i] == 0:
        upd([i], i)
        # print(visit)

for tmp in ans:
    print(tmp)


it = int(stdin.readline())
for _ in range(it):
    i,j = map(int, stdin.readline().split())
    print(ans[i-1][j-1])