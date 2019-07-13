<center> <h1>Script de sauvegarde en Python</h1> </center>

## Langage utilisé ##  

Pwershell  
Python 

## Prerequis ##
- Vous devez avoir les droits administrateurs  
- Un environnement Python, Vous pouvez télécharger Python 3.7 [ici](  https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe)

## Présentation ##  

Ce script a été écrit avec python 3.7.4,  il est donc fonctionnel avec l'environement Python 3.7.4 ou plus.  

Ce script a pour but de sauvegarder vos données. Il vous offre la possibilité de faire une copie de vos données tel que ou bien de les compresser.

Lors du lancement du script il suffit de lui préciser si vous souhaité une simple sauvegarde ou une archive en '.zip', ensuite il vous demandera le dossier source ainsi que l'emplacement de la sauvegarde.

## Installation ##

- Il faut télécharger Python 3.X, vous pouvez télécharger python via le lien fourni ci-dessus.
- Installer Python avec les droits admin
- Vérifier que le path pour python a bien été créé.

## Exemple d'utilisation ##

Lancer votre cmd en mode admin 

![Screenshot](0.Png)

Rendez-vous dans le répertoire du script backup.py via l'invite de commande. puis tapez " python backup.py"  afin de lancer le script. 

![Screenshot](1.png) 

Indiquez le nom de l'emplacement du dossier source à sauvegarder puis le nom de l'emplacement de la sauvegarde 


![Screenshot](2.png) 



### Création d'un archive en ".zip"
Si vous voulez, créer une archive de votre dossier répondez oui
 
![Screenshot](3.png)

Si l'archive n'existe pas elle se crée.  

Si l'archive exite le script vous demandera si vous voulez l'ecraser, répondez oui ou non selon vos besoin.

![Screenshot](4.png)

En Sachant que si vous répondez oui il écrasera votre archive, si vous répondez non l'opération sera annulée et sa sera la fin du script.

![Screenshot](5.png)

### Création d'une sauvegarde simple 

Si vous souhaitez créer une simple sauvegarde, répondez non, le script fera une simple copie de votre de dossier 
  
![Screenshot](6.png)    

Si le dossier exite le script vous demandera si vous voulez l'ecraser, répondez oui ou non selon vos besoin.

![Screenshot](7.png)

En Sachant que si vous répondez oui il écrasera votre dossier, si vous répondez non l'opération sera annulée et sa sera la fin du script.

![Screenshot](8.png)

## Authors ##
Ibine && Moussi13 
## Licence ##

Ce projet est sous la licence MIT  -- Pour plus de détails cliquez [ici](https://choosealicense.com/licenses/)

