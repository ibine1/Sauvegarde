
import os
import shutil
import zipfile
import subprocess,sys

#copy files and folder and compress into a zip file
def	docompress(source_folder, target_zip):

    print ('=> Starting function')
    
    if  os.path.exists( target_folder +'.zip'):
        # directory already exists
        reponse_user = input("le Zip existe deja voulez vous ecraser, o ou n ?")
        if reponse_user == 'o':
            #suppression et relancé la fonction
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




#copy files to a target folder	
def	docopy(source_folder, target_folder):

        print ('=> Starting function')

        try:
            shutil.copytree(source_folder,target_folder )
            print ('===> Copy create')   
        except FileExistsError:
            # directory already exists
            reponse_user = input("le dossier existe deja voulez vous ecraser, o ou n ?")
            if reponse_user == 'o':
                #suppression et relancé la fonction
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


reponse_user = input("Voulez faire une archive compressé de votre dossier user, o ou n ?")

#verification si ficher exist si oui demander si on l'ecrase    a fairre !!
if reponse_user == 'o':

    #compress to zip
        print ('***Starting Compress***')
        docompress(source_folder, target_folder +'.zip')
        print ('***Ending Compress***')

else:
    #copy files to a target folder
        print ('***Starting Copy***')
        docopy(source_folder, target_folder)
        print ('***Ending Copy***')

    

print ('Ending script')