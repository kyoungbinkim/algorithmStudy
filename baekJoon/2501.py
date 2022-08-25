from sys import stdin
num, ret = map(int, stdin.readline().split())
cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1
    if cnt == ret:
        print(i)
        break
if cnt < ret:
    print(0)