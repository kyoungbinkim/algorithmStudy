from sys import stdin
from heapq import heappush, heappop
from itertools import combinations


def solve():
    ans = [0 , float('inf')]
    n, m, k = map(int,stdin.readline().split())
    alice = list(map(int,stdin.readline().split()))
    bob = list(map(int,stdin.readline().split()))

    aheap = []
    bheap = []
    for l in combinations(range(n), k):
        heappush(aheap, sum(alice[i] for i in l))
    for l in combinations(range(m), k):
        heappush(bheap, sum(bob[i] for i in l))
    
    mina = aheap[0]
    minb = bheap[0]

    if len(aheap) == 1 :
        maxa = aheap[0]
    if len(bheap) == 1:
        maxb = bheap[0]

    cura = heappop(aheap)
    curb = heappop(bheap)
    curlen = abs(cura - curb)
    ans[1] = curlen
    # print(cura ,aheap)
    # print(curb, bheap)
    while len(aheap) and len(bheap):
        if len(aheap) == 1 :
            maxa = aheap[0]
        if len(bheap) ==  1:
            maxb = bheap[0]
        nexta = aheap[0]
        nextb = bheap[0]
        nextlen = abs(nexta - nextb)
        curalen = abs(cura - nextb)
        curblen = abs(curb - nexta)
        curlen = min(curlen, curalen, curblen, nextlen)

        if curlen == nextlen:
            cura = heappop(aheap)
            curb = heappop(bheap)
            ans[1] = min(ans[1], curlen)
        elif curlen == curalen:
            curb = heappop(bheap)
            ans[1] = min(ans[1], curlen)
        elif curlen == curblen:
            cura = heappop(aheap)
            ans[1] = min(ans[1], curlen)
        else:
            ans[1] = min(ans[1], curlen)
            cura = heappop(aheap)
            curb = heappop(bheap)
            curlen = abs(cura - curb)
            ans[1] = min(ans[1], curlen)
        # print(ans)

    # print(aheap, bheap)
    while len(aheap):
        if len(aheap) == 1 :
            maxa = aheap[0]
        cura = heappop(aheap)
        curlen = abs(cura - maxb)
        ans[1] = min(ans[1], curlen)
    while len(bheap):
        if len(bheap) == 1 :
            maxb = bheap[0]
        curb = heappop(bheap)
        curlen = abs(maxa - curb)
        ans[1] = min(ans[1], curlen)
    ans[0] = max(abs(maxa-minb), abs(mina-maxb))
    ans.reverse()
    print(*ans)

for _ in range(int(stdin.readline())):
    solve(  )