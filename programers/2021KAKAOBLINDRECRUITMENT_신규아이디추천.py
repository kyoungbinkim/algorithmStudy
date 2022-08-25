def round2(s):
    r = str('')
    for i in range(len(s)):
        if(s[i].isalpha() or s[i].isnumeric() or s[i] =='_' or s[i]=='-' or s[i] == '.'):
            r += s[i]
    return r

def round3(s):
    r = str('')
    for i in range(len(s)-1):
        if(s[i] == '.' and s[i+1] =='.'):
            continue
        else:
            r += s[i]
    r += s[len(s)-1]
    return r

def round4(s):
    r = str('')
    if s[0] != '.':
        r+= s[0]
    r+= s[1:len(s)-1]
    if s[len(s)-1] != '.':
        r+= s[len(s)-1]
    return r

def round5(s):
    if len(s)==0:
        return str('a')
    else:
        return s
    
def round6(s):
    if (len(s)>15):
        r = s[:15]
        if s[14] == '.':
            r = s[:14]
    else:
        r = s
    return r

def round7(s):
    r = s
    if len(r) <= 2:
        while len(r) <3:
            r +=s[len(s)-1]
    return r

def solution(new_id):
    print(0,new_id)
    new_id = new_id.lower()
    print(new_id)
    new_id = round2(new_id)
    print(new_id)
    new_id = round3(new_id)
    print(new_id)
    new_id = round4(new_id)
    print(new_id)
    new_id = round5(new_id)
    print(new_id)
    new_id = round6(new_id)
    print(new_id)
    new_id = round7(new_id)
    print(new_id)
    
    return new_id