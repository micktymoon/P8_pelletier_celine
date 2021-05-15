# Bien manger, le site pour mieux manger.

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img alt="Django" src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> <img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/> <img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>

## Pour commencer
### Pré-requis:
Vous avez besoin de : 
* Python3
* pip
* venv
* Git
* Un compte heroku
* Heroku CLI
* tout ce que le fichier .zip contient
* Django

  
### Installation : 

1. Créer un dossier qui contiendra l'application.
2. Entrer dans le dossier grâce au terminal.
```
~$ cd chemin/vers/le_dossier
```
3. Créer un nouvel environnement virtuel.
```
~$ python3 -m venv newenv
```
4. Activer le.
```
~$ source newenv/bin/activate
```
5. Se loger à Heroku.
```
~$ heroku login
```
Un message demandant d'entrer n'importe quelle lettre (sauf "q") apparait.  
Entrer n'importe quelle lettre.
Un fenêtre internet s'ouvre.  
Cliquer sur __"Log in"__.

6. Créer un clone du dépôt P7_GrandPy_Bot suivant : 
[Liens vers le dépôt P8_pelletier_celine](https://github.com/micktymoon/P8_pelletier_celine.git)
```
~$ git clone https://github.com/micktymoon/P8_pelletier_celine.git
~$ cd P8_pelletier_celine
```
7. Installer le fichier requierement.txt
```
~$ pip install -r requirements.txt
```
8. Créer une application Heroku.
```
~$ heroku create
```
9. Faire un Git Push vers Heroku main.
```
~$ git push heroku master
```
10. Normalement, cette commande ne doit rien faire, vos fichiers de migration ont déjà du être créés dans votre environnement local
```
~$ heroku run python manage.py makemigrations 
```
11. Appliquer les changements dans la base postgres Heroku.
```
~$ heroku run python migrate
```
12. Créer un utilisateur super admin.
```
~$ heroku run python manage.py createsuperuser
```
13. Remplir la base de données.
```
~$ heroku run python manage.py fill_db
```    
14. Visiter l'application à l'URL générée par son nom d'application. Ou utilisez le raccourci pratique suivant:
```
~$ heroku open
```

## Démarrage

Dans un navigateur :
1. Entrer l'url de l'application heroku. 
Ex : https://celine-bienmanger.herokuapp.com/

2. Vous pouvez maintenant rechercher des substitus de produit.

## Fabriqué avec

   * Pycharm - IDE Python
   *  <img alt="Django" src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> - Framework open-source de développement web en Python.
   *  <img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/> - Plateforme en tant que service permettant de déployer des applications sur le Cloud.
 
## Versions
<img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

Voici le lien vers la version stable : 
[Liens vers le dépôt P8_pelletier_celine](https://github.com/micktymoon/P8_pelletier_celine.git)


## Auteurs

Céline PELLETIER alias @micktymoon

## Remerciements

Je tiens à remercier la communauté d'OpenClassRooms et mon mentor de m'avoir soutenu dans ce projet.
