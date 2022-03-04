from flask  import *
app=Flask(__name__)
@app.route('/s',methods=['POST'])
def fun():
  res=request.form
  f=open('c.csv','a')
  f.write('\n')
  s=res.name+','+res.pass
  f.write(s)
  f.close()
