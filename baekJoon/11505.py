
from sys import stdin, setrecursionlimit
from math import ceil, log2

setrecursionlimit(10000)
p = 1000000007
n,m,k = map(int, stdin.readline().split())

tree = [0 for _ in range( 2 ** ceil(log2(n) + 1))]
leafs = [int(stdin.readline()) for _ in range(n)]
# print(len(tree), leafs)

def init(s, e, idx):
    if s==e:
        tree[idx] = leafs[s]
        return tree[idx]
    
    mid = (s + e) // 2
    tree[idx] = (init(s,mid, idx*2) * init(mid+1,e, idx*2 + 1)) % p
    return tree[idx]

def prod(s, e, idx, l, r):
    
    if l>e or s>r:
        return 1
    
    if l <= s and e <= r:
        # print(tree[idx])
        return tree[idx]
    
    mid = (s + e) // 2

    return (prod(s,mid, idx*2, l, r) * prod(mid+1,e, idx*2+1, l, r) )% p

def update(s, e, leaf, idx, up):
    if s > leaf or e < leaf:
        return
    
    tree[idx] = (tree[idx]  * up ) % p
    if(e<=s):
        return

    
    mid = (s+e) // 2
    update(s, mid, leaf, idx * 2, up)
    update(mid+1, e, leaf, idx*2 + 1, up)

init(0, n-1, 1)
# print(tree)

for _ in range(m+k):
    cmd, a, b = map(int ,stdin.readline().split())
    if cmd == 1:

        up = (b * pow(leafs[a-1], p-2, p)) % p
        leafs[a-1] = b
        if up == 0:
            init(0, n-1, 1)
        else:
            update(0, n-1, a-1, 1, up)
        # print(tree)
    else:
        print(prod(0, n-1, 1, a-1, b-1))