from flask import Flask

app = Flask(__name__)
@app.route('/')
def div():
    return """<div style= "width:300px;height:300px;background-color:red;margin-left:200px;margin- top:200px;">
    <h1> Hello You Tube</h1>
    <h1> Hello You Tube</h1>
    <h1> Hello You Tube</h1>
    <h1> Hello You Tube</h1>
    
     </div>"""

app.run(debug=True)