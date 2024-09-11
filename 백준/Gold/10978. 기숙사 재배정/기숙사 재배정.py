from sys import stdin

tmp = [0, 0, 1, 2]

for i in range(4, 21):
    tmp.append((i)*tmp[-1] + (-1)**i  )
for _ in range(int(stdin.readline())):
    print(tmp[int(stdin.readline())])