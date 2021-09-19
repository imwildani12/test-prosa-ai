  
from flask_socketio import SocketIO, join_room, leave_room, emit, close_room
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

import requests as re

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, manage_session=False)

api_url = 'http://django:8000/api/'


@app.route('/', methods=['GET', 'POST'])
def index():
    if(session.get('email') != None):
        return redirect(url_for('chat'))
    else:
        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.method=='POST'):
        data = {    
            'email': request.form['email'],
            'password': request.form['password'],
            'password2': request.form['password2'] 
        }
        url = api_url + 'register/'
        user = re.post(url, data=data).json()
        #Store the data in session
        try:
            session['email'] = user['email']
            session['room'] = user['room']
        except:
            return render_template('register.html')
        return render_template('chat.html', session = session)
    else:
        if(session.get('email') != None):
            return render_template('chat.html', session = session)
        else:
            return render_template('register.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if(request.method=='POST'):
        data = {    
            'email': request.form['email'],
            'password': request.form['password'] 
        }
        url = api_url + 'login/'
        user = re.post(url, data=data).json()
        #Store the data in session
        try:
            session['email'] = user['email']
            session['room'] = user['room']
        except:
            return "user not found"
        return render_template('chat.html', session = session)
    else:
        if(session.get('email') != None):
            return render_template('chat.html', session = session)
        else:
            return redirect(url_for('index'))


@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    join_room(room)
    emit('message', {'msg': 'prosa-bot' + ' : Hi! thanks for your visit, feel free to ask me any question!'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    data = {    
        'text': message['msg'] 
    }
    url = api_url + 'question/'
    answer = re.post(url, data=data).json()
    
    emit('message', {'msg': session.get('email') + ' : ' + message['msg']}, room=room)
    emit('message', {'msg': 'prosa-bot' + ' : ' + answer['msg']}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    print("someone")
    room = session.get('room')
    close_room(room)
    session.clear()



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='5000')