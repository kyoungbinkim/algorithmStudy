
ans = [0] * 10
nstr = input()
num = int(nstr)
lenstr = len(nstr)
left,right = None, None

left = num//10
ans = [left] * 10
for i in range(1, num%10+1):
    ans[i] +=1
print("Start : ",ans)


for i in range(1,lenstr):
    ten = 10**i
    left = num//(ten*10)
    right = num%ten   
    n = (num//ten)%10
    print(left,n, right, ten)

    for j in range(10):
        ans[j]+= left * ten
    
    for j in range(n):
        ans[j] += ten
    ans[n] += right +1
    ans[0] -= ten
    # print(ans,"\n")

for i in range(9):
    print(ans[i], end=" ")
print(ans[9])

# print("429904664 541008121 540917467 540117067 533117017 473117011 429904664 429904664 429904664 429904664")
