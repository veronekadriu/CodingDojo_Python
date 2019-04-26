from flask import Flask, render_template, redirect, request

from mysqlconnection import connectToMySQL
app = Flask(__name__)



@app.route('/')
def index():
    mysql = connectToMySQL("leadsandclients")
    leadsandclients = mysql.query_db("SELECT * FROM leadsandclients")
    return render_template('index.html', leadsandclients =  leadsandclients)

@app.route("/update_date", methods =['POST'])
def create():
    mysql = connectToMySQL("leadsandclients")
    query = "UPDATE leadsandclients SET start_report_date = %(start_report_date)s, end_report_date = %(end_report_date)s WHERE customers = %(customers)s;"
  
    data = {
                "customers" :request.form['customers'],
                "start_report_date": request.form['start_report_date'],
                "end_report_date": request.form['end_report_date']
            }
    leadsandclients = mysql.query_db(query, data)
    return redirect('/')
    


if __name__ == "__main__":
    app.run(debug=True)