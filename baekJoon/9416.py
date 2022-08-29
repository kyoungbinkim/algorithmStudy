from sys import stdin

ans = [1,1,1,2,2, 3, 4, 5, 7, 9]

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(len(ans), n):
        ans.append(ans[i-1]+ans[i-5])
    print(ans[n-1])

