from sys import stdin
from heapq import heappush, heappop


n,k = map(int, stdin.readline().split())
ans = 0
plus = []
minus = []

for _ in range(n):
    ck  =  int(stdin.readline())
    if ck >= 0:
        heappush(plus, -ck)
    else:
        heappush(minus, ck)

cnt = 0
while len(plus):
    ans += heappop(plus)* -2
    cnt = 1
    while len(plus) and cnt < k:
        cnt += 1
        heappop(plus)


while len(minus):
    ans += heappop(minus) * -2
    cnt = 1
    while len(minus) and cnt < k:
        cnt += 1
        heappop(minus)

print(ans)

