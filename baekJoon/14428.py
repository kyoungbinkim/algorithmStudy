from sys import stdin

size = int(stdin.readline())
leafs =[10**9+1]+ list(map(int, stdin.readline().split()))
tree = [0] * (2 ** (len(bin(size))-1))
def init(tree, ind, start, end ):
    if start == end:
        tree[ind] = start
        return tree[ind]
    tree[ind] = min(init(tree, ind*2, start, (start+end)//2), init(tree, ind*2+1, (start+end)//2+1, end),
    key=lambda x: leafs[x])
    return tree[ind]

def search(tree, ind, start, end, l, r):
    if l > end or r < start:
       return 0
    if l<= start and end<=r :
        return tree[ind]
    return min(search(tree, ind*2, start, (start+end)//2, l, r), search(tree, ind*2+1, (start+end)//2+1, end, l, r),
    key=lambda x: leafs[x])

def update(tree, ind, start, end, changeInd, val=0):
    if changeInd < start or changeInd > end:
        return tree[ind]
    if start == end:
        tree[ind] = start
        return tree[ind]
    tree[ind] = min(update(tree, ind*2, start, (start+end)//2,changeInd ), update(tree, ind*2+1, (start+end)//2+1, end, changeInd),
    key=lambda x: leafs[x])
    return tree[ind]
    
init(tree, 1, 1, size)
# print(tree)

num = int(stdin.readline())
for _ in range(num):
    cmd = list(map(int, stdin.readline().split()))
    if cmd[0] == 2:
        print(search(tree, 1, 1, size, cmd[1], cmd[2]))
    else:
        leafs[cmd[1]] = cmd[2]
        update(tree, 1, 1,size, cmd[1])
        # print(cmd, tree)

