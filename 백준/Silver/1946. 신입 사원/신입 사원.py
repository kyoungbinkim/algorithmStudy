from sys import stdin

t = int(stdin.readline())
ans = []

for _ in range(t):
    n = int(stdin.readline())
    scores, cnt, th = [], 0, float("inf")
    for _ in range(n):
        scores.append(tuple(map(int, stdin.readline().split())))
    scores.sort()
    for i in range(n):
        if th > scores[i][1]:
            th = scores[i][1]
            cnt += 1
    ans.append(cnt)
for a in ans:
    print(a)