from sys import stdin
from math import floor

n = int(stdin.readline())
ckr = [list(map(lambda x: int(x), stdin.readline().split())) for _ in range(n)]
edges = []
visit = set()
ans, cnt = 0, 0

def calc(a,b):
    return floor((a[1] + b[1]) / (abs(a[0] - b[0])))


for i in range(n):
    for j in range(i):
        tmp = calc(ckr[i], ckr[j])
        edges.append(( i, j, tmp))

edges.sort(key=lambda x: x[2], reverse=True)
# print(edges)
parents = [i for i in range(n)]
def find_set(x):
    # x의 대표원소를 찾아서 리턴한다.
    while x != parents[x]:
        x = parents[x]
    return x

deg = [0 for _ in range(n)]
board = [[0 for _ in range(n)] for _ in range(n)]
for a,b,l in edges:
    fsa, fsb = find_set(a), find_set(b)
    if fsa != fsb:
        parents[fsa] = fsb
        deg[a] += 1
        deg[b] += 1
        board[a][b] = 1
        board[b][a] = 1
        ans += l
        cnt += 1
        if cnt == n-1:
            break
print(ans)

for _ in range(n-1):
    # print(deg, board)
    for (idx, val) in enumerate(deg):
        if val == 1:
            for i in range(n):
                if board[idx][i] == 1:
                    board[idx][i] = 0
                    board[i][idx] = 0
                    deg[i] -= 1
                    deg[idx] -= 1
                    print(i+1 , idx+1)
                    break
            break

