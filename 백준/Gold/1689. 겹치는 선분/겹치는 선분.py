from sys import stdin

n = int(stdin.readline())

numlist = []

for _ in range(n):
    a,b = map(int, stdin.readline().split())
    numlist.append((a,1))
    numlist.append((b,-1))
numlist.sort()

ans, cnt = 0, 0

for i in range(2 * n):
    cnt += numlist[i][1]
    ans = max(ans, cnt)
print(ans)