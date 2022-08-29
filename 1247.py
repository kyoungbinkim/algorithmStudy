from sys import stdin
rl = stdin.readline

for _ in range(3):
    sum = 0
    for _ in range(int(rl())):
        sum += int(rl())
    if sum == 0:
        print(0)
    elif sum > 0:
        print("+")
    else:
        print("-")