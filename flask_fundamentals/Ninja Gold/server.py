from flask import Flask, render_template, session, redirect, request
import random
import datetime
app = Flask(__name__)
app.secret_key= "Very_secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.datetime.now()
    place = request.form['place']
    places= {
        'farm': random.randint(10,20),
        'cave': random.randint(5,10),
        'house': random.randint(2,5),
        'casino': random.randint(-50,50)
    }
    
    current_gold = places[place]
    if not 'gold' in session:
        session['gold'] = current_gold
    else:
        session['gold'] += current_gold

    if current_gold>0:
        message = {
        'class': 'green',
        'content': 'You won {} golds at the {} on {}'.format(current_gold,place,now)

    }
    else:
        message = {
        'class': 'red',
        'content': 'You lost {} golds at the {} on {}'.format(current_gold,place,now)

    }
    if not 'activities' in session:
        session['activities'] = [message]
    else: 
        session['activities'].insert(0,message)
        session.modified = True

 

    





    return redirect('/')




app.run(debug=True)
