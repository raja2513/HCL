
from flask import *
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
DS=mysql.connector.connect(host="localhost",user="root",password="",database="code")
serv=DS.cursor()
app=Flask(__name__,template_folder='templates')
@app.route('/')
def funn():
    return render_template("login.html")
@app.route('/login', methods=['POST','GET']) 
def fun():
     usr=request.form['Usr']  
     pas=request.form['pas']
     serv.execute("select UserName from UserInf")
     ur=serv.fetchall()
     ur=[j for i in ur for j in i]
     serv.execute("select UsPassword from UserInf")
     ps=serv.fetchall()
     ps=[j for i in ps for j in i]
     if usr in ur:
         if pas in ps:
             if(ur.index(usr)==ps.index(pas)):
                 return render_template("welcome.html",name=pas)
             else:
                 return render_template("paserror.html")
         else:
             return render_template("paserror.html")
     else:
        return render_template("usrerror.html")
emaill=''
otp=''
genotp=''
@app.route("/email",methods=["POST","GET"])
def ffff():
    print("****")
@app.route('/signupp', methods=['POST','GET']) 
def ee():
       return render_template("signup.html")
@app.route('/err', methods=['POST','GET']) 
def fun1():
       return render_template("login.html")
@app.route('/er', methods=['POST','GET']) 
def f():
       return render_template("signup.html")
@app.route('/signup',methods=['POST','GET'])
def fun2():
     usr=request.form['Usr']  
     pas=request.form['pas']
     con=request.form['con']
     serv.execute("select UserName from UserInf")
     ur=serv.fetchall()
     ur=[j for i in ur for j in i]
     serv.execute("select UsPassword from UserInf")
     ps=serv.fetchall()
     ps=[j for i in ps for j in i]
     print(usr,*ur,usr not in ur)
     if usr not in ur and usr!='':
         if con=='8':
              sql = "INSERT INTO UserInf(UserName,UsPassword) VALUES (%s, %s)"
              val = (usr,pas)
              serv.execute(sql, val)
              DS.commit()
              return render_template("welcome.html")
         else:
             return render_template("paserror.html")
     else:
         return render_template("exist.html") 
app.run()