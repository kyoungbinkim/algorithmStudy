from sys import stdin

def matMul(m1, m2, size):
    a = []
    for _ in range(size):
        a.append([0]*size)
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                a[i][j] += m1[i][k] * m2[k][j]
            a[i][j] = a[i][j] % 1000
    return a


size, b = map(int, stdin.readline().split())
bbin = bin(b)[2:]
ans = []
arr = []
for i in range(size):
    ans.append([0]*size)
    ans[i][i] = 1

for _ in range(size):
    arr.append(list(map(int, stdin.readline().split())))

for s in bbin[::-1]:
    if s=='1':
        ans = matMul(ans, arr,size)
    arr= matMul(arr,arr, size)

for a in ans:
    for b in a:
        print(b, end=" ")
    print("")

