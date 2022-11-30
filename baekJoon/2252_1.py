from sys import stdin

def getZeroNode(arr,size, s):
    ans = []
    for i in range(size):
        if i in s:
            continue
        tmp = 0
        for j in range(size):
            if (1<<i & arr[j]) > 0: # arr[j][i]
                tmp += 1
                break
        if tmp == 0:
            ans.append(i)
    return ans

n,m = map(int, stdin.readline().split())
Graph = [[] for _ in range(n)]
degree = [0] * n
ans = []

for _ in range(m):
    a,b = map(int, stdin.readline().split())
    Graph[a-1].append(b-1)
    degree[b-1] += 1

# for g in Graph:
#     print(bin(g))
# print()

while len(ans) < n:
    d = []
    for i in range(n):
        if degree[i] == 0:
            d.append(i)
            degree[i] = -1
    ans += d
    for i in d:
        for ind in Graph[i]:
            degree[ind] -= 1
# print(ans)

for i in range(n-1):
    print(ans[i]+1, end=" ")
print(ans[n-1]+1)
