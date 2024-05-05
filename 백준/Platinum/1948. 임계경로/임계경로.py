from sys import stdin
from collections import deque

c = int(stdin.readline())
r = int(stdin.readline())

deg = [0 for _ in range(c)]
b = [[] for _ in range(c)]

for _ in range(r):
    s, e, l = map(lambda x: int(x)-1, stdin.readline().split()) 
    deg[e] += 1
    b[s].append([e,l+1])
start, end = map(lambda x: int(x)-1, stdin.readline().split())

ans = [[0, set()] for _ in range(c)]
topo = deque([start])
while len(topo):
    node = topo.popleft()
    for dest, dis in b[node]:
        deg[dest] -= 1

        if ans[dest][0] < ans[node][0] + dis:
            ans[dest] = [ans[node][0] + dis, ans[node][1].union(set([(node,dest)]))]
        elif ans[dest][0] == ans[node][0] + dis:
            ans[dest][1] = ans[dest][1].union(ans[node][1].union(set([(node,dest)])))
        
        if deg[dest] == 0:
            topo.append(dest)
    if node != end:
        ans[node] = [0, set()]
    # print(ans)
print(ans[end][0])
print(len(ans[end][1]))