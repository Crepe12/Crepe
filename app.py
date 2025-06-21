from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    if room not in rooms:
        rooms[room] = [""] * 9
    emit('update_board', rooms[room], to=room)

@socketio.on('move')
def handle_move(data):
    room = data['room']
    index = data['index']
    player = data['player']
    if rooms[room][index] == "":
        rooms[room][index] = player
        emit('update_board', rooms[room], to=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)
