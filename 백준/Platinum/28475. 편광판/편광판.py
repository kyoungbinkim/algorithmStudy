from sys import stdin

n, m = map(int, stdin.readline().split())
nodeCnt = 2**(len(bin(n)) - 1)
tree = [ False for _ in range(nodeCnt)]
b = list(map(lambda x: int(x) , stdin.readline().split()))
edges = [ abs(b[i]- b[i+1])%4 == 2 for i in range(n-1)]
def initTree():
    for i in range(n-1):
        tree[nodeCnt//2 + i] = edges[i]
    for i in range(nodeCnt//2 -1, 0, -1):
        tree[i] = tree[i*2] or  tree[i*2 + 1]

def getBound(idx):
    
    start,end = idx, end

    while start < nodeCnt//2:
        start *= 2
    
    while end < nodeCnt//2:
        end *= 2
        end += 1
    
    return (start, end)

def updateTree(idx, val):
    b[idx] = val
    if idx < n-1:
        edges[idx] = abs(b[idx]-b[idx+1])%4 == 2
    if idx > 0:
        edges[idx-1] = abs(b[idx-1]-b[idx])%4 == 2
    
    if idx < n-1:
        trIdx = nodeCnt//2 + idx
        tree[trIdx] = edges[idx]
    
    if idx > 0:
        trIdx = nodeCnt//2 + idx - 1
        tree[trIdx] = edges[idx-1]

    trIdx = nodeCnt//2 + idx
    while trIdx > 1:
        trIdx //= 2
        tree[trIdx] = tree[trIdx*2] or tree[trIdx*2 + 1]
    
    if idx > 0:
        trIdx = nodeCnt//2 + idx - 1
        while trIdx > 1:
            trIdx //= 2
            tree[trIdx] = tree[trIdx*2] or tree[trIdx*2 + 1]

    # print(b)
    # print(edges)
    # print(tree)
    # print()

def lca(start, end):
    trStart, trEnd = nodeCnt//2 + start, nodeCnt//2 + end
    while trStart != trEnd:
        trStart //= 2
        trEnd //= 2
    return trEnd

def canGo(start, end, node, left, right):
    
    if left > end or start > right:
        return False
    # print( start, end, node, left, right)
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return canGo(start, mid, node*2, left, right) or canGo(mid+1, end,node*2+1, left, right)



initTree()

for _ in range(m):
    q, i, j = map(lambda x: int(x)-1, stdin.readline().split())

    if q == 0:
        updateTree(i, j+1)
    else:
        if canGo(0, nodeCnt//2-1, 1, i, j-1):
            print(0)
        else:
            print(1)

