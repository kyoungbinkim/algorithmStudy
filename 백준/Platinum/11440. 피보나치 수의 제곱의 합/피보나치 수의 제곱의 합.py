p = 1_000_000_007

def matMul(a,b):
    ans = [[0,0],[0,0]]

    for row in range(2):
        for col in range(2):
            for i in range(2):
                ans[row][col] += a[row][i] * b[i][col]
                ans[row][col] %= p
    return ans

def matPow(a,n):
    if n == 1:
        return a
    
    bn = bin(n)[2:]

    sq = a
    ret = [[1,0],[0,1]]
    for i in range(len(bn)-1, -1, -1):
        if bn[i] == '1':
            ret = matMul(ret, sq)
        sq = matMul(sq, sq)
    return ret


n = int(input())
ans = matPow([[1,1],[1,0]], n-1)
# print(ans)
print((sum(ans[0]) * sum(ans[1]))%p)