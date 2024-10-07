# Utiliser une image de base Python
FROM python:3.12.2

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port de l'application
EXPOSE 8000

# Commande pour démarrer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
