import math
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib as mpl
from matplotlib.ticker import PercentFormatter
import numpy as np
import matplotlib.mlab as mlab
import LCGs
from MatrixMultiplication import Matrix
import os
#Lehmer Random Number Generators
#Form: X_n+1 = X_n * b mod q where q is a
#prime of power of a prime
#Advantages: Easy to implement
#Since q is prime or the power of a prime as long
#as we don't pick a stupid seed(X_0 value) or
#multiplier(b). None of the X_n will every be zero
'''
def isPrime(num):
  for i in range(2,int(math.sqrt(num))+1):
    if num%i == 0:
       return False
  return True
def totient(prime,power):
  return ((prime-1)*(prime**(power-1)))
'''
#Read a txt file that has a value every line
def readtxt(txtfile):
  with open(txtfile, 'r') as f:
    txt = [int(line.strip()) for line in f]
  return txt
#write to a txt file with a list
def writetxt(ls, txtfile):
  with open(txtfile, 'a') as the_file:
    for i in ls:
      the_file.write(str(i) + "\n")
#opens a file if it exists and returns a list of values, if it doesn't returns false
def checkfile(name):
  try:
    dat = readtxt(name)
    return dat
  except FileNotFoundError:
    return False

def str_to_intls(string):
  ls = []
  for i in string.split(","):
    ls.append(int(i))
  return ls

def str_to_matrix(string):
  ls = []
  nstr = string.split("\n")
  for i in range(len(nstr)):
    ls.append([])
    for j in nstr[i].split(" "):
      ls[i].append(j)
  return Matrix(ls)

def user_interface():
  types = LCGs.types
  print("LCGs:")
  for i in types:
    print(i)
  typeLCG = str(input("What type of LCG would you like to test: "))
  reqdic = LCGs.check_requirements(typeLCG)
  inputs = []
  directory = "/Users/aayu/PycharmProjects/PRNGs/" + typeLCG + "/" + typeLCG
  for key in reqdic:
    if key == "n":
      uinput = int(input("n(Will generate up to the nth random number): "))
      inputs.append(uinput)
    elif reqdic[key] == "int":
      uinput = int(input(key+": "))
      inputs.append(uinput)
      directory = directory + "(" + key + "=" + str(uinput) + ")"
    elif reqdic[key] == "list":
      uinput = str_to_intls(input(key+": "))
      inputs.append(uinput)
      directory = directory + "(" + key + "=" +str(uinput)+")"
    elif reqdic[key] == "matrix":
      uinput = str_to_matrix(input(key+"(separate items with spaces and separate lines with Shift+Enter):"))
      inputs.append(uinput)
      directory = directory + "(" + key + "=" + str(uinput) + ")"


  return[typeLCG,inputs,directory]






def modLCG(info,mod):
  lcg = info[0]
  reqs = info[1]
  directory = info[2]
  n = reqs[len(reqs) - 1]
  if not checkfile(directory+".txt"):
    getattr(LCGs,lcg)(reqs)
  else:
    ls = readtxt(directory+".txt")
    if n>len(ls):
      getattr(LCGs, lcg)(reqs)
  if not checkfile(directory + " (results modded by="+str(mod)+").txt"):
    ls = readtxt(directory+".txt")
    results = []
    for i in range(n):
      results.append((int(ls[i])%mod))
    writetxt(results,directory + " (results modded by="+str(mod)+").txt")
    return results
  else:
    ls = readtxt(directory+".txt")
    old = readtxt(directory + " (results modded by="+str(mod)+").txt")
    extension = []
    for i in range(len(old),n):
      extension.append(int(ls[i])%mod)
    writetxt(extension,directory + " (results modded by="+str(mod)+").txt")
    return old + extension



def plotLCG(info,mod):
  lcg = info[0]
  reqs = info[1]
  directory = info[2]
  data = modLCG(info,mod)
  fig, ax = plt.subplots(facecolor='#37474e')
  ax.set_facecolor('#37474e')
  ax.tick_params(labelcolor='white')
  ax.spines['bottom'].set_color('white')
  ax.spines['top'].set_color('white')
  ax.spines['left'].set_color('white')
  ax.spines['right'].set_color('white')
  plt.hist(data,bins=mod,color='#ffffff')
  plt.xlabel("Value Generated by " + lcg,color='#ffffff')
  plt.ylabel("Frequency",color='#ffffff')
  for t in ax.xaxis.get_ticklines(): t.set_color('white')
  for t in ax.yaxis.get_ticklines(): t.set_color('white')
  plt.title("Frequencies of " +str(reqs[len(reqs)-1])+ " Random Numbers Generated using " + lcg,color='#ffffff')
  plt.savefig(directory+" (Generated up to "+str(reqs[len(reqs)-1])  + "th random number) Histogram")
  plt.show()

def testLCG():
  info = user_interface()
  plotLCG(info,256)
  for i in range(10):
    plotLCG(info,(i+1)*10)

testLCG()
#37474e



'''
num_bins = mod
# the histogram of the data
plt.hist(period, bins=mod)


# add a 'best fit' line
plt.plot()
plt.xlabel('Residue')
plt.ylabel('Frequency')
plt.title('Histogram of Fibonnaci Numbers mod '+str(mod))
 '''

# Tweak spacing to prevent clipping of ylabel
'''
plt.subplots_adjust(left=0.15)
plt.show()
plt.savefig('foo' + str(mod) + '.png')
'''
'''
plt.plot(period)
plt.ylabel('Fi🅱onacci Numbers mod 100')
plt.show()
plt.savefig('foo.png')
'''