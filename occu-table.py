from flask import Flask, render_template

app = Flask(__name__)

occ = open("occu-table.csv","r")
ZeList = []
occ.next()
for row in occ:
        ZeList.append(row)
occDict = {}
for i in ZeList:
    d = i.rfind(",")
    occDict[i[0:d]] = float(i[d+1:len(i)])
del occDict['Total']

def randOcc():
    from random import randint
    p = randint(0,1000)
    t = 0
    for key in occDict:
        t += occDict[key]
        if (t * 10) >= p:
            return key

@app.route('/')
def what():
     return "goteeeeeeeeee"

@app.route('/occupations')
def occ():
    return render_template('occu-table.html') #, tab = occDict, ran = randOcc())

if __name__ == '__main__':
    app.debug = True
    app.run()
 
