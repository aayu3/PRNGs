import time
import tkinter as tk
def binToString(binary):
    sections = int(len(binary)/7)
    ls = list(binary)
    new = []
    for i in range(sections):
        temp = ""
        for j in range(7):
            num = i*7+j
            temp =temp + ls[num]
        if temp == "0000000":
            break
        new.append(binToLetter(temp))
    return "".join(new)


def letterToBinary(char):
    num = ord(char)
    string = str(bin(num))[2:]
    if len(string) < 7:
        string = "0"*(7-len(string)) + string
    return string


def binToLetter(strnum):
    return chr(int(strnum,base=2))


def strToBin(string):
    print("Converting to Binary!")
    thing = list(string)
    halfconvert = thing
    nthing = []
    print("".join(halfconvert))
    for i in range(len(thing)):
        st = letterToBinary(thing[i])
        nthing.append(st)
        halfconvert[i] = st
        print("".join(halfconvert))
    return "".join(nthing)



def encrypt(p,q, message):
    n = p*q
    binstring = strToBin(message)
    blis = list(binstring)
    if len(blis) > n:
        print("The modulus is not big enough for this message")
        raise OverflowError
    else:
        for i in range(n-len(blis)):
            blis.append("0")
    xz = ((n//2)**2)%n
    xlis = [xz]
    for i in range(n):
        xlis.append((xlis[i]**2)%n)
    elis = []
    for i in range(n):
        elis.append(str((xlis[i]+int(blis[i]))%2))
    return [p,q,xlis[len(xlis)-1],"".join(elis)]



def qresidue(n,p):
    r1 = (n**((p+1)//4))%p
    r2 = p-r1
    if (r1**((p-1)//2))%p == 1:
        return r1
    else:
        return r2

def solveLinearReq(p,q):
    remainderls = []
    quotientls = []
    numls = []
    if p<q:
        numls = [q,p]
        a = q
        b = p
    else:
        numls = [p,q]
        a = p
        b = q
    rem = 1
    while rem !=0:
        rem = a - b*(a//b)
        quotientls.append(a//b)
        remainderls.append(rem)
        a = b
        b = rem
    remainderls.pop()
    s2 = 1
    t2 = 0
    s1 = 0
    t1 = 1
    for i in range(len(remainderls)):
        temps = s2-quotientls[i]*s1
        tempt = t2-quotientls[i]*t1
        s2 = s1
        t2 = t1
        s1 = temps
        t1 = tempt
    if p<q:
        return([t1,s1])
    else:
        return([s1,t1])

def isQR(n,p):
    if 1 == (n ** ((p + 1) // 4)) % p:
        return True
    else:
        return False


def genPrev(p,q,x,u,v):
    n = p*q
    xp = qresidue(x,p)
    xq = qresidue(x,q)
    xn1 = (xp*q*v+xq*p*u)%n
    return xn1




def decrypt(p,q,xno,estring):
    n= p*q
    templis = solveLinearReq(p,q)
    elis = list(estring)
    u = templis[0]
    v = templis[1]
    xrevlis = [xno]
    for i in range(n):
        xrevlis.append(genPrev(p,q,xrevlis[i],u,v))
    xlis = xrevlis[::-1]
    olis = []
    for i in range(n):
        olis.append(str((xlis[i]+int(elis[i]))%2))
    return binToString("".join(olis))


info = encrypt(31,23,"")
print(decrypt(info[0],info[1],info[2],info[3]))
