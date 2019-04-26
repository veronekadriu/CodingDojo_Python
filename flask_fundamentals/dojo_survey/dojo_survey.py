from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="Helloo"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/process", methods=["POST"])
def process():
    form = request.form
    errors = []

    if len(form['name'])<1:
        errors.append("Name must be written!")
    if len(form['comment'])>120:
        errors.append("Comment must be shorter than 120 characters")
    if len(form['comment'])<1:
        errors.append("Comment must be written!")
    
    if len(errors)>0:
        for error in errors:
            flash(error)

        return redirect("/")
    else:
        session['name']= request.form['name']
        session['location']= request.form['location']
        session['language']= request.form['language']
        session['comment'] = request.form['comment']
        return redirect("/success")






if __name__== "__main__":
    app.run(debug=True)
