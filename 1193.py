num = int(input())

i = 0
Sum = 0
while Sum < num:
    i+=1
    Sum += i
up = num-(Sum-i)
down = i+1 - up
if i %2 ==0:
    print("{}/{}".format(up, down))
else:
    print("{}/{}".format(down, up))