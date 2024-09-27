import random

keycode = random.randint(9,96)

def isCoprime(x):
    if x<1:
        return False
    if x<4 and x>1:
        return True
    if x==5:
        return True
    if x==7:
        return True
    if x==11:
        return True
    if x==13:
        return True
    if x==17:
        return True
    if x==19:
        return True
    else:
        return False

def getPQ():
    while True:
        p = random.randint(2, 20)
        q = random.randint(2, 20)
        if isCoprime(p) and isCoprime(q) and p!=q:
            return p, q

def getFunctionN(p,q):
    n = p*q
    Fn = (p-1)*(q-1)
    return n, Fn

def getED(Fn):
    while True:
        e = random.randint(2, 19)
        for i in range(1000):
            if e*i % Fn == 1:
                return i,e

def getKeyWord(x):
    key = []
    for char in x:
        char = ord(char) - keycode
        # if char < 150:
        key.append(char)
    return key

def getY(x,e,n):
    Y = []
    for xi in x:
        y = pow(xi,e) % n
        Y.append(y)
    return Y

def getValueWord(key):
    val = []
    for k in key:
        if k<1000:
            v = chr(k+keycode)
        else:
            v = ord(k+keycode)
        val.append(v)
    return val

def getX(y,d,n):
    X = []
    for yi in y:
        x = pow(yi,d) % n
        X.append(x)
    return X


if __name__== '__main__':
    p, q = getPQ()
    n, Fn = getFunctionN(p, q)
    d,e = getED(Fn)
    user_input = input("请输入key：")
    f = getKeyWord(user_input)
    print('字符码：{}'.format(f))
    y = getY(f,e,n)
    print('加密：{}'.format(y))
    x = getX(y,d,n)
    print('解密：{}'.format(x))
    val = getValueWord(x)
    print('明文：{}'.format(val))
    print('p:{} q:{} n:{} fn:{} d:{} e:{}'.format(p,q,n,Fn,d,e))
