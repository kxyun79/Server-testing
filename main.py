from flask import Flask, jsonify, render_template, request
server = Flask(__name__)
app = Flask('a')

data = "The message is " + "'hello world!'"

def sendit():
  if request.method == "SEND":
    if request.form.get('send'):
      return render_template('personal_user.html')
    else:
      return render_template('page.html')
  elif request.method == "GET":
    #dosomething
    pass
@app.route('/')
def index():
	return render_template('page.html')
  

@app.route('/userpage')
def userpage():
  return render_template('personal_user.html')


app.run('0.0.0.0',8080)