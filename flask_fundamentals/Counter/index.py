from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "VerySecret"

@app.route("/")
def index():
    if "count" in session.keys():
        session["count"] += 1
    else:
        session["count"] = 1
    return render_template("index.html", counter = session["count"])

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

@app.route("/incrementby2", methods=["POST"])
def add_two():
    session["count"] += 1
    return redirect("/")

app.run(debug = True)