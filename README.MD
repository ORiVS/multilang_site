
# Projet Multilang Site avec Chatbot

Ce projet est un site web simple développé avec Django, intégrant la gestion multilingue et un chatbot utilisant un modèle de langage GPT pour répondre aux utilisateurs.

## Configuration du Projet

### Prérequis

Avant de commencer, assurez-vous d'avoir installé Python 3.x et pip sur votre système.

### Installation

1. Clonez le repository depuis GitHub :

   ```bash
   git clone https://github.com/ORiVS/multilang_site.git
   cd multilang_site
   ```

2. Créez un environnement virtuel (recommandé) :

   ```bash
   python -m venv env
   # Sur Windows
   .\env\Scripts\activate
   # Sur macOS/Linux
   source env/bin/activate
   ```

3. Installez les dépendances Python nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

### Configuration Django

1. Configurez les variables d'environnement :

   Créez un fichier `.env` à la racine du projet et ajoutez-y votre clé API OpenAI :

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Assurez-vous que `django-environ` est installé pour charger les variables d'environnement à partir de ce fichier.

2. Effectuez les migrations de la base de données :

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Utilisation

1. Lancez le serveur de développement Django :

   ```bash
   python manage.py runserver
   ```

2. Accédez à l'application dans votre navigateur :

    - Accueil : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - Version anglaise : [http://127.0.0.1:8000/en/](http://127.0.0.1:8000/en/)
    - Version française : [http://127.0.0.1:8000/fr/](http://127.0.0.1:8000/fr/)
    - Chatbot : [http://127.0.0.1:8000/chatbot/](http://127.0.0.1:8000/chatbot/)

## Fonctionnalités

- **Articles de Blog :** Affiche une liste d'articles dans différentes langues.
- **Multilinguisme :** Permet de basculer entre l'anglais et le français.
- **Chatbot :** Répond aux messages des utilisateurs en utilisant un modèle de langage GPT.