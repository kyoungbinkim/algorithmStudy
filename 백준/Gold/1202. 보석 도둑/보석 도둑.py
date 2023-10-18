from sys import stdin
from heapq import heappush, heappop

n,k = map(int,stdin.readline().split())
heap, vHeap, bags, ans = [], [],[], 0

for _ in range(n):
    m,v = map(int ,stdin.readline().split())

    heappush(heap, (m, -v))


for _ in range(k):
    heappush(bags, int(stdin.readline()))


while len(bags):
    num = heappop(bags)
    while len(heap):
        bling = heappop(heap)
        if num < bling[0]:
            heappush(heap, bling)
            break
        heappush(vHeap, bling[1])
    
    if len(vHeap):
        ans -= heappop(vHeap)
        
print(ans)