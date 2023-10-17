from sys import stdin
from collections import deque

N,k = map(int, stdin.readline().split())

K = k
cnt = 0
num = stdin.readline().removesuffix('\n')
ans = deque()

for n in num:
    while len(ans) and 0<k:
        if ans[-1] < n:
            ans.pop()
            k -= 1
        else:
            break
    ans.append(n)

while len(ans) > N-K:
    ans.pop()
print("".join(ans))


