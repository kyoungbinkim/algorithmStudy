from sys import stdin
from heapq import heapify, heappop

n, ans = int(stdin.readline()), 0
heapify(nums := list(map(int, stdin.readline().split())))

while len(nums):
    ans += 1
    for _ in range(heappop(nums) -1):
        if len(nums) == 0:
            break
        heappop(nums)
print(ans)