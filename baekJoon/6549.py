from sys import stdin

# get keyList index
def binarySearch(numlist, tar, start, end):
    mid = (start+end) // 2
    if numlist[mid] == tar:
        return mid
    elif numlist[mid] > tar:
        return binarySearch(numlist, tar, start, mid-1)
    else:
        return binarySearch(numlist, tar, mid+1, end)


if __name__ == '__main__':
    while True:
        numlist = list(map(int, stdin.readline().split()))
        if numlist[0] == 0:
            break
        keyList = list(set(numlist[1:]))
        keyList.sort()
        keyListLen = keyList.__len__()
        # print("\nkeylen : ",keyListLen, keyList)
        tmp = {} # key : length
        ans = {} # key : length
        for key in keyList:
            ans.update({key : 0})
            tmp.update({key : 0})
        
        for i in range(1, numlist[0]+1):
            ind = binarySearch(keyList, numlist[i], 0, keyListLen)
            # print(ind, numlist[i])
            for j in range(ind+1):
                tmp[keyList[j]] += 1
            for j in range(ind+1, keyListLen):
                ans[keyList[j]] = tmp[keyList[j]]  if tmp[keyList[j]] > ans[keyList[j]] else ans[keyList[j]]
                tmp[keyList[j]] = 0
        for k in keyList:
            if tmp[k] > ans[k]:
                ans[k] = tmp[k]
        
        ansVal = 0
        for k in keyList:
            tmp = k * ans[k]
            if tmp > ansVal:
                ansVal = tmp
        print(ansVal)    
        