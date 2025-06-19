# Générateur de Factures - Django
Ce projet est une application web de gestion de produits et génération de factures, réalisée dans le cadre d’un test technique.
---

## Fonctionnalités
- Gestion CRUD des produits (nom, prix, date de péremption)
- Création de factures en sélectionnant plusieurs produits
- Affichage détaillé des factures (nombre de produits, total à payer)
- Pagination pour les listes de produits et de factures
- Interface claire et responsive grâce à Bootstrap 5.
--

## Installation
1. Cloner le dépôt :    
    git clone <https://github.com/cielxneil/generateur-factures-django>
    
    cd gestion_factures

2. Créez et activez un environnement virtuel Python :
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. Installez les dépendances :
    pip install -r requirements.txt

4. Appliquez les migrations :
    python manage.py migrate

5. Démarrez le serveur :
    python manage.py runserver

## ⚙️ Utilisation
- Rendez‑vous sur `http://127.0.0.1:8000/produits/` pour gérer vos produits.
- Rendez‑vous sur `http://127.0.0.1:8000/factures/` pour créer vos factures.

## Auteurs
- [xiel] Développeur du projet
---
