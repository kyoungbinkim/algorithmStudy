from sys import stdin
a,b,n = map(int, stdin.readline().split())

ans = 1
tmp = a
for i in bin(b)[2:][::-1]:
    if i == '1':
        ans = ans * tmp % n
    tmp = tmp * tmp % n
print(ans)