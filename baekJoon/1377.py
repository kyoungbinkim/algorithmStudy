from sys import stdin

def isSorted(arr,size):
    for i in range(size-1):
        if arr[i] > arr[i+1]:
            return False
    return True

ans = []
size = int(stdin.readline())
for _ in range(size):
    ans.append(int(stdin.readline()))


ret = 0

while len(ans) > 1:
    while True:
        if ans[len(ans)-1] > ans[len(ans)-2]:
            ans.pop()
        else:
            break
    
    ans.remove(max(ans))
    ret+=1
print(ret)