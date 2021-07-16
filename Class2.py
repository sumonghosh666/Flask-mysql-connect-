from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"
@app.route('/Home')
def Home():
    return "You are on Home Page"
@app.route('/Contact')
def Contact():
    return "Please see our contact pages"
app.run(debug=True)

