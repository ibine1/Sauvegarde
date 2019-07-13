<center> <h1>Script de sauvegarde en Python</h1> </center>

## Langage utilisé ##  

PowerShell  
Python 

## Prerequis ##
- Vous devez avoir les droits administrateurs  
- Un environnement Python, Vous pouvez télécharger Python 3.7 [ici](  https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe)

## Présentation ##  

Ce script a été écrit avec python 3.7.4,  il est donc fonctionnel avec l'environnement Python 3.7.4 ou plus. Ce script a pour but de sauvegarder vos données. Il vous offre la possibilité de faire une copie de vos données ou bien de les compresser.
Lors du lancement du script il suffit de lui préciser si vous souhaitez une simple sauvegarde ou une archive en '.zip', ensuite il vous demandera le dossier source ainsi que l'emplacement de la sauvegarde.

## Installation ##

- Téléchargez Python 3.X, vous pouvez télécharger python via le lien fourni ci-dessus.
- Installez Python avec les droits admin
- Vérifiez que le path pour python a bien été créé.

## Exemple d'utilisation ##

Lancez votre cmd en mode admin 

![0](https://user-images.githubusercontent.com/52750872/61171631-9ec7d400-a57a-11e9-889a-0768cfb36a03.PNG)

Rendez-vous dans le répertoire du script backup.py via l'invite de commande, puis tapez " python backup.py"  afin de lancer le script. 

![1](https://user-images.githubusercontent.com/52750872/61171632-9ec7d400-a57a-11e9-9f7e-f2613223416b.PNG)

Indiquez le nom de l'emplacement du dossier source à sauvegarder puis le nom de l'emplacement de la sauvegarde 


![2](https://user-images.githubusercontent.com/52750872/61173048-118e7a80-a58e-11e9-8d7d-412966fab132.PNG)

### Création d'un archive en ".zip"

Si vous voulez, créer une archive de votre dossier répondez oui
 
![3](https://user-images.githubusercontent.com/52750872/61171634-9ec7d400-a57a-11e9-9301-05177db3c3c2.PNG)

Si l'archive n'existe pas elle se crée.  

Si l'archive exite le script vous demandera si vous voulez l'écraser, répondez oui ou non selon vos besoin.

![4](https://user-images.githubusercontent.com/52750872/61171635-9ec7d400-a57a-11e9-9d7a-44987feb96b2.PNG)

En Sachant que si vous répondez oui il écrasera votre archive, si vous répondez non l'opération sera annulée et ça sera la fin du script.

![5](https://user-images.githubusercontent.com/52750872/61171627-9e2f3d80-a57a-11e9-9a36-1ab26d155276.PNG)


### Création d'une sauvegarde simple 

Si vous souhaitez créer une simple sauvegarde, répondez non, le script fera une simple copie de votre de dossier 
  
![6](https://user-images.githubusercontent.com/52750872/61171628-9e2f3d80-a57a-11e9-8dda-2e8caf928195.PNG)   

Si le dossier existe, le script vous demandera si vous voulez l'écraser, répondez oui ou non selon vos besoin.

![7](https://user-images.githubusercontent.com/52750872/61171629-9e2f3d80-a57a-11e9-8d02-f2d51d2cbf42.PNG)

En Sachant que si vous répondez oui il écrasera votre dossier, si vous répondez non l'opération sera annulée et ça sera la fin du script.

![8](https://user-images.githubusercontent.com/52750872/61171630-9e2f3d80-a57a-11e9-91f3-974056038743.PNG)

## Authors ##
Ibine && Moussi13 
## Licence ##

Ce projet est sous la licence MIT  -- Pour plus de détails cliquez [ici](https://choosealicense.com/licenses/)

