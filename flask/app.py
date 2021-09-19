  
from flask import Flask, render_template, request, redirect, url_for, session
import requests as re

app = Flask(__name__)
api_url = 'localhost:8000/api/'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if(request.method=='POST'):
        data = {    
            'email': request.form['email'],
            'password': request.form['password'] 
        }
        user = re.post(api_url, data=data).json()
        #Store the data in session
        session['email'] = user.email
        session['room'] = user.room
        return render_template('chat.html', session = session)
    else:
        if(session.get('email') is not None):
            return render_template('chat.html', session = session)
        else:
            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()