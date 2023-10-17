
def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result

n,r = map(int, input().split())
ans = permutation(list(range(1, n+1)), r)

for l in ans:
    print(" ".join([str(c) for c in l]))