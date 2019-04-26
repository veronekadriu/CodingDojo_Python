
from flask import Flask
app = Flask(__name__)
# 1.localhost:5000 - have it say "Hello World!" - Hint: If you have only one route that your server is listening for, it must be your root route ("/")

@app.route("/")
def index():
    return "Hello World!"
# 2.localhost:5000/dojo - have it say "Dojo!"
@app.route("/dojo")
def coding():
    return "Dojo!"

# 3.4.5localhost:5000/say/flask - have it say "Hi Flask".  Have function say() handle this routing request. The same goes for 4 and 5
@app.route("/say/<name>")
def say(name):
    return "Hi " + name.capitalize() + " !"
# 6.7localhost:5000/repeat/35/hello - have it say "hello" 35 times! The same goes for 7
@app.route("/repeat/<num>/<word>") 
def repeat(num, word):
    print(num)
    print( word )
    num = (int)(num)
    return  (" "+ word + " ")*num




if __name__ == "__main__":
    app.run(debug=True)