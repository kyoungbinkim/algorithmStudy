import math

catalanList = []
while True:
    num = int(input())
    if num == 0:
        break
    
    n1 = math.factorial(num*2)
    n2 = math.factorial(num)
    print(int(n1//n2//n2)//(num+1))