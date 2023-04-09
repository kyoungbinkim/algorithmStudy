from sys import stdin

n = int(stdin.readline())


check = [0 for _ in range(n)]
ans = ['1']

print(2**n-1)
for i in range(1, n+1):
    ans = (ans[:-1]) + [str(i)] + (ans[:-1])[::-1] + [str(i)]
for a in ans:
    check[int(a)-1] = 1 if check[int(a)-1]==0 else 0
    tmp =''
    for c in check:
        tmp += str(c)
    print(a, end=' ')
