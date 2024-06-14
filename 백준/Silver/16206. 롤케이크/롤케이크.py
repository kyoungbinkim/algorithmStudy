from sys import stdin
n,m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
nums.sort(key=lambda x:(x%10, x))
ans = 0
for num in nums:
    if m <= 0 and num > 10:
        break
    if  num == 10:
        ans += 1
        continue
    if num < 10:
        continue
    while m and num > 10:
        m -= 1
        num -= 10
        ans += 1
    if num == 10:
        ans += 1
print(ans)