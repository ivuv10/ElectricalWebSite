from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/", methods=['post','get'])

def login():
   message=''
   if request.method == 'POST':
       user=request.form.get('userName')
       pas=request.form.get('passWord')
       if user=='eyal' and pas=='peretz':
          return render_template('2.html')
       else:
          message='sorry, There is a mistake'
          return render_template('1.html', message=message)
   return render_template('1.html')
    
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)