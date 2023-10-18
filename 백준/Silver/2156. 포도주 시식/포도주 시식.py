from sys import stdin

n = int(stdin.readline())

dp = [[0,0,0,0]]

for _ in range(n):
    num = int(stdin.readline())
    tmp = [0,0,0,0]

    tmp[0] = max(dp[-1][2], dp[-1][0])
    tmp[1] = tmp[0] + num
    tmp[2] = max(dp[-1][1], dp[-1][3])
    tmp[3] = dp[-1][1] + num
    dp.append(tmp)

print(max(dp[-1]))
