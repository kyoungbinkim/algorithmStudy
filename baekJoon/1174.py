n = int(input())

arr = []
for _ in range(10):
    arr.append(0)
arr[0] = 1

def next(arr):
    for i in range(len(arr)-1):
        if sum(arr) > sum(range(10)):
            return False
        if arr[i+1]-arr[i] == 1:
            continue
        if arr[i]+1 < arr[i+1]:
            arr[i]+= 1
            for k in range(i):
                arr[k]= k
            return True
        elif arr[i]+1 == arr[i+1] and arr[i+1] != 9:
            arr[i+1]+=1
            for k in range(i+1):
                arr[k]= k
            return True
        # print(arr[i], arr[i+1])
        elif arr[i] == 9 and arr[i+1] == 0:
            for k in range(i+2):
                arr[k]= k
            return True
        elif arr[i+1] == 0 and arr[i] != 0:
            arr[i]+=1
            for k in range(i):
                arr[k]= k
            return True

if n > 1023:
    print(-1)
elif n == 1:
    print(0)
else:
    for i in range(2,n):
        flag= next(arr)
        # print(arr)
        # if (i+1) % 10 ==0:
        #     print(i)
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * (10**i)
    print(ans)


