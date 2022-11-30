from sys import stdin

size= int(stdin.readline()) + 1
arr = [0] + list(map(int, stdin.readline().split()))
dInd, dVal = [0], [-1000000001]

for i in range(1,size):
    val = arr[i]

    if dVal[len(dVal)-1] < val:
        dVal.append(val)
        dInd.append(len(dVal)-1)
    else:
        lo,hi = 0, len(dVal)-1
        mid = (lo+hi) //2
        while lo <= hi:
            if val > dVal[mid]:
                lo = mid+1
            else:
                hi = mid-1
            mid = (lo+hi) //2
        dVal[lo] = val
        dInd.append(lo)

# print(dInd)
# print(dVal)
ind =len(dVal)-1
print(ind)


dInd.reverse()
arr.reverse()

ans = []
for i in range(0,len(dInd)-1):
    if ind == dInd[i]:
        ans.append(arr[i])
        ind -= 1
ans.reverse()

for i in range(len(ans)-1):
    print(ans[i], end=" ")
print(ans[len(ans)-1])
