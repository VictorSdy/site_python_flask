# 🌐 Site Python Flask – Chat & Visioconférence

Un site web complet développé avec **Flask**, combinant :
- 🔐 un système d’authentification (login / signup / logout),
- 💬 un tchat en temps réel avec **Flask-SocketIO**,
- 🎥 une visioconférence via **WebRTC**,
- 📰 des liens vers des actualités en ligne,
- 🎶 un accès rapide à du contenu multimédia.

---

## 🚀 Fonctionnalités

### 🏠 Page d’accueil
- Présente les différentes activités proposées :
  - Actualités belges 🇧🇪 (RTBF)
  - Actualités françaises 🇫🇷 (France Info)
  - Tchat en direct 💬
  - Lecture musicale 🎧

### 💬 Tchat en direct
- Communication instantanée entre utilisateurs connectés.
- Liste des membres *en ligne* avec statut.
- Interface moderne inspirée des messageries comme WhatsApp / Messenger.
- Gestion des pseudos via SocketIO.

### 🎥 Visioconférence (WebRTC)
- Activation automatique de la caméra.
- Appel vidéo entre utilisateurs connectés.
- Fonctionne localement et via **ngrok** pour un accès externe.

### 🔐 Authentification
- Création de compte / connexion sécurisée.
- Stockage de session utilisateur via Flask.
- Protection des routes sensibles avec `@login_required`.
- Déconnexion via bouton “Logout”.

---

## 🧱 Architecture du projet
```
site_python_flask/
│
├── app/
│   ├── static/
│   │     ├── css/
│   │     │   ├──auth.css     # style de la page d'authentification
│   │     │   ├──news.css     # style des news
│   │     │   └──style.css    # style global (à nettoyer)
│   │     └── js/
│   │         └── main.js     # chargement des page dans le container
│   ├── __init__.py           # Initialisation de Flask et SocketIO
│   ├── routes.py             # Routes principales (home, news, son, etc.)
│   ├── auth_routes.py        # Authentification (login, signup, logout)
│   ├── socketio_events.py    # Gestion du tchat et de la visioconférence
│   │
│   └── templates/
│       ├── partials/
│       ├──    ├── newsbe.html  #sous-page des actus Belgique
│       ├──    ├── newsfr.html  #sous-page des actus France
│       ├──    └── son.html     #sous-page de la redirection youtube (todo: detection des liens embed ou redirection vers soundcloud)
│       ├── login.html
│       ├── signup.html
│       ├── home.html
│       ├── tchat_visio.html
│       └── page_not_found.html
│
├── run.py                    # Point d’entrée principal
└── README.md                 # Documentation du projet
```


## Prérequis

* Python 3.x installé
* Windows (PowerShell)
* Git (pour cloner le dépôt)

---

## Installation et lancement

1. **Cloner le dépôt :**

```powershell
git clone https://github.com/tonPseudo/site_python_flask.git
cd site_python_flask
```

2. **Lancer le script PowerShell pour créer le venv, installer les dépendances et démarrer l'application :**

* **Windows Powershell :**

```powershell
.\script_lancement_site.ps1
#NB: pensez a gerer vos droits d execution de script : Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

* **Linux/macOS :**

```bash
chmod +x script_lancement_site.sh
./script_lancement_site.sh
```


* Le script fait automatiquement :

  * Création d'un environnement virtuel `venv` si nécessaire
  * Activation du venv
  * Installation des packages listés dans `requirements.txt`
  * Lancement de l'application Flask (`run_app.py`)

3. **Quitter l'environnement virtuel :**

Après avoir utilisé l'application, pour quitter le venv, tapez simplement :

```powershell
deactivate
```

## Notes

* Choisissez le script correspondant à votre système : `script_lancement_site.ps1` pour Windows PowerShell, `script_lancement_site.sh` pour Linux/macOS.
