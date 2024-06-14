from sys import stdin

nums = list(map(int, stdin.readline().split()))
# 5
ans = nums[4]

# 4
ans += nums[3]
nums[0] -= nums[3]

# 3,2
ans += min(nums[2], nums[1])
tmp = min(nums[2], nums[1])
nums[2] -= tmp
nums[1] -= tmp


if nums[2] > 0:
    ans += nums[2]
    nums[0] -= nums[2]*2
    nums[2] = 0


if nums[1] > 0:
    ans += nums[1]//2 + (1 if nums[1]%2 != 0 else 0)
    nums[0] -= nums[1]//2 + (1 if nums[1]%2 != 0 else 0)*3 

if nums[0] > 0:
    ans += nums[0]//5 + (1 if nums[0]%5 != 0 else 0)

print(ans)