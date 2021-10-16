import sys, os
from urllib.request import urlopen

path = os.path.dirname(sys.argv[0])

def mkdir(path,l):
    for e in l:
        try:
            print(f"création {e}")
            os.makedirs(path+e)
        except FileExistsError:
            print("le dossier est déjà existant")
def dl(path,n,a):
    for x in range(len(n)):
        print(f"téléchargement de {n[x]}")
        with open(path + n[x], 'wb') as img:
            img.write(urlopen(a[x]).read())

def done():
    mkdir(path,["/container","/system","/system/glade","/system/mod"])
    dl(path,["/main.py","/system/glade/Compiler.py","/system/glade/Tools.py","/system/mod/Cytron.py","/system/mod/ColorPrint.py","/system/settings.txt","/container/t.py"],["https://raw.githubusercontent.com/pf4-DEV/glade/main/main.py","https://raw.githubusercontent.com/pf4-DEV/glade/main/system/glade/Compiler.py","https://raw.githubusercontent.com/pf4-DEV/glade/main/system/glade/Tools.py","https://raw.githubusercontent.com/pf4-DEV/cytron/main/cytron.py","https://raw.githubusercontent.com/pf4-DEV/Color-Printer/main/ColorPrint.py","https://raw.githubusercontent.com/pf4-DEV/glade/main/system/settings.txt","https://raw.githubusercontent.com/pf4-DEV/glade/main/container/t.py"])



try:
    urlopen("https://google.com")
    done()
    print("Glade téléchargé avec succes")

except: print("pas de connection internet")