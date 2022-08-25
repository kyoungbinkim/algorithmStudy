from sys import stdin

setSize = int(stdin.readline())
numSet = set(map(int, stdin.readline().split()))
target = int(stdin.readline())
ans = 0
for i in numSet:
    if target-i in numSet:
        ans += 1
print(ans//2)