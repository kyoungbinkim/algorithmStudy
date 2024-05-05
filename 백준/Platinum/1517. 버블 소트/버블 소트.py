from sys import stdin
        
def cntSwap(nums1, nums2):
    swap = []
    cnt = 0
    i = len(nums1) - 1
    j = len(nums2) - 1  

    while i >= 0 and j >= 0:
        # print(i,j, swap, nums1[i], nums2[j])

        if nums1[i] == nums2[j]:
            while j >= 1 and nums2[j] == nums2[j-1]:
                swap.append(nums2[j])
                j -= 1
            swap.append(nums1[i])
            swap.append(nums2[j])
            cnt += j
            i -= 1
            j -= 1
            
        elif nums1[i] > nums2[j]:
            swap.append(nums1[i])
            i -= 1
            cnt += (j+1)
            
        else:
            swap.append(nums2[j])
            j -= 1
            
    swap.reverse()
    if i>=0:
        swap = nums1[:i+1] + swap
    elif j>=0:
        swap = nums2[:j+1] + swap
    return swap, cnt

# print(cntSwap([1,3,4,8], [1,2,3,4]))

n = int(stdin.readline())
nums = list(map(lambda x: [int(x)], stdin.readline().split()))
# print(nums)

ANS = 0

while len(nums) > 1:
    nxt = []

    for i in range(0, len(nums), 2):
        if i+1 == len(nums):
            nxt.append(nums[i])
            continue
        swap, cnt = cntSwap(nums[i], nums[i+1])
        ANS += cnt
        nxt.append(swap)
    
    nums = nxt
    # print(nums, ANS)
print(ANS)
