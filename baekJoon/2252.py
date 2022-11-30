from sys import stdin

class Vertex:
    def __init__(self, ind):
        self.ind = ind
        self.p = set([])
        self.c = set([])
    
    def addP(self, i):
        self.p.add(i)
    
    def addC(self, i):
        self.c.add(i)
    
    def delP(self, i):
        if i in self.p:
            self.p.remove(i)
    
    def empty(self):
        if len(self.p) == 0:
            return True
        return False

n,m = map(int, stdin.readline().split())
Graph = [Vertex(i) for i in range(n)]
ans = []

for _ in range(m):
    a,b = map(int, stdin.readline().split())
    Graph[a-1].addC(b-1)
    Graph[b-1].addP(a-1)

while len(ans) < n:
    updateInd = len(ans)
    for i in range(n):
        if i in ans:
            continue
        if Graph[i].empty():
            ans.append(i)
    
    for i in range(updateInd, len(ans)):
        Graph[i].c.clear()
        for j in range(n):
            Graph[j].delP(ans[i])
    # print(ans)
for i in range(n-1):
    print(ans[i]+1, end=" ")
print(ans[n-1]+1)

    

