from sys import stdin
import heapq

upperBound = 2 << 31

k, n = map(int, stdin.readline().split())
primeList = list(map(int, stdin.readline().split()))

def select(plist, cnt, dep, num):
    if cnt == dep:
        return [num]

    tmp = []
    for p in plist:
        tmp += select(plist, cnt+1, dep, num*p)
    
    return tmp
    


heap = []
for i in range(k):
    heapq.heappush(heap, primeList[i])

# print(select(primeList, 0, 1, 1))
# print(select(primeList, 0, 2, 1))
# print(select(primeList, 0, 3, 1))