from sys import stdin
import gc

def binarySearch(arr, tar):
    lo, hi = 0, len(arr)-1
    mid = (lo+hi) // 2
    while lo < hi:
        if arr[mid] == tar:
            break
        if arr[mid] < tar:
            if tar < arr[mid+1]:
                ans = arr[mid] if abs(arr[mid] - tar) < abs(arr[mid+1] - tar) else arr[mid+1]
                return ans
            lo = mid + 1
        else:
            if tar > arr[mid-1]:
                ans = arr[mid] if abs(arr[mid] - tar) < abs(arr[mid-1] - tar) else arr[mid-1]
                return ans
            hi = mid - 1
        mid = (lo+hi) // 2
    
    # print(arr, tar)
    # print(lo, hi, mid)
    # print()
    # print(arr[lo], arr[hi], arr[mid])

    ans = arr[lo] if abs(arr[lo] - tar) < abs(arr[hi] - tar) else arr[hi]
    # print(tar, ans)
    
    return ans



size = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
p = [x for x in arr if x>=0]
m = [x for x in arr if x<0 ]

del arr
gc.collect()

ans = []
if len(p) >= 2:
    ans = [p[0], p[1]]

if len(m) >= 2:
    if ans == []:
        ans = [m[len(m)-2], m[len(m)-1]]
    elif abs(sum(ans)) > abs(m[len(m)-2] + m[len(m)-1]):
        ans = [m[len(m)-2], m[len(m)-1]]
if ans == []:
    ans = [float("inf"), float("inf")]

for n in p:
    if len(m) == 0:
        break
    if sum(ans) == 0:
        break
    tmp = binarySearch(m, -n)
    # print(tmp,n)
    if abs(tmp+n) < abs(sum(ans)):
        ans = sorted([tmp, n])

for n in m:
    if len(p) == 0:
        break
    if sum(ans) == 0:
        break
    tmp = binarySearch(p, -n)
    # print(tmp, n)
    if abs(tmp+n) < abs(sum(ans)):
        ans = sorted([tmp, n])

print("{} {}".format(ans[0], ans[1]))