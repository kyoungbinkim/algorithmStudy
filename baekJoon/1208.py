from sys import stdin

N,S = map(int, stdin.readline().split())
numList = list(map(int, stdin.readline().split()))
ansNum = 0
ans = []
for _ in range(N):
    ans.append(([0]*N).copy())


for ind in range(N):
    tmp = numList[ind]
    for i in range(N):
        for j in range(N):
            if i>ind or j<ind:
                continue
            ans[i][j] += tmp

for i in range(N):
    for j in range(N):
        if j<i:
            continue
        if ans[i][j] == S:
            ansNum+=1
print(ansNum)