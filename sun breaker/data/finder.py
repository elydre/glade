from cytron import *


bk = True
rt = False

tf = input("break a trouvé: ")
name = input("nom de la basse de donné: ")


fichier = cy_rfil_rela("name")
for ligne in str(fichier).split("\n"):

    if bk:
        bk = False
        if ligne == tf:
            rt = True
    else:
        if rt:
            print("trouvé:", ligne)
            break
        bk = True