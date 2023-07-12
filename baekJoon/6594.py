from sys import stdin

def parseString(str):
    ret = []
    tmp = 0
    for i in range(len(str)):  
        if str[i].isdigit():
            tmp *= 10
            tmp += int(str[i]) 
            # print(tmp)
        else:
            if tmp != 0:

                ret.append(tmp)
            ret.append(str[i])
            tmp = 0
    return ret

while True:
    try:
        str = stdin.readline().replace('\n', '')
        if str == '':
            break
        str = str.split('=')
        
        str[0] = parseString(str[0])
        str[1] = parseString(str[1])





    except:
        break


