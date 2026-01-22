# Crée le venv si nécessaire
if (!(Test-Path "venv")) {
    python -m venv venv
}

# Active le venv
.\venv\Scripts\Activate.ps1

# Installe les dépendances
pip install -r requirements.txt

# Lancer l'application
python .\run_app.py
