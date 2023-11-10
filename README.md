# Test Technique Projet de Paiement en ligne

## Description du Projet
Ce projet est une petite application de paiement en ligne, développée en utilisant React pour le frontend, Django pour le backend, et une base de données MySQL.

## Fonctionnalités

- Les utilisateurs peuvent ajouter des produits à leur panier, respectant les limites de stock.
- Une page de paiement permet aux utilisateurs de finaliser leur commande.
- Les commandes sont enregistrées dans la base de données avec le prix total et les détails des articles.
- La gestion du stock des produits est mise à jour après chaque commande.

## Structure du Projet

- Le frontend est développé en React.
- Le backend est développé en Django.
- La base de données MySQL est utilisée pour stocker les informations sur les produits et les commandes.

## Installation et Exécution

### Frontend (React)

1. Naviguez vers le répertoire frontend : `cd frontend`   
2. Installez les dépendances : `npm install`   
3. Démarrez l'application : `npm start`   

### Backend (Django)
1.Ouvrire le Projet et Installer virtualenv : pip install virtualenv    
2.Puis crier un enveronement : virtualenv myenv     
3. Activez l'environnement virtuel :    
   - Sur Windows : `myenv\scripts\activate`

4. Installez les dépendances : `pip install -r requirements.txt`
5. Naviguez vers le répertoire backend : `cd backend`   
6. Appliquez les migrations : `python manage.py migrate`
7. Démarrez le serveur : `python manage.py runserver`




