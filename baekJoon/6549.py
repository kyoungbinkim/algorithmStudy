from sys import stdin

while True:
    numList = list(map(int, stdin.readline().split()))
    if numList[0] == 0:
        break
    ans = 0

    for pivot in range(1, numList[0]+1):
        start, end = pivot , pivot
        while start > 1:
            start -= 1
            if numList[start] < numList[pivot]:
                start += 1
                break
        while end < numList[0]:
            end += 1
            if numList[end] < numList[pivot]:
                end -= 1
                break
        
        tmp = numList[pivot] * (end - start  + 1) 
        # print(pivot, start, end,  '\t', numList[pivot], tmp)
        ans = tmp if tmp > ans else ans
    print(ans)
        
        

