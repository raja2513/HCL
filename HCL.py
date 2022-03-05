from flask  import *
app=Flask(__name__)
@app.route('/s',methods=['POST'])
def fun():
   return "raja"
app.run(debug=True)
