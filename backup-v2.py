
import os
import shutil
import zipfile
import subprocess,sys

#Cration de la fonction de compression en .zip
def	docompress(source_folder, target_zip):

    print ('=> Starting function')
    
    if  os.path.exists( target_folder +'.zip'):
        # Si le dossier existe déjà 
        reponse_user_user = input("le Zip existe deja voulez vous ecraser, oui ou non ?")
        
        while reponse_user_user != "oui" and  reponse_user_user != "non":
                reponse_user_user = input(" repondez uniquement par  [oui] ou [non]  ")   
        
        if reponse_user_user == 'oui':
            #suppression et lancement de la fonction de compression 
            os.remove(target_folder +'.zip')
            
            zipf = zipfile.ZipFile(target_zip, "w")
            for subdir, dirs, files in os.walk(source_folder):
                for file in files:
                    print (os.path.join(subdir, file))
                    zipf.write(os.path.join(subdir, file))
            print ("l'archive a été ecrasée ==>", target_folder +'.zip')             

        else:   
            print ('=====> Operation anulee')   
        
    else:
        zipf = zipfile.ZipFile(target_zip, "w")
        for subdir, dirs, files in os.walk(source_folder):
            for file in files:
                print (os.path.join(subdir, file))
                zipf.write(os.path.join(subdir, file))
        print ("Zip Created =====>", target_zip)
   
    print ('=> Ending fonction')




#Copie des dossier, fichier vers la cible 
def	docopy(source_folder, target_folder):

        print ('=> Starting function')

        try:
            shutil.copytree(source_folder,target_folder )
            print ('===> Copy create')   
        except FileExistsError:
            # Si le dossier existe déjà
            reponse_user_user = input("le dossier existe deja voulez vous ecraser, oui ou non ?")

            while reponse_user_user != "oui" and  reponse_user_user != "non":
                reponse_user_user = input(" repondez uniquement par  [oui] ou [non]  ")


            if reponse_user_user == 'oui':
                #suppression et lancement de la fonction de copie
                shutil.rmtree(target_folder)    
                shutil.copytree(source_folder,target_folder )
                print ("===> Ecrasement effectué  ", target_folder)
                    
            else:   
                print ('===> Operation anulee')   
        pass

        print ('=> Ending fonction')



if __name__ =='__main__':
    print ('Starting script')
				
#Recuperation du hostname
cmd = subprocess.Popen(["powershell.exe", 
    "[Environment]::UserName "],  
    stdout=subprocess.PIPE, universal_newlines=True)
hostname = cmd.communicate()[0].replace('\n','')

print ('Initialisation des paths')

#/!\ Penser a mettre un slash de chaque coté : ex : /media/backup/
source_folder = input("Merci de nous indiquer le chemin absolue du dossier à sauvegarder ")

#/!\ Penser a mettre un slash de chaque coté : ex : /media/backup/
target_folder = input("Merci de nous indiquer l'emplacement final du backup ")
target_folder = target_folder+"\\"+ hostname

print('source ===>',source_folder)
print('targert ===>',target_folder)


reponse_user = input("Voulez faire une archive compressé de votre dossier user, oui ou non ?")

while reponse_user != "oui" and  reponse_user != "non":
    reponse_user = input(" repondez uniquement par  [oui] ou [non]  ")

#verification si ficher exist si oui demander si on l'ecrase a fairre !!
if reponse_user == 'oui':

    #Compression vers un dossier en .zip
        print ('***Starting Compress***')
        docompress(source_folder, target_folder +'.zip')
        print ('***Ending Compress***')

else:
    #Copie des dossier et fichier vers la cible
        print ('***Starting Copy***')
        docopy(source_folder, target_folder)
        print ('***Ending Copy***')

    

print ('Ending script')