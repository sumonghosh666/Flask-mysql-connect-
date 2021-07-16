from flask import Flask,render_template,request
import mysql.connector

app = Flask (__name__)
@app.route('/')
def students():
    return render_template('index.html')



@app.route('/result',methods =['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host ="localhost",
        user= "root",
        password ="",
        database="sanjoy"
    )
    mycursor=mydb.cursor
    if request.method =='POST':
        result = request.form.to_dict()
    
        phy = int(request.form['Physics'])
        che = int(request.form['Chemistry'])
        mat = int(request.form['Mathematics'])
        s = str(phy+che+mat)
        result["Total"] =s
        return render_template('test.html',result= result)

app.run(debug=True)