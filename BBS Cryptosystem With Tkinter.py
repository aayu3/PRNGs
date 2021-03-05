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



def encrypt():
    global encodedmessage
    global e3
    global binarymessage
    global xn
    p = int(e1.get())
    q = int(e2.get())
    message = e3.get()
    binarymessage.config(text=str(message))
    n = p*q
    binstring = strToBin(message)
    blis = list(binstring)
    if len(blis) > n:
        global errormessage
        errormessage.grid(row=3,column=0)
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
    encodedmessage.config(text="".join(elis))
    encodedmessage.grid(row=6,column=1)
    print("".join(elis))
    e3.delete(0, 'end')
    xn.config(text=str(xlis[len(xlis)-1]))
    xn.grid(row=7,column=1)
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




def decrypt():
    global decryptedmessage
    p = int(bp1.get())
    q = int(bp2.get())
    xno = int(key.get())
    estring = str(emessage.get())
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

    message= binToString("".join(olis))
    decryptedmessage.config(text=message)
    decryptedmessage.grid(row=15,column=1)
    return message


root = tk.Tk()
tk.Label(root,text="Encrypt").grid(row=0,column=0)
tk.Label(root,
         text="Blum Prime 1").grid(row=1,column=0)
tk.Label(root,
         text="Blum Prime 2").grid(row=1,column=3)
tk.Label(root,
         text="Message").grid(row=2,column=0)
errormessage = tk.Label(root,text="The Modulus is Not Big Enough for the Message")
binarymessage = tk.Label(root,text="")
encodedmessage = tk.Message(root,text="")
encodedmessagelabel = tk.Label(root,text="Encoded Message:")
encodedmessagelabel.grid(row=6,column=0)
binarymessagelabel = tk.Label(root,text="Message:")
binarymessagelabel.grid(row=4,column=0)
xnlabel = tk.Label(root,text="Key Value:")
xn = tk.Message(root,text="")
xnlabel.grid(row=7,column=0)
errormessage.grid_remove()
binarymessage.grid_remove()

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e1.grid(row=1, column=1)
e2.grid(row=1, column=4)
e3.grid(row=2,column=1)
encryptbutton = tk.Button(root,
          text='Encrypt',
          command=encrypt,fg='black')
encryptbutton.grid(row=8,column=0,sticky=tk.W,pady=4)
showhide = tk.IntVar()
showhide.set(2)  # initializing the choice, i.e. Python

onoff = [
    ("Show",1),
    ("Hide",2)
]

def ShowHide():
    if int(showhide.get()) == 1:
        binarymessage.grid_remove()
    else:
        binarymessage.grid(row=4, column=1)


tk.Label(root,
         text="""Toggle Showing the Original Message""",
         justify = tk.LEFT,
         padx = 20).grid(row=9)

for val, mode in enumerate(onoff):
    tk.Radiobutton(root,
                  text=mode,
                  padx = 20,
                  variable=showhide,
                    indicatoron = 0,
                  command=ShowHide,
                  value=val).grid(row=10,column=val)

tk.Label(root,text="Decrypt").grid(row=11,column=0)
tk.Label(root,
         text="Blum Prime 1").grid(row=12,column=0)
tk.Label(root,
         text="Blum Prime 2").grid(row=12,column=3)
tk.Label(root,text="Key").grid(row=13,column=0)
tk.Label(root,text="Encoded Message").grid(row=13,column=3)
bp1 = tk.Entry(root)
bp2 = tk.Entry(root)
key = tk.Entry(root)
emessage = tk.Entry(root)
bp1.grid(row=12, column=1)
bp2.grid(row=12, column=4)
key.grid(row=13,column=1)
emessage.grid(row=13,column=4)
decryptbutton = tk.Button(root,
          text='Decrypt',
          command=decrypt,fg='black')
decryptbutton.grid(row=14,column=0,sticky=tk.W,pady=4)
tk.Label(root,text="Decoded Message:").grid(row=15,column=0)
decryptedmessage = tk.Message(root,text="")
tk.Button(root,
                   text="QUIT",
                   fg="red",
                   command=root.quit).grid(row=16,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
root.mainloop()
