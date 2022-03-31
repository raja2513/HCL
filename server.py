from re import I
import pandas as pd
from flask import *
from csv import writer

app=Flask(__name__,template_folder='templates')
@app.route('/login', methods=['POST','GET']) 
def fun():
    
     usr=request.form['Usr']  
     pas=request.form['pas']
   
     da=pd.read_csv('data.csv')
     ur=list(da['Username'])
     
     ps=list(map(str,list(da['Password'])))
   
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
     da=pd.read_csv('data.csv')
     ur=list(da['Username'])
    
     ps=list(map(str,list(da['Password'])))
     if usr not in ur:
         if con=='8':
              l=[]
              l.append(usr)
              l.append(pas)
              print(l)
              with open('data.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(l)
                    f_object.close()
              return render_template("welcome.html") 
         else:
             return render_template("paserror.html")
     else:
         return render_template("exist.html") 
app.run()
