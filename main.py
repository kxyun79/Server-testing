from flask import Flask, render_template, request, redirect
server = Flask(__name__)
app = Flask('a')

data = 'uname'
@app.route('/')
def index():
	return render_template('page.html', )
  

@app.route('/user')
def userpage():
  return render_template('personal_user.html',user=data)


app.run('0.0.0.0',8080) 