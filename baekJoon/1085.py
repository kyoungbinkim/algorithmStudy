
p = list(map(int, input().split()))
print(min([p[0], p[1], p[2]-p[0], p[3]-p[1]]))