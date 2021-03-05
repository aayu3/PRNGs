#File Managing
# Read a txt file that has a value every line
def readtxt(txtfile):
    with open(txtfile, 'r') as f:
        txt = [int(line.strip()) for line in f]
    return txt
# write to a txt file with a list

def writetxt(ls, txtfile):
    with open(txtfile, 'a') as the_file:
        for i in ls:
            the_file.write(str(i) + "\n")
# opens a file if it exists and returns a
# list of values, if it doesn't returns false

def checkfile(name):
    try:
        dat = readtxt(name)
        return dat
    except FileNotFoundError:
        return False

#list to str
def str_to_ls(string):
    string = string.strip("[")
    string = string.strip("]")
    ls = []
    for i in string.split(", "):
        ls.append(int(i))
    return ls


# read a txt file that stores 1D matrices
def mreadtxt(txtfile):
    with open(txtfile, 'r') as f:
        txt = [str_to_ls()]


types = ["RANDU", "SRG", "ALFG", "AWCLFG", "SLFG", "MLFG"]

def check_requirements(lcg):
    return globals()[lcg+"_requirements"]()







def RANDU_requirements():
    return {"seed":"int","n":"int"}

def SRG_requirements():
    return {"seed":"matrix","linear function":"matrix","n":"int"}

def ALFG_requirements():
    return {"seeds":"list","j":"int","k":"int","mod":"int","n":"int"}

def AWCLFG_requirements():
    return {"seeds":"list","j":"int","k":"int","mod":"int","n":"int"}

def SLFG_requirements():
    return {"seeds":"list","j":"int","k":"int","mod":"int","n":"int"}

def MLFG_requirements():
    return {"seeds":"list","j":"int","k":"int","mod":"int","n":"int"}

#Congruential Generator

#Bad early LCG that was widely used, as we can see for
# an odd seed it will only generate odd numbers and for
# an even seed it will eventually terminate

def RANDU(ls):
    seed = ls[0]
    n = ls[1]
    if not checkfile("/Users/aayu/PycharmProjects/PRNGs/RANDU/RANDU(seed=" + str(seed) + ").txt"):
        ls = [seed]
        for i in range(n):
            ls.append((65539 * int(ls[i])) % 2147483648)
        writetxt(ls, "/Users/aayu/PycharmProjects/PRNGs/RANDU/RANDU(seed=" + str(seed) + ").txt")
        return ls[n]
    else:
        ls = readtxt("/Users/aayu/PycharmProjects/PRNGs/RANDU/RANDU(seed=" + str(seed) + ").txt")
        length = len(ls)
        newls = [ls[length - 1]]
        if n < length:
            return ls[n]
        else:
            for i in range(length - 1, n):
                newls.append((65539 * int(newls[i - length + 1])) % 2147483648)
            writetxt(newls[1:], "/Users/aayu/PycharmProjects/PRNGs/RANDU/RANDU(seed=" + str(seed) + ").txt")
            return newls[len(newls) - 1]

#Shift-Register Generator

#Basic Shift-Register Generator
'''
def SRG(ls):
    seedmatrix = ls[0]
    func = ls[1]
    n = ls[2]
    if not checkfile("/Users/aayu/PycharmProjects/PRNGs/SRG/SRG(seed=" + str(seedmatrix) + ")(linear function="+str(func)+ ").txt"):
'''

#Lagged Fibonacci Generators
#Also called lagged two bit generators
#Each term of the sequence is based on two previous
# terms hence the lagged part from the previous terms
#and the two bit part from the two previous terms
#In general fibonacci generators use one of 4 binary operations
#+,-,x, and xor these are commercial Random Number Generators and
# are good because they can be computed relatively quickly

#Additive Lagged Fibonnaci Generator

