from flask import Flask, render_template
from utils import occupations

app = Flask(__name__)

@app.route('/')
def what():
     return "goteeeeeeeeee"

@app.route('/occupations')
def occ():
    return render_template('occu-table.html', tab = occupations.tab(), ran = occupations.randOcc())

if __name__ == '__main__':
    app.debug = True
    app.run()
 
