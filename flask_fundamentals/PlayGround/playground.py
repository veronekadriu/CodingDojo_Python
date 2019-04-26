from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("home.html")

@app.route("/play") 
def play():
    return render_template("playground.html")

@app.route("/play/<x>") 
def playXTimes(x):
    x = (int)(x)
    return render_template("playground2.html",times=x)

@app.route("/play/<x>/<color>") 
def changeColor(x, color):
    x = (int)(x)
    return render_template("playground3.html",times=x , color=color)





if __name__=="__main__":
    app.run(debug=True)