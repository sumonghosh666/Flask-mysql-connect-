from flask import Flask

app = Flask(__name__)
@app.route('/')
def html():
    return """<h1 style = "color:blue;"> Hello You tube </h1>"""

app.run(debug=True)
