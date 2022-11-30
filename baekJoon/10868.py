from sys import stdin

def initTree(tree, leafs, ind, start, end):
    if start == end:
        tree[ind] = leafs[start]
        return tree[ind]
    
    tree[ind] = min(initTree(tree, leafs, ind*2, start, (start+end)//2), initTree(tree,leafs, ind*2+1, (start+end)//2+1, end))
    return tree[ind]

def search(tree, ind, start, end, l, r):
    if l > end or r < start:
       return tree[0]
    if l<= start and end<=r :
        return tree[ind]
    left = search(tree, ind*2, start,(start+end)//2, l, r )
    right = search(tree, ind*2+1, (start+end)//2+1, end, l, r)
    return min(left, right)

n,m = map(int, stdin.readline().split())
tree = [10**9+1] + [0]*(2**(len(bin(n))-1))
leafs = [0]
for _ in range(n):
    leafs.append(int(stdin.readline()))

initTree(tree, leafs, 1, 1, n)

for _ in range(m):
    a,b = map(int, stdin.readline().split())
    print(search(tree, 1, 1, n, a, b))