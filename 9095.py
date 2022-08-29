
arr = [0,1,2,4,7,13,24,44]
for _ in range(int(input())):
    k = int(input())
    for i in range(len(arr), k+1):
        tmp = arr[i-1] + arr[i-2] + arr[i-3]
        arr.append(tmp)
    print(arr[k])

