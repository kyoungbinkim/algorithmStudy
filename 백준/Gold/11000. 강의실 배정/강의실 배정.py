from sys import stdin
from heapq import heappop, heappush

n = int(stdin.readline())

schedules = []

for _ in range(n):
    schedules.append(tuple(map(int,stdin.readline().split())))
schedules.sort()
endTime = [schedules[0][1]]

for schedule in schedules[1:]:
    if endTime[0] <= schedule[0]:
        heappop(endTime)
    heappush(endTime, schedule[1])

print(len(endTime))