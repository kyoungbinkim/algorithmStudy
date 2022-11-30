from sys import stdin

def initTree(tree, leafs, nodeInd, start,end):
    if start == end:
        tree[nodeInd] = leafs[start]
        return tree[nodeInd]

    left  = initTree(tree, leafs, nodeInd*2  , start, (start+end)//2)
    right = initTree(tree, leafs, nodeInd*2+1, (start+end)//2+1, end)
    tree[nodeInd] = left + right
    return tree[nodeInd]

def search(tree, ind, start, end, l, r):
    if l > end or r < start:
       return 0
    if l<= start and end<=r :
        return tree[ind]
    left = search(tree, ind*2, start,(start+end)//2, l, r )
    right = search(tree, ind*2+1, (start+end)//2+1, end, l, r)
    return left + right

def update(tree,leafs, ind, start, end, changeInd, val=0):
    if changeInd < start or changeInd > end:
        return tree[ind]
    if start == end:
        tree[ind] = leafs[start]
        return tree[ind]
    tree[ind] = update(tree,leafs, ind*2, start, (start+end)//2,changeInd )+ update(tree, leafs,ind*2+1, (start+end)//2+1, end, changeInd)

    return tree[ind]

n,m,k = map(int, stdin.readline().split())
leafs = [0]
tree = [0]*(2**(len(bin(n))-1))

for _ in range(n):
    leafs.append(int(stdin.readline()))

initTree(tree, leafs, 1,1,n)

for _ in range(m+k):
    cmd = list(map(int, stdin.readline().split()))
    if cmd[0] ==1 :
        leafs[cmd[1]] = cmd[2]
        update(tree, leafs, 1, 1, n, cmd[1])
        # print(leafs, tree)
    else:
        print(search(tree, 1,1,n, cmd[1], cmd[2]))



    