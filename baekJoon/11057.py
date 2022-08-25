n = int(input())
ret = [1,1,1,1,1,1,1,1,1,1]
for _ in range(1,n):
    s = sum(ret)
    tmp = []
    for i in range(10):
        tmp.append((s - sum(ret[:i]))% 10007)
    ret = tmp.copy()
print(sum(ret)%10007)
