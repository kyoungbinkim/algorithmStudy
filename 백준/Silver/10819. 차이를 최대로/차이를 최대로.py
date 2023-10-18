from sys import stdin
from itertools import permutations

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

def calcAns(line):
    ans = 0
    for i in range(len(line)-1):
        ans += abs(line[i] - line[i+1])
    return ans

ans = 0
for k in permutations(nums):
    ans = max(ans, calcAns(k))
print(ans)
