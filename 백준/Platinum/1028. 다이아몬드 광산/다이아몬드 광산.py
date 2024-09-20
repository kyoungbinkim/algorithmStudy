from sys import stdin

ans = 0
n,m = map(int, stdin.readline().split())
maxlen = min(n,m)//2+1  if min(n,m)%2 else min(n,m)//2-1

b = [[int(x) for x in stdin.readline().strip()] for _ in range(n)]

dp = [[[0,0] if  b[0][i] == 0 else [1,1] for i in range(m)] if j ==0 else 
     [[0,0] for _ in range(m)] for j in range(n)]

for i in range(1, n):
    for j in range(m):
        if j-1 >= 0 and b[i][j] == 1:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
        elif j-1 < 0 and b[i][j] == 1:
            dp[i][j][0] = 1
        
        if j+1 < m and b[i][j] == 1:
            dp[i][j][1] = dp[i-1][j+1][1] + 1
        elif j+1 >= m and b[i][j] == 1:
            dp[i][j][1] = 1
    

for i in range(n-1, -1, -1):
    for j in range(m):
        l = min(dp[i][j])
        
        if l < ans:
            continue
        # print(l)
        for k in range(l-1, ans-1, -1):
            # print(k, dp[i-k][j-k], dp[i-k][j+k])
            if i-k < 0 :
                continue
            if j-k >= 0 and dp[i-k][j-k][1]  > k and j+k < m and dp[i-k][j+k][0] > k:
                ans = k+1
                break

print(ans)