def ALFG(ls):
    seeds = ls[0]
    j = ls[1]
    k = ls[2]
    mod = ls[3]
    n = ls[4]
    if not checkfile("/Users/aayu/PycharmProjects/PRNGs/ALFG/ALFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt"):
        ls = seeds[0:]
        for i in range(len(seeds),n+1):
            e_j = ls[i-j]
            e_k = ls[i-k]
            ls.append((e_j+e_k)%mod)
        writetxt(ls, "/Users/aayu/PycharmProjects/PRNGs/ALFG/ALFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        return ls[n]
    else:
        ls = readtxt("/Users/aayu/PycharmProjects/PRNGs/ALFG/ALFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        length = len(ls)
        if n < length:
            return ls[n]
        else:
            newls = ls[length - len(seeds):]
            for i in range(len(seeds),n+1-length+len(seeds)):
                e_j = newls[i-j]
                e_k = newls[i-k]
                newls.append((e_j+e_k)%mod)
            writetxt(newls[len(seeds):], "/Users/aayu/PycharmProjects/PRNGs/ALFG/ALFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
            return newls[len(newls)-1]

#Blum Blum Shub Generator



#Addition With Carry Lagged Fibonnaci Generator

def AWCLFG(ls):
    seeds = ls[0]
    j = ls[1]
    k = ls[2]
    mod = ls[3]
    n = ls[4]
    if not checkfile("/Users/aayu/PycharmProjects/PRNGs/AWCLFG/AWCLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt"):
        ls = seeds[0:]
        bit = 0
        for i in range(len(seeds),n+1):
            e_j = ls[i-j]
            e_k = ls[i-k]
            ls.append((e_j+e_k+bit)%mod)
            if e_j + e_k + bit > mod:
                bit = 1
            else:
                bit = 0
        writetxt(ls, "/Users/aayu/PycharmProjects/PRNGs/AWCLFG/AWCLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        return ls[n]
    else:
        ls = readtxt("/Users/aayu/PycharmProjects/PRNGs/AWCLFG/AWCLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        length = len(ls)
        if n < length:
            return ls[n]
        else:
            newls = ls[length - len(seeds):]
            bit = 0
            for i in range(len(seeds),n+1-length+len(seeds)):
                e_j = newls[i-j]
                e_k = newls[i-k]
                newls.append((e_j+e_k+bit)%mod)
                if e_j + e_k + bit > mod:
                    bit = 1
                else:
                    bit = 0
            writetxt(newls[len(seeds):], "/Users/aayu/PycharmProjects/PRNGs/AWCLFG/AWCLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
            return newls[len(newls)-1]
        
#Subractive Lagged Fibonnaci Generator

def SLFG(ls):
    seeds = ls[0]
    j = ls[1]
    k = ls[2]
    mod = ls[3]
    n = ls[4]
    if not checkfile("/Users/aayu/PycharmProjects/PRNGs/SLFG/SLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt"):
        ls = seeds[0:]
        for i in range(len(seeds),n+1):
            e_j = ls[i-j]
            e_k = ls[i-k]
            ls.append((e_j-e_k)%mod)
        writetxt(ls, "/Users/aayu/PycharmProjects/PRNGs/SLFG/SLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        return ls[n]
    else:
        ls = readtxt("/Users/aayu/PycharmProjects/PRNGs/SLFG/SLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        length = len(ls)
        if n < length:
            return ls[n]
        else:
            newls = ls[length - len(seeds):]
            for i in range(len(seeds),n+1-length+len(seeds)):
                e_j = newls[i-j]
                e_k = newls[i-k]
                newls.append((e_j-e_k)%mod)
            writetxt(newls[len(seeds):], "/Users/aayu/PycharmProjects/PRNGs/SLFG/SLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
            return newls[len(newls)-1]

#Multiplicative Lagged Fibonnaci Generator

def MLFG(ls):
    seeds = ls[0]
    j = ls[1]
    k = ls[2]
    mod = ls[3]
    n = ls[4]
    if not checkfile("/Users/aayu/PycharmProjects/PRNGs/MLFG/MLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt"):
        ls = seeds[0:]
        for i in range(len(seeds),n+1):
            e_j = ls[i-j]
            e_k = ls[i-k]
            ls.append((e_j*e_k)%mod)
        writetxt(ls, "/Users/aayu/PycharmProjects/PRNGs/MLFG/MLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        return ls[n]
    else:
        ls = readtxt("/Users/aayu/PycharmProjects/PRNGs/MLFG/MLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
        length = len(ls)
        if n < length:
            return ls[n]
        else:
            newls = ls[length - len(seeds):]
            for i in range(len(seeds),n+1-length+len(seeds)):
                e_j = newls[i-j]
                e_k = newls[i-k]
                newls.append((e_j*e_k)%mod)
            writetxt(newls[len(seeds):], "/Users/aayu/PycharmProjects/PRNGs/MLFG/MLFG(seeds=" + str(seeds)+")(j="+str(j)+")(k="+str(k)+")(mod="+str(mod) + ").txt")
            return newls[len(newls)-1]

#XOR Lagged Fibonnaci Generator



#Multiply-With-Carry Generator for generating sequences
# of random integers based on an initial set from two to
# many thousands of randomly chosen seed values. The main
# advantages of the MWC method are that it invokes simple
# computer integer arithmetic and leads to very fast
# generation of sequences of random numbers with immense
# periods, ranging from around 260 to 22000000.
#def MCW(seed,n):