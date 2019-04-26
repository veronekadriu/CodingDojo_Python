from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')


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

    if len(form['firstname'])<1:
        errors.append("First name must be written!")
    if any(char.isdigit() for char in request.form['firstname']) == True:
        errors.append('First name cannot have  any numbers!')
    if len(form['firstname'])<1:
        errors.append("Last name must be written!")
    if any(char.isdigit() for char in request.form['lastname']) == True:
        errors.append('Last name cannot have any numbers!')
    if len(form['email'])<1:
        errors.append("Email must be written!")
    if len(form['password'])<1:
        errors.append("Password must be written!")
    if len(form['password'])<8:
        errors.append("Password should be more than 8 characters!")
    if not  EMAIL_REGEX.match(request.form['email']):
        errors.append("You should enter a valid email!")
    if not  PASSWORD_REGEX.match(request.form['password']):
        errors.append("Your password should have at least  1 uppercase letter and 1 numeric value")
    if request.form['confirm_password'] != request.form['password']:
        errors.append("Passwords should match!")
        
    
    
    
    
    if len(errors)>0:
        for error in errors:
            flash(error)

        return redirect("/")
    else:
        session['firstname']= request.form['firstname']
        session['lastname']= request.form['lastname']
        session['email']= request.form['email']
        session['password'] = request.form['password']
        return redirect("/success")






if __name__== "__main__":
    app.run(debug=True)
