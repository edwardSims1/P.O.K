from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def genius():
        return '<h1>Welcome to Edwards website!</h1>'

@app.route('/about/')
def about():
        return '<h3>Born in the city of Detroit, Edward has been growing up loving to read! Since third grade the first thing after homework at home was reading! Formed from his love of reading, his dream is to leave a legacy behind like comic book creator Stan Lee did! Edward is 14 years old and now attends Detroit School of Arts!</h3>'


@app.route('/capitalize/<word>/')
def capitalize(word) :
        return '<h1>{}</h1>'.format(escape(word.capitalize()))


@app.route('/add/<int:n1>/<int:n2>/')
def add(n1,n2):
        return '<h1>{}</h1>'.format(n1+n2)

@app.route('/users/<int:user_id>/')
def greet_user (user_id):
        users = ['Bob', 'Jane', 'Adam'] 
        try:  
                return '<h2> Hi {}</h2>' . format(users[user_id])   
        
        except IndexError:
                abort(404)

@app.route('/myName/<first>/<middle>/<last>/')
def myName(first,middle,last):
        return '<h1>{}</h1>'.format(first +" "+ middle + " "+ last)

@app.route('/rep_yo_city/<City>/<State>')
def rep_yo_city(City, State):
        return '<h1>{}</h1>' .format(escape(City.capitalize()) +","+  " "+ escape(State.capitalize()) ) 
      
@app.route('/mult/<int:n1>/<int:n2>/')
def mult(n1,n2):
        return '<h1>{}</h1>' .format(n1*n2)

@app.route ('/sub/<int:n1>/<int:n2>/')
def sub(n1,n2):
        return '<h1>{}</h1>' .format(n1-n2)

@app.route ('/div/<int:n1>/<int:n2>/')
def div(n1,n2):
        return '<h1>{}</h1>' .format(n1/n2)

@app.route ('/mod/<int:n1>/<int:n2>/')
def mod(n1,n2):
        return '<h1>{}</h1>' .format(n1%n2)

@app.route('/geniuses/<int:geniuses_id>/')
def greet_geniuses(geniuses_id):
        geniuses =['Alvin Bryant','Boyd White IV','Craig Miller','Damonie Thomas',
'Derek Mitchell II','Edward Sims','Enansi Wooten','Isaiah Ingram','Isaiah Mcclendon',
'Jaden Henry','Jordan Conley','Matthew Johnson','Moriah Bishop','Noah Tyson',
'Prinzton Williams','Tahir Yufenu','Talib Yufenu','Tyler Windham','Wendell Smith','Zion Myers']
        try:
                 return '<h2> Hi ' +" "+ ' {}</h2>'.format(geniuses[geniuses_id])
        
        except IndexError:
                abort(404)
        

