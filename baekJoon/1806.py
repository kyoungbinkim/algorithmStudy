from sys import stdin

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arrSum = [0]
for i in range(n):
    arrSum.append(arrSum[i] + arr[i])

if arrSum[n] < s:
    print(0)
else:
    f = False
    for i in range(1,n+1):
        for j in range(0, n+1-i):
            if arrSum[j+i] - arrSum[j] >= s:
                print(i)
                f = True
                break
        if f:
            break

