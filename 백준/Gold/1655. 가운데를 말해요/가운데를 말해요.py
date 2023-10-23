from sys import stdin
from heapq import heappop, heappush

left, right = [], []

n, FLAG = int(stdin.readline()), True

for _ in range(n):
    num = int(stdin.readline())

    if len(left) == 0:
        left = [-num]
    
    elif len(left) == len(right):
        if right[0] < num:
            heappush(left, -heappop(right))
            heappush(right, num)
        else:
            heappush(left, -num)
    else:
        if num <= -left[0]:
            heappush(right, -heappop(left))
            heappush(left, -num)
        else:
            heappush(right, num)
    print(-left[0])
