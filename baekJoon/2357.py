from sys import stdin

def initTree(tree, leafs, nodeInd, start,end):
    if start == end:
        tree[nodeInd] = [leafs[start], leafs[start]]
        return tree[nodeInd]

    left  = initTree(tree, leafs, nodeInd*2  , start, (start+end)//2)
    right = initTree(tree, leafs, nodeInd*2+1, (start+end)//2+1, end)
    tree[nodeInd] = [min(left[0], right[0]), max(left[1], right[1])]
    return tree[nodeInd]

def search(tree, ind, start, end, l, r):
    if l > end or r < start:
       return tree[0]
    if l<= start and end<=r :
        return tree[ind]
    left = search(tree, ind*2, start,(start+end)//2, l, r )
    right = search(tree, ind*2+1, (start+end)//2+1, end, l, r)
    return [min(left[0], right[0]), max(left[1], right[1])]

n,m = map(int, stdin.readline().split())
tree = [[10**9+1,0]]*(2**(len(bin(n))-1))
leaf = [-1]
for _ in range(n):
    leaf.append(int(stdin.readline()))
initTree(tree, leaf, 1, 1,n)
# print(tree)

for _ in range(m):
    a,b = map(int, stdin.readline().split())
    ans = search(tree, 1, 1, n, a, b)
    print("{} {}".format(ans[0], ans[1]))
    