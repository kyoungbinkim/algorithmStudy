
from sys import stdin, setrecursionlimit
from math import ceil, log2

setrecursionlimit(100000)
# p = 1000000007
size = 1000000
size = 5

nodeNum  = 2 ** ceil(log2(size) + 1) 
offset = nodeNum//2
print('\n',nodeNum, offset, nodeNum-offset, '\n')

n = int(stdin.readline())
tree = [0 for _ in range(nodeNum)]
leafs = [0 for _ in range(size + 1)]

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

def search(s,e, idx, num):
    # print(idx)
    

    if idx > offset :
        tree[idx] -= 1
        return idx - offset + 1
    
    if tree[idx*2] >= num:
        ans = search(s,e,idx*2, num)
    else:
        ans = search(s,e, idx*2+1, num-tree[idx*2])
    tree[idx] -= 1
    return ans
    
    

def update(s, e, leaf, idx, up):
    
    if s > leaf or e < leaf:
        return
    
    print(leaf, idx)
    tree[idx] += up 
    if(e<=s):
        return

    
    mid = (s+e) // 2
    update(s, mid, leaf, idx*2, up)
    update(mid+1, e, leaf, idx*2+1, up)

# init(0, n-1, 1)
# print(tree)

for _ in range(n):
    cmd = list(map(int, stdin.readline().split()))
    if cmd[0] == 1:
        # print('\n\n\n\n')
        print(search(0, 0 ,1, cmd[1]))
        # up = b - leafs[a-1]
        # leafs[a-1] = b
        
        # update(0, n-1, a-1, 1, up)
        
        pass
    else:
        tree[cmd[1] + offset -1] = cmd[2]
        update(0,offset-1, cmd[1]-1, 1, cmd[2])
        # for i in range(nodeNum):
        #     if tree[i]:
        #         print(i, tree[i])
    
    print(tree)

    
