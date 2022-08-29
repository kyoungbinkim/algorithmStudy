n = int(input())
ans = [1, 3]

for i in range(2,n):
    ans.append((ans[i-2]*2 + ans[i-1])%10007)
print(ans[n-1])
