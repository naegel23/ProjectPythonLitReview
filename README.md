# ProjectPythonLitReview
Installation du projet Projet_P9 sur votre machine

Aller sur le dépôt github : https://github.com/naegel23/ProjectPythonLitReview/

Dans l'onglet <> Code de la page ci-dessus, cliquer sur le bouton Code puis sur Download ZIP
Placer le fichier zip dans le dossier projects et le dézipper.
Ouvrir un terminal et se déplacer dans la racine du projet dossier.

Installer pip pour python3 si ce n'est pas déjà fait.
Créer un environnement virtuel et l'activer.

Installer les dépendances du projet
Toujours à la racine du projet, lancer l'une des 2 commandes suivantes :

pip3 install -r requirements.txt

python3 -m pip install -r requirements.txt

Une fois l'environnement virtuel activé et les dépendances du projet Projet_P9 installées, en étant positionné dans le dossier pythonProjectLitReview,
si besoin se déplacer dans le répertoire du projet Django lit_review contenant le fichier manage.py en tapant la commande : 

cd nom_du_fichier 

Puis lancer le serveur Django en tapant la commande :

python manage.py runserver 

Une fois le serveur démarré, ouvrir un navigateur et taper l'url : http://127.0.0.1:8000/
La page de connexion au site web LITReview s'affiche alors dans votre navigateur.
