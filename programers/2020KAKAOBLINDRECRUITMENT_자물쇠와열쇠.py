import numpy as np

def pad(img, size):
    wid = img.shape[0]
    r = np.zeros((wid+size*2-2, wid+size*2-2), dtype=int)
    r[size-1 : size+wid-1, size-1 : size+wid-1] = img
    print(r, r.shape, wid)
    print(r[size-1 : size+wid-1, size-1 : size+wid-1].shape , img.shape)
    return r
    
def rotate(img):
    return np.rot90(img)

def mySum(img):
    S = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] >= 2:
                return -1
            else:
                S += img[i,j]
    return S

def check(pad, img, key):
    n = img.shape[0]
    m = key.shape[0]
    
    
    for i in range(m+n-1):
        for j in range(m+n-1):
            tmp = pad.copy()
            tmp[i:i+m, j:j+m] += key
            
            # print(tmp[m-1 : m+n-1, m-1:m+n-1], mySum(tmp[m-1 : m+n-1, m-1:m+n-1]))
            if mySum(tmp[m-1 : m+n-1, m-1:m+n-1]) == img.size:
                # print(tmp, i,j)
                return True
    return False
             
    
def solution(key, lock):
    k = np.array(key)
    l = np.array(lock)
    
    padimg = pad(l, k.shape[0])
    for _ in range(4):
        # print(k)
        if check(padimg, l, k):
            return True
        k = rotate(k)
    return False