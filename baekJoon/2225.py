N,k = map(int, input().split())
def update(ans):
    tmp = []
    for i in range(len(ans)):
        tmp.append(sum(ans[:i+1]))
    return tmp

ans = []
for i in range(N+1):
    ans.append(1)

for i in range(1,k):
    ans = update(ans)
    print(ans)
print(ans[N] % 1000000000)


# 