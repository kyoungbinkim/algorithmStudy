def calcPercent(arr):
    avg = sum(arr[1:])/arr[0]
    num = 0
    for i in range(1, len(arr)):
        if arr[i] > avg:
            num += 1
    return round(num/arr[0] * 100, 3)

inputSize = int(input())
inputArr = []
for _ in range(inputSize):
    tmp = []
    for i in input().split():
        tmp.append(int(i))
    inputArr.append(tmp)

for l in inputArr:
    print('{:.3f}%'.format(calcPercent(l)))
