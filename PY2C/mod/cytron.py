'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
               ██
.avec    : Lolo11
.codé en : UTF-8
.langage : python 3
.github  : https://github.com/pf4-DEV/cytron
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

### importation
import os, sys
from urllib.request import urlopen
from _thread import start_new_thread

### definition des variables
global path_v, version, console_o

version_id = "cytron 13"

console_o = False
path_v = os.path.dirname(sys.argv[0])

### fonctions

def check_internet(site="https://google.com"):
    try:
        urlopen(site)
        return(True)
    except: return(False)

def console():
    if console_o == False:
        start_new_thread(console_to_thread,())

def ls(chem):
    return(os.listdir(path_v + chem))

def version():
    return(version_id)

def path():
    return(path_v)

def mkdir(chem, nom):
    try:
        temp = path_v + chem + "/" + nom
        os.makedirs(temp)
        return("DONE")
    except: return("erreur: 'chem rela + nom'")

def wget(chem, nom, addr):
    if check_internet():
        temp = path_v + chem + "/" + nom
        with open(temp, 'wb') as img: img.write(urlopen(addr).read())
        return("DONE")
    else: return("erreur: pas de connection internet")

def mkfil(chem, nom, text):
    temp = path_v + chem + "/" + nom
    fil = open(temp, "w")
    fil.write(str(text))
    fil.close()
    return("DONE")

def rfil(chem):
    fil = open(chem, "r")
    return(fil.read())

def rfil_rela(chem, nom):
    temp = path_v + chem + "/" + nom
    try:
        fil = open(temp, "r")
        return(fil.read())
    except: pass

### retro compatibilité
def cy_console():               return(console())
def cy_ls(chem):                return(ls(chem))
def cy_version():               return(version())
def cy_path():                  return(path())
def cy_mkdire(chem, nom):       return(mkdir(chem, nom))
def cy_mkdir(chem, nom):        return(mkdir(chem, nom))
def cy_wget(chem, nom, addr):   return(wget(chem, nom, addr))
def cy_mkfil(chem, nom, text):  return(mkfil(chem, nom, text))
def cy_rfil(chem):              return(rfil(chem))
def cy_rfil_rela(chem, nom):    return(rfil_rela(chem, nom))
def cy_run(ipt):                return(run(ipt))

### console pour console_print
def console_to_thread():
    global console_o
    console_o = True
    while True:
        ipt = input('~} ').split(" ")
        retour = run(ipt)
        if retour == None: os.system('cls' if os.name == 'nt' else 'clear')
        elif retour == "exit": console_o = False ; break
        else: print(retour)

### commandes
def run(ipt):
    if ipt[0] == "": pass                                   # commande vide
    elif ipt[0] == "version": return(version())             # version
    elif ipt[0] == "path": return(path())                   # path
    elif ipt[0] == "mkdir":                                 # mkdir
        try: return(mkdir(ipt[1], ipt[2]))
        except: return("erreur: 'chem rela + nom'") 
    elif ipt[0] == "wget":                                  # wget
        try: return(wget(ipt[1], ipt[2], ipt[3]))
        except: return("erreur: 'chem rela + nom + addr'")
    elif ipt[0] == "mkfil":                                 # mkfil
        try: return(mkfil(ipt[1], ipt[2], ipt[3]))
        except: return("erreur: 'chem rela + nom + text'")
    elif ipt[0] == "ls":                                    # ls
        try: return(ls(ipt[1]))
        except: return("erreur: 'chem rela'")
    elif ipt[0] == "rfil":                                  # rfil
        try: return(rfil_rela(ipt[1], ipt[2]))
        except: return("erreur: 'nom'")
    elif ipt[0] == "exit":                                  # exit
        return("exit")
    elif ipt[0] == "aide" or ipt[0] == "help":              # aide
        return("version > affiche la version\npath    > affiche le chemain\nmkdir   > crée un dossier\nls      > affiche le contenue d'un dossier\nwget    > crée un fichier depuis le web\nmkfil   > créé un fichier\nrfil    > affiche le contenue d'un fichier\nhelp    > affiche l'aide")
    else: return("commande inconnu")                        # autres commandes