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
    mycursor=mydb.cursor()
    if request.method =='POST':
        result = request.form.to_dict()
        name= result['Name']
        phy = int(result['Physics'])
        che = int(result['Chemistry'])
        mat = int(result['Mathematics'])
        s = str(phy+che+mat)
        result["Total"] =s
        mycursor.execute("insert into piyas (name,phy,che,mat,total)values(%s,%s,%s,%s,%s)",(name,phy,che,mat,s))
        mydb.commit()
        mycursor.close()
        return render_template('test.html',result= result)
    return render_template("index.html")


app.run(debug=True)