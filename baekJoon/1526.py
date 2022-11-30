
a = int(input())
ans, ten = 1 , 10**5
ansTrue = 1
for i in range(1, a+1):
    ans = (ans * i) 
    ansTrue = ansTrue * i
    while (ans%10 == 0):
        ans = ans//10
    ans = ans % (ten*100) 
    print(i, ans%ten, ansTrue)

# 2 -> 15
# 3 -> 25 
# 4 -> 45



