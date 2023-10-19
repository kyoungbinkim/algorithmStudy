from sys import stdin
from heapq import heappop, heappush

n = int(stdin.readline())

schedules = []

for _ in range(n):
    schedules.append(tuple(map(int, stdin.readline().split())))
schedules.sort()

heap,ans = [-schedules[0][1]], 1

# print(schedules)
for s in schedules[1:]:
    # print(heap, ans)
    if -heap[0] > s[1]:
        heappop(heap)
        heappush(heap, -s[1])
    elif -heap[0] <= s[0]:
        ans += 1
        heappush(heap, -s[1])
print(ans)
