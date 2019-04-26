from flask import Flask, render_template, redirect, request,flash, session

from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key="Helloo"


@app.route('/')
def index():
    mysql = connectToMySQL("emailsdb")
    emails = mysql.query_db("SELECT * FROM emails")
    
    return render_template('index.html', emails =  emails)
@app.route("/process", methods =['POST'])
def create():
    mysql = connectToMySQL("emailsdb")
    form = request.form
    errors = []

    
    if len(form['email'])<1:
        errors.append("Email must be written!")
        
    if not  EMAIL_REGEX.match(form['email']):
        errors.append("You should enter a valid email!")
   
    query = "SELECT id FROM emails WHERE email= %(email)s;"
    data = {
                "email" : request.form['email']
    }
    email_list = mysql.query_db(query, data)

    if len(email_list)>0:
        errors.append("Email is already taken!")

    if len(errors)>0:
        for error in errors:
            flash(error)

        return redirect("/")
    else:
        
    
        session['email'] = form['email']
        
        
        return redirect('/emails')
@app.route("/emails")
def email():
    mysql = connectToMySQL("emailsdb")
    query = "INSERT INTO emails (email,created_at,updated_at) VALUES (%(email)s,NOW(), NOW());"
    data = {
                "email" : session['email']
                
        }
    mysql.query_db(query, data)
    return redirect("/success")



@app.route("/success")
def success():
    flash("The email address you entered is a VALID email. Thank you!")
    mysql = connectToMySQL("emailsdb")
    emails = mysql.query_db("SELECT * FROM emails")
     
    
    return render_template('emails.html', emails =  emails)

@app.route("/delete", methods = ['POST'])
def delete():
    mysql = connectToMySQL("emailsdb")

    query = "DELETE FROM emails WHERE id = %(id)s"
    data = {
            'id': request.form['id'],
        }
    mysql.query_db(query, data)
    return redirect("/success")





    



if __name__ == "__main__":
    app.run(debug=True)
   

        
        
