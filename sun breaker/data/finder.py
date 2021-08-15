from cytron import *


bk = True
rt = False

tf = "pf4"

fichier = cy_rfil_rela("/home/pf4/dev/sun breaker","data.txt")
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