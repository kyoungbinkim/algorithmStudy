from sys import stdin

tmp =  list(map(int, stdin.readline().split()))
a = tmp[0] % tmp[1]
b = tmp[1]
for _ in range(tmp[2]-1):
    a = (a*10)%b
print((10 * a)//b) 