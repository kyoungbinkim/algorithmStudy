
from sys import stdin

nodeNum =int(stdin.readline())
network = {}
virus = {}

for i in range(1, nodeNum+1):
    virus.update({i:False})
    network.update({i:[]})

for _ in range(int(stdin.readline())):
    tmp = list(map(int, stdin.readline().split()))
    tmp.sort()
    a,b= tmp
    network[a].append(b)
    network[b].append(a)

def visit(ind):
    virus[ind] = True
    for i in network[ind]:
        if virus[i] == True:
            continue
        visit(i)
visit(1)
ans = 0
for i in range(1, nodeNum+1):
    ans += int(virus[i])
print(ans-1)