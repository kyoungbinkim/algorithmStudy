from sys import stdin

rl = stdin.readline

offset = ord('a')
c,n = map(int ,rl().split())
clist, nlist = [], []
setlist = [set() for _ in range(26)]

for _ in range(c):
    clist.append(rl().removesuffix('\n'))

for _ in range(n):
    nlist.append(rl().removesuffix('\n'))

for color in clist:
    perfix = ord(color[0])
    for name in nlist:
        setlist[perfix-offset].add(color+name)

del clist
del nlist

for _ in range(int(rl())):
    tmp = rl().removesuffix('\n')
    ind = ord(tmp[0]) - offset
    if tmp in setlist[ind]:
        print("Yes")
        setlist[ind].remove(tmp)
    else:
        print("No")