### trash variables

l = [0,1,2,3,4,5,6,7,8,9,10,11]

f = 6
### imports

import setup

### functions

def printWholeBracket(l,f):
    for i in range(f):
        i = i*2
        try:
            c = (str(l[i]), str(l[i+1]))
        except:
            c = (str(l[i]), "")
        print("[%s][%s]" % c)
    

def gameLoop(l,f):
    fl = []
    
    for i in range(f):
        pc = False
        i = i*2
        try:
            c = (str(l[i]), str(l[i+1]))
        except:
            c = (str(l[i]), "" )
            p = str(l[i])
            pc = True
        print("[%s][%s]" % c)
        done = True        
        while done and pc == False:
            wPstr = input("what player?  ")
            try:
                wP = int(wPstr)
                p = wP
                p = str(p)
                if c.count(p) >= 1:
                    break
                else:
                    print("Try again")
            except:
                print("Try again")
        print("Winner is %s!"% p)
        fl.append(int(p))
    l = fl.copy()
    return l
            
def game(l,f):
    game = True
    while game:
        printWholeBracket(l,f)
        print("--------")
        l = gameLoop(l,f)
        print("--------")
        f = setup.findFactor(l)
        if len(l) == 1:
            break