
from sys import stdin, setrecursionlimit
from math import ceil, log2

setrecursionlimit(10000)
# p = 1000000007
n, k= map(int, stdin.readline().split())

tree = [0 for _ in range( 2 ** ceil(log2(n) + 1))]
leafs = [0 for _ in range(n)]
# print(len(tree), leafs)

def init(s, e, idx):
    if s==e:
        tree[idx] = leafs[s]
        return tree[idx]
    
    mid = (s + e) // 2
    tree[idx] = (init(s,mid, idx*2) + init(mid+1,e, idx*2 + 1)) 
    return tree[idx]

def sum(s, e, idx, l, r):
    
    if l>e or s>r:
        return 0
    
    if l <= s and e <= r:
        # print(tree[idx])
        return tree[idx]
    
    mid = (s + e) // 2

    return (sum(s,mid, idx*2, l, r) + sum(mid+1,e, idx*2+1, l, r) )

def update(s, e, leaf, idx, up):
    if s > leaf or e < leaf:
        return
    
    tree[idx] = (tree[idx]  + up ) 
    if(e<=s):
        return

    
    mid = (s+e) // 2
    update(s, mid, leaf, idx * 2, up)
    update(mid+1, e, leaf, idx*2 + 1, up)

# init(0, n-1, 1)
# print(tree)

for _ in range(k):
    cmd, a, b = map(int ,stdin.readline().split())
    if cmd == 1:

        up = b - leafs[a-1]
        leafs[a-1] = b
        
        update(0, n-1, a-1, 1, up)
        # print(tree)
    else:

        ans = sum(0, n-1, 1, a-1, b-1) if b > a else sum(0, n-1, 1, b-1, a-1)
        print(ans)

