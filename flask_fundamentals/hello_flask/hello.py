from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/coding")
def coding():
    return "<h1> Coding Dojo </h1>"

if __name__ == "__main__":
    app.run(debug=True)