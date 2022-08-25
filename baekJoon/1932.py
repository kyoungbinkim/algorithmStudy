from sys import stdin
rl = stdin.readline
triArr= []

def update(upline, downline):
    for i in range(len(upline)):
        upline[i] = max(downline[i:i+2]) + upline[i]

for _ in range(int(rl())):
    triArr.append(list(map(int, rl().split())))

for i in range(len(triArr)-1, 0, -1):
    update(triArr[i-1], triArr[i])
print(triArr[0][0])
