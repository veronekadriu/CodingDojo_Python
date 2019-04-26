from flask import Flask, render_template, redirect, request
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'


@app.route('/')
def index():
    mysql = connectToMySQL("friendsdb")
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('index.html', friends =  all_friends)
@app.route("/create_friend", methods =['POST'])
def create():
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name,created_at,updated_at,occupation) VALUES (%(first_name)s, %(last_name)s,NOW(), NOW(),%(occupation)s);"
    data = {
                "first_name" :request.form['first_name'],
                "last_name": request.form['last_name'],
                "occupation": request.form['occupation']
            }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')
    

# now, we may invoke the query_db method

if __name__ == "__main__":
    app.run(debug=True)
