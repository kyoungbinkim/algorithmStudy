import heapq
from sys import stdin

n = int(stdin.readline())
heap = []

for _ in range(n):
    tmp = int(stdin.readline())
    if tmp == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap)[1])
        continue
    tmp_abs = abs(tmp)

    heapq.heappush(heap, [tmp_abs,tmp])