from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash("Tu dois être connecté pour accéder à cette page.")
            return redirect(url_for('main.signup'))
        return f(*args, **kwargs)
    return decorated_function


# Stockage temporaire des utilisateurs (en mémoire)
users = {}  # {username: password}

def valid_login(username, password):
    return username in users and users[username] == password

def create_user(username, password):
    if username in users:
        return False
    users[username] = password
    return True
