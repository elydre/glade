from cytron import *
from time import time

name = input("nom de la basse de donnée: ")
debut = time()
print(round(time()-debut,1),"s - lecture de la base de donnée")
fichier = cy_rfil_rela("/",name)
print(round(time()-debut,1),"s - base de donnée lu!")

while True:
    bk = True
    rt = False
    tf = input("\nbreak a trouvé: ")
    debut = time()
    print(round(time()-debut,1),"s - recherche...")
    for ligne in str(fichier).split("\n"):
        if bk:
            bk = False
            if ligne == tf:
                rt = True
        else:
            if rt:
                print(round(time()-debut,1),"s - texte en clair:", ligne)
                rt = False
            bk = True
    print(round(time()-debut,1),"s - fin")