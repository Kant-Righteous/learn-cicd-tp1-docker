# Learn CI/CD - TP Docker

## Exercice 3: Manipulation de base des conteneurs

### 1. Commandes exécutées
- `docker --version` : Vérification de la version de Docker
- `docker images` : Liste des images locales
- `docker pull hello-world` : Téléchargement de l'image de test
- `docker run hello-world` : Exécution du conteneur de test
- `docker ps` & `docker ps -a` : Affichage des conteneurs actifs et terminés
- `docker rm <ID>` : Suppression du conteneur arrêté
- `docker rmi <ID>` : Suppression de l'image locale

### 2. Captures d'écran
![Étape 1 à 4](Ex3/01.png)
![Étape 5 à 8](Ex3/02.png)


## Exercice 4: Création d'un serveur web avec Docker

### 1. Commandes exécutées
- `docker pull nginx` : Téléchargement de l'image officielle Nginx
- `docker run -d -p 8080:80 --name mon_nginx nginx` : Lancement du serveur web en arrière-plan avec redirection de port
- `docker ps` : Vérification du bon fonctionnement du conteneur
- `docker stop mon_nginx` : Arrêt du serveur web
- `docker rm mon_nginx` : Suppression du conteneur

### 2. Captures d'écran
- Déploiement et accès web :  
  ![Serveur Nginx actif](Ex4/01.png)
- Arrêt, suppression et vérification de la coupure de service :  
  ![Arrêt du serveur](Ex4/02.png)


## Exercice 5: Déploiement d'une application Python Flask

### 1. Description
Création d'une application minimale avec Flask, conteneurisée à l'aide d'un Dockerfile personnalisé et exécutée sur le port 5000.

### 2. Commandes exécutées
- `docker build -t flask-app .` : Construction de l'image Docker
- `docker run -d -p 5000:5000 --name mon_flask flask-app` : Lancement du conteneur
- `docker ps` : Vérification du statut du conteneur
- `docker stop mon_flask` : Arrêt du conteneur
- `docker rm mon_flask` : Suppression du conteneur

### 3. Captures d'écran
- Construction et exécution du conteneur :  
  ![Build et Run](Ex5/01.png)
- Vérification dans le navigateur :  
  ![Page Web Flask](Ex5/02.png)