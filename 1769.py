num = input()
step = 0
while int(num) >= 10:
    step += 1
    num = str(sum(list(map(int, num))))
print(step)
if int(num) % 3 ==0:
    print("YES")
else:
    print("NO")
