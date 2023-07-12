from sys import stdin

n, k = map(int, stdin.readline().split())
fishTank = [[int(x)] for x in stdin.readline().split()]

def firstStep(fishTank):
    low = min([min(x) for x in fishTank])

    for i in range(n):
        for j in range(len(fishTank[i])):
            if fishTank[i][j] == low:
                fishTank[i][j] += 1

def secondStep(fishTank):
    def split(arr):
        if len(arr) == n:
            return 1
        std = len(arr[0])
        for i in range(len(arr)):
            if len(arr[i]) != std:
                return i
    
    idx = split(fishTank)
    while True and idx != None:
        left = fishTank[:idx]
        right = fishTank[idx:]
        if len(left[0]) > len(right) or idx ==None:
            break

        
        left.reverse()
        for i in range(len(left[0])):
            right[i] = right[i] + [x[i] for x in left]
        
        fishTank = right
        idx = split(fishTank)
    return (left + right) if idx != None else fishTank

def thirdStrp(fishTank):
    ans = [[0 for _ in range(len(x))] for x in fishTank]

    for i in range(len(fishTank)):
        for j in range(len(fishTank[i])):
            if i < len(fishTank)-1 and len(fishTank[i+1]) > j:
                diff, rem = (fishTank[i][j] - fishTank[i+1][j]) // 5 , (fishTank[i][j] - fishTank[i+1][j]) % 5
                ansdiff = (diff if diff >= 0 or (rem == 0 and diff < 0) else diff +1 ) 
                ans[i][j] += ansdiff * -1
                ans[i+1][j] += ansdiff
            if j < len(fishTank[i])-1 :
                diff, rem = (fishTank[i][j] - fishTank[i][j+1]) // 5 , (fishTank[i][j] - fishTank[i][j+1]) % 5
                ansdiff = (diff if diff >= 0 or (rem == 0 and diff < 0) else diff +1 ) 
                ans[i][j] += ansdiff * -1
                ans[i][j+1] += ansdiff
    for i in range(len(fishTank)):
        fishTank[i] = [x+y for x,y in zip(fishTank[i], ans[i])]
    return fishTank

def fourthStep(fishTank):
    ans = []
    for f in fishTank:
        for x in f:
            ans.append([x])
    return ans

def fifthStep(fishTank):
    ans = []
    for i in range(len(fishTank) // 2):
        ans.append(fishTank[len(fishTank) // 2 + i] + fishTank[len(fishTank) // 2 - i - 1])
    ans2 = []
    for i in range(len(ans) // 2):
        ans[len(ans) // 2 - i - 1].reverse()
        ans2.append(ans[len(ans) // 2 + i] + ans[len(ans) // 2 - i - 1])
    return ans2

def check(fishTank):
    h = max([max(x) for x in fishTank])
    l = min([min(x) for x in fishTank])
    return h - l <= k

cnt = 0
while not check(fishTank):
    firstStep(fishTank)
    fishTank = secondStep(fishTank)
    fishTank = thirdStrp(fishTank)
    fishTank = fourthStep(fishTank)
    fishTank= fifthStep(fishTank)
    fishTank = thirdStrp(fishTank)
    fishTank = fourthStep(fishTank)
    cnt += 1
print(cnt)