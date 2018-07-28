# Documentation d'installation

## Environnement

### Application basé sur le framework Django 2.0

Nécessite une version de Python supérieur à 3.4

Sur Windows, assurez-vous que la commande suivante renvoi bien le numéro de version:

```bash
python --version
```

Si ce n'est pas le cas, il vous manque peut-être Python sur votre ordinateur, ou votre répertoire n'a pas été ajouté au PATH Windows, pour cela reportez-vous à la documentation suivante:

Installation de Python: https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/230659-quest-ce-que-python#/id/r-2447950

Ajout de Python à la variable PATH:
```
For Windows 10/8/7:
Open System Properties (Right click Computer in the start menu, or use the keyboard shortcut Win+Pause)
Click Advanced system settings in the sidebar.
Click Environment Variables...
Select PATH in the System variables section
Click Edit
Add Python's path to the end of the list (the paths are separated by semicolons). For example:

C:\Windows;C:\Windows\System32;C:\Python27

## For Windows XP:
Open System Properties (Type it in the start menu, or use the keyboard shortcut Win+Pause)
Switch to the Advanced tab
Click Environment Variables...
Select PATH in the System variables section
Click Edit
Add Python's path to the end of the list (the paths are separated by semicolons). For example:

C:\Windows;C:\Windows\System32;C:\Python27
```

Installation de virtualenv:

```bash
pip install virtualenv
```

Installation de Django, puis mise à jour

```bash
pip install Django==2.0
pip install Django --upgrade
```

Récupérer le repo actuel dans un répertoire quelconque (nécessite git, sous windows, téléchargez gitbash: https://gitforwindows.org/)

```bash
git clone https://github.com/aittiritesoufian/ESGI-pythonproject.git
```

Rendez-vous dans le répertoire ESGI-pythonproject/webannonces/
```bash
cd ESGI-pythonproject/webannonces/
```

Lancez la commandea suivante permettant d'initialiser la base de donnée du projet:
```bash
python manage.py migrate
```

Lancez maintenant la commande suivante, permettant de lancer le serveur web:
```bash
python manage.py runserver
```

Une fois le serveur lancé, rendez-vous sur l'URL suivante pour accéder à la page d'accueil du site:
```url
http://localhost:8000/annonces/
```

Vous pouvez peupler la base de données avec 200 annonces et 2 utilisateurs en vous rendant sur cette url:
```url
http://localhost:8000/annonces/peupleurbdd/
```

Utilisateurs générés avec le peupleur:
```bash
user : Soufian
password : mypass

user : Pierre
password : mypass2
```
