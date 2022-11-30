from sys import stdin

def BFS(arr, n):
    visit = set([n])
    que = [n]

    while len(que) > 0:
        tmp = que[0]
        del que[0]

        for i in range(len(arr)):
            if arr[tmp][i] == 1 and i not in visit:
                que.append(i)
                visit.add(i)
    return visit

n = int(stdin.readline())
price =list(map(int, stdin.readline().split()))
graph, linkg = [],[]
for _ in range(n):
    graph.append([int(s) for s in stdin.readline().replace('\n', '')])
    linkg.append([0] * n)

for i in range(n):
    tmp = BFS(graph, i)
    for j in tmp:
        linkg[i][j] = 1
for l in linkg:
    print(l)

