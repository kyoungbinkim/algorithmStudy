from sys import stdin
from heapq import heapify, heappop

n = int(stdin.readline())
nums = list(map(lambda x: -int(x), stdin.readline().split()))
heapify(nums)

ans = 0
rect = []

while len(nums) > 1:
    a,b = -heappop(nums), -heappop(nums)
    
    if a==b:
        rect.append(a)
    
    elif a-1 == b:
        rect.append(b)
    
    else:
        while len(nums):
            a = b
            b = -heappop(nums)
            if a==b:
                rect.append(a)
                break
            elif a-1 == b:
                rect.append(b)
                break
    
    if len(rect) == 2:
        ans += rect[0]*rect[1]
        rect = []
print(ans)