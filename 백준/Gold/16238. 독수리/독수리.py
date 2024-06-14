from sys import stdin
from heapq import heapify, heappop

n = int(stdin.readline())
heapify(nums := list(map(lambda x:-int(x), stdin.readline().split())))

ans = -heappop(nums)
tmp = ans
for i in range(1, n):
    tmp -= heappop(nums)
    tmp -= i
    # print(ans, tmp, i)
    ans = max(ans, tmp)
print(ans)