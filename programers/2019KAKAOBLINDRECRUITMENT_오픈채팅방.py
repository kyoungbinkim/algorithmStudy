class user:
    def __init__(self, n,f):
        self.name = n
        self.flag = f
    
    def _changeName(self, _n):
        self.name = _n
        return True
        
    def _getName(self):
        return self.name
    
    def Join(self, _n:str):
        self.flag = True
        self.name = _n
        return True
    
    def isJoin(self):
        return self.flag
    
class handler(user):
    def __init__(self):
        self.uidToUser = {}
        return
        
    def getDict(self):
        return self.uidToUser
            
    
    def Enter(self, uid : str, n : str):
        
        if self.uidToUser.get(uid) == None:
            self.uidToUser.update({uid : user(n, True)})
        else:
            self.uidToUser.get(uid).Join(n)
            
    def Change(self, uid:str, n:str):
        self.uidToUser.get(uid)._changeName(n)
    
    def find(self, uid : str):
        return (self.uidToUser.get(uid) != None)
    
    def getName(self, uid:str):
        return self.uidToUser.get(uid)._getName()
    
    



def EnterUser(s):
    uid = s[:s.find(" ")]
    name = s[s.find(" ")+1 :]

uidToUser = {}
def solution(record):
    answer = []
    h = handler()
    cmd = {"Enter":0, "Leave":1 , "Change" : 2}
        
    
    for i in range(len(record)):
        c = record[i][:record[i].find(" ")]
        tmp = record[i][record[i].find(" ")+1 : ]
        
        if c=="Enter":
            uid = tmp[:tmp.find(" ")]
            name = tmp[tmp.find(" ")+1 : ]
            h.Enter(uid, name)
            
        
        elif c == "Leave":
            uid = tmp[tmp.find(" ")+1 : ]
            
        elif c == "Change":
            uid = tmp[:tmp.find(" ")]
            name = tmp[tmp.find(" ")+1 : ]
            h.Change(uid, name)
    
    
    for i in range(len(record)):
        c = record[i][:record[i].find(" ")]
        tmp = record[i][record[i].find(" ")+1 : ]
        if c == "Enter":
            uid = tmp[:tmp.find(" ")]
            name = tmp[tmp.find(" ")+1 : ]
            answer.append('{}님이 들어왔습니다.'.format(h.getName(uid)))
        elif c == "Leave":
            uid = tmp[tmp.find(" ")+1 : ]
            answer.append(("{}님이 나갔습니다.".format(h.getName(uid))))
             
    return answer