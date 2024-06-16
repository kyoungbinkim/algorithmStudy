from sys import stdin

p = 1000000007
n = int(stdin.readline())

ans = 0
twosqare = [1]
for i in range(n):
    twosqare.append(twosqare[i] * 2 % p)
arr = list(map(int, stdin.readline().split()))
arr.sort()
# print(arr, twosqare)

for i in range(n-1):
    for j in range(i+1, n):
        # ans += ((arr[j]- arr[i]) * twosqare[j-i-1]) % p
        ans = (ans + (arr[j]- arr[i]) * twosqare[j-i-1] % p) % p
print(ans % p)
