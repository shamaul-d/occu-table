def tab():
    occ = open("data/occu-table.csv","r")
    ZeList = []
    occ.next()
    for row in occ:
        ZeList.append(row)
    occDict = {}
    for i in ZeList:
        d = i.rfind(",")
        occDict[i[0:d]] = float(i[d+1:len(i)])
    del occDict['Total']
    return occDict

def randOcc():
    from random import randint
    p = randint(0,1000)
    t = 0
    l = tab()
    for key in l:
        t += l[key]
        if (t * 10) >= p:
            return key
