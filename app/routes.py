from flask import Blueprint, render_template, redirect, url_for,request,session
from .utils import login_required,valid_login,create_user
import feedparser

bp = Blueprint('main', __name__)

@bp.route("/")
def root():
    """ return redirect(url_for('main.signup')) """
    return redirect(url_for('main.auth'))

@bp.route('/home')
@login_required
def home():
    return render_template('home.html') 

@bp.route('/son')
@login_required
def son():
    #return redirect("https://www.youtube.com/watch?v=E8gmARGvPlI&list=RDE8gmARGvPlI&start_radio=1")
    return render_template('partials/son.html')

@bp.route('/newsbe')
@login_required
def partial_newsbe():
    feed = feedparser.parse("https://rss.rtbf.be/article/rss/highlight_rtbf_info-belgique.xml")
    articles = feed.entries[:10]  # 10 derniers articles
    return render_template('partials/newsbe.html',articles=articles)

@bp.route('/newsfr')
@login_required
def newsfr():
    feed = feedparser.parse("https://www.franceinfo.fr/france.rss")
    articles = feed.entries[:10]  # 10 derniers articles
    return render_template('partials/newsfr.html',articles=articles)
    #return redirect("https://www.franceinfo.fr")

@bp.route('/tchat')
@login_required
def tchat():
    return render_template('tchat_visio.html')

""" @bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if valid_login(username, password):
            session['user'] = username
            return redirect(url_for('main.home'))  # 'main.home' = route home
        else:
            error = 'Nom d’utilisateur ou mot de passe incorrect'
    return render_template('login.html', error=error)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if create_user(username, password):
            hash('Compte créé avec succès ! Connectez-vous.')
            return redirect(url_for('login'))
        else:
            error = 'Nom d’utilisateur déjà utilisé'
    return render_template('signup.html', error=error) """

@bp.route('/auth', methods=['GET', 'POST'])
def auth():
    error = None

    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')
        password = request.form.get('password')

        if action == 'login':
            if not valid_login(username, password):
                error = "Aucun compte n'existe ou mot de passe incorrect"
            else:
                session['user'] = username
                return redirect(url_for('main.home'))

        elif action == 'signup':
            if not create_user(username, password):
                error = "Nom d'utilisateur déjà utilisé"
            else:
                error = "Compte créé avec succès 🎉 Vous pouvez vous connecter."

    return render_template('auth.html', error=error)



@bp.route('/logout')
def logout():
    session.pop('user', None)
    hash('Vous êtes déconnecté.')
    return redirect(url_for('main.auth'))
