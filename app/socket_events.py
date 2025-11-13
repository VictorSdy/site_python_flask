from flask import request
from . import socketio
from flask_socketio import emit, send

# Global variables
connected_users = set()
user_sid_map = {}

# Chat
@socketio.on('set_username')
def handle_set_username(username):
    global connected_users, user_sid_map
    if username not in connected_users:
        connected_users.add(username)
        user_sid_map[request.sid] = username
        emit('user_list', list(connected_users), broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    global connected_users, user_sid_map
    username = user_sid_map.get(request.sid)
    if username:
        connected_users.discard(username)
        del user_sid_map[request.sid]
        emit('user_list', list(connected_users), broadcast=True)

@socketio.on('message')
def handle_message(data):
    send(f"{data['username']}: {data['msg']}", broadcast=True)

# WebRTC
@socketio.on('join_video')
def handle_join_video(username):
    emit('new_user', request.sid, broadcast=True, include_self=False)

@socketio.on('offer')
def handle_offer(data):
    emit('offer', {'offer': data['offer'], 'from': request.sid}, to=data['to'])

@socketio.on('answer')
def handle_answer(data):
    emit('answer', {'answer': data['answer'], 'from': request.sid}, to=data['to'])

@socketio.on('ice-candidate')
def handle_ice(data):
    emit('ice-candidate', {'candidate': data['candidate'], 'from': request.sid}, to=data['to'])
