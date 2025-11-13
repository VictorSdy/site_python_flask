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
│   ├── __init__.py           # Initialisation de Flask et SocketIO
│   ├── routes.py             # Routes principales (home, news, son, etc.)
│   ├── auth_routes.py        # Authentification (login, signup, logout)
│   ├── socketio_events.py    # Gestion du tchat et de la visioconférence
│   │
│   └── templates/
│       ├── login.html
│       ├── signup.html
│       ├── home.html
│       ├── tchat_visio.html
│       └── page_not_found.html
│
├── run.py                    # Point d’entrée principal
└── README.md                 # Documentation du projet
```


