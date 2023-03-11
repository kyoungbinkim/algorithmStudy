from sys import stdin

listSize = int(stdin.readline())
numList = [None] + list(map(int, stdin.readline().split()))

orderNum = int(stdin.readline())


ans = [[0]*(listSize+1) for _ in range(listSize+1)]

for i in range(1,listSize+1):
    ans[i][i] = 1
    start,end =i, i
    for j in range(1,min(i, listSize+1-i)):
        start -= 1
        end += 1
        if numList[start] == numList[end]:
            ans[start][end] = 1
        else:
            break
    start, end = i, i+1
    for j in range(min(i, listSize-i)):
        if numList[start] == numList[end]:
            ans[start][end] = 1
        else:
            break
        start -= 1
        end += 1

# print(ans)
# for l in ans:
#     print(l)
for _ in range(orderNum):
    s,e = map(int, stdin.readline().split())
    print(ans[s][e])
