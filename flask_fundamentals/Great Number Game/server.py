from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "Secret_key"

@app.route("/")
def index():
    if "correct" not in session:
        session["correct"] = random.randint(0,101)
    if "result" not in session:
        result="no guess"
    else:
        result=session["result"]
    return render_template("index.html", result=result)
@app.route("/guess", methods=["POST"])
def guess():
    guess = int(request.form["guess"])
    correct = session["correct"]
    if guess> correct:
        session["result"] = "high"
    elif guess< correct:
        session["result"] = "low"
    else:
        session["result"] = "correct"

    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    session['result'] = random.randint(0, 101)
   
    return redirect("/")
    



app.run(debug = True)