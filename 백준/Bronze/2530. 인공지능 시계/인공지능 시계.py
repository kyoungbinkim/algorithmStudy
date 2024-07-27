from sys import stdin

h, m, s = map(int, stdin.readline().split())
ds = int(stdin.readline())

s += ds

m += s // 60
s %= 60

h += m // 60
m %= 60

h %= 24

print(h, m, s)