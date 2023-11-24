from sys import stdin

N, a0 = map(int ,stdin.readline().split())
if N == 0:
    print(0)
    exit()
sequence = list(map(int, stdin.readline().split()))

start, end = sequence[0] - a0, sequence[0] - a0 + 1
for i in range(1,N):
    start = max((sequence[i] - a0) / (i+1), start)
    end   = min((sequence[i] - a0 + 1) / (i+1), end)
    # print(start, end)

if start >= end or start < 0:
    print(-1)
else:
    print(round(start, 10))