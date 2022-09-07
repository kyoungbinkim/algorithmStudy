from sys import stdin

Start, End = map(int, stdin.readline().split())

sbin,ebin = bin(Start)[2:], bin(End)[2:]
sbin = sbin.zfill(len(ebin))
print(sbin, ebin)

