### imports
import random


### functions

def askForSize():
    done = True
    while done == True:
        wSstr = input("what s?  ")
        try:
            wS = int(wSstr)
            s = wS
            done = False
        except:
            print("Try again")
    return s

def generateList(s):
    l = []
    for i in range(0, s):
        l.append(i)
    return l

def randomizeList(l):
    fl = l.copy()
    l = []
    length = len(fl)
    for i in range(0, length):
        r = random.randint(0, len(fl))
        l.append(fl[r-1])
        fl.pop(r-1)
    return l

def findFactor(l):
    f = int(len(l)/2+0.5)
    # i = True
    # while i:
    #     if (len(l)) > 2*f:
    #         f = f+1
    #     else:
    #         i = False
    return f

def allFunctions():
    s = askForSize()
    l = generateList(s)  
    l = randomizeList(l)
    f = findFactor(l)
    return l, f

### testing