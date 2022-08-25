size = int(input())
scores = list(map(int, input().split()))
m = max(scores)
refacor = [x/m*100 for x in scores]
print(sum(refacor)/size)