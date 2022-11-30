from sys import stdin
from itertools import combinations
Ai = []
N = int(stdin.readline())
ans = [None] * N
for _ in range(N):
    Ai.append(int(stdin.readline()))

ans[Ai[0]] = 1

