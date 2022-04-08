
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
@app.route("/emailop",methods=["POST","GET"])
def eeee():
    return render_template("emailvrf.html")
@app.route("/email",methods=["POST","GET"])
def ffff():
  try:
    global emaill
    global otp
    emaill=request.form['mail']
    serv.execute("select email from UserInf")
    lmail=serv.fetchall()
    lmail=[j for i in lmail for j in i]
    if(1):       
            sender_address = 'hclteam4546@gmail.com'
            sender_pass = '________'#password here
            receiver_address = emaill
            message = MIMEMultipart()
            print(message)
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'HCL OPT VER'   
            otp=str(random.randint(1111,9999))
            message.attach(MIMEText( 'Use the OTP  to verify your email ID:-'+otp,'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
            return render_template("otpvrf.html")
  except:
      return render_template("emailnotfound.html")
@app.route("/otpvv",methods=["POST","GET"])
def ooo():
    global otp
    genotp=request.form['o1']+request.form['o2']+request.form['o3']+request.form['o4']
    if(otp==genotp):
         return render_template("signup.html")
    else:
        return render_template("emailerror.html")
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
     global emaill
     usr=request.form['Usr']  
     pas=request.form['pas']
     con=request.form['con']
     serv.execute("select UserName from UserInf")
     ur=serv.fetchall()
     ur=[j for i in ur for j in i]
     serv.execute("select UsPassword from UserInf")
     ps=serv.fetchall()
     ps=[j for i in ps for j in i]
     if usr=="":
         return render_template("EntterUN.html")
     if usr not in ur:
         if con=='8':
              sql = "INSERT INTO UserInf(UserName,UsPassword,email) VALUES (%s, %s,%s)"
              val = (usr,pas,emaill)
              serv.execute(sql, val)
              DS.commit()
              return render_template("welcome.html")
         else:
             return render_template("passentry.html")
     else:
         return render_template("exist.html") 
app.run()