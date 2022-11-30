from sys import stdin

# graph {ind : [ind, len]}
def prim(G,size):
    visit = set([0])
    ans = [0]

    while len(ans) != size:
        m = float("inf")
        mind = None
        for f in visit:
            for t in G[f]:
                if t[0] in visit:
                    continue
                if m > t[1]:
                    m = t[1]
                    mind = t[0]
        ans.append(m)
        visit.add(mind)
    return ans

# {len :[ind, ind]}
def kruskal(G,size):
    rt = [-1 for _ in range(size)]
    visit = set([])
    ans = []

    for i in range(len(G)):
        l,a,b = G[i]

        if rt[a] == rt[b] and rt[a] >= 0:
            continue

        ans.append(l)
        visit.add(b)
        visit.add(a)
        if len(ans) == size -1:
            break
    # print(ans)
    return sum(ans)
        
v,e = map(int ,stdin.readline().split())
graph = {}
for i in range(v):
    graph.update({i: []})

for _ in range(e):
    a,b,l = map(int, stdin.readline().split())
    graph[a-1].append([b-1,l])
    graph[b-1].append([a-1,l])

print(sum(prim(graph,v)))