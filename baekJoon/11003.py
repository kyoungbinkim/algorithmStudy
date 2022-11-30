from sys import stdin

def init(tree, leafs, ind, start, end):
    if start >= end:
        tree[ind] = leafs[start]
        return leafs[start]
    mid = (start+end)//2
    tree[ind] = min(init(tree, leafs, ind*2, start, mid), init(tree, leafs, ind*2+1, mid+1, end))
    return tree[ind]

def search(tree,ind, start, end, scope):
    # print(ind, start, end, scope)
    if scope[0] <= start and end <= scope[1]:
        return tree[ind]
    if (scope[0] > end) or (scope[1] < start):
        return float("inf")
    mid = (start+end)//2
    return min(search(tree,ind*2, start, mid, scope),search(tree,ind*2+1, mid+1, end, scope))

n,l = map(int ,stdin.readline().split())
numlist = list(map(int, stdin.readline().split()))
tree = [0] * (2**(n.bit_length()+1))
ans = [numlist[0]]
init(tree, numlist, 1, 0, n-1)

for i in range(1,l):
    ans.append(min(ans[i-1], numlist[i]))
for i in range(l, n):
    before = ans[i-1]
    if numlist[i] <= before:
        ans.append(numlist[i])
        continue
    elif numlist[i-l] == before:
        ans.append(search(tree,1, 0,n-1, [i-l+1 if i>=l else 0, i]))
    else:
        ans.append(before)
for a in ans:
    print(a, end=" ")
print()