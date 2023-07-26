from flask import Flask, url_for, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    aa = int(request.form['a'])
    bb = int(request.form['b'])
    cc = int(request.form['c'])
    if bb**2-4*aa*cc <0:
      x1 = "no real root"
      x2 = "no real root"
    else:
      x1 = (-bb+math.sqrt(bb**2-4*aa*cc))/(2*aa)
      x2 = (-bb-math.sqrt(bb**2-4*aa*cc))/(2*aa)
    result = [x1,x2]
    return render_template('index.html', data=result) # GET
  return render_template('index.html')

@app.route('/form', methods=['GET','POST'])
def form_function():

  return render_template('index.html')

app.run(host='0.0.0.0', port=81, debug=True)
