from flask import Flask,render_template,request
from flask_mysqldb import MySQL
# import mysql.connector


app=Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "users"

mysql = MySQL(app)

@app.route('/',methods= ['GET','POST'])
def index ():


    if request.method =='POST':
        username = request.form['username']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student(Name,Email) VALUES(%s,%s)",(username,email))
        mysql.connection.commit()
        cur.close()
        return"success"

    return render_template('index_1.html')

app.run(debug=True)