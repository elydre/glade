from cytron import *
from sunbreaker import sunbreaker

global sort, car, tp

name = input("nom de la basse de donné a créé: ")
max_long = int(input("longeur max des mots: "))

car = list("-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,;:!?./*$%&'(_)=+<> ")
cy_mkfil("/",name,"")
sort = [""]
tp = ""
dp = 0
long = 0

def save():
    global tp
    temp = cy_rfil_rela("/",name) + tp
    cy_mkfil("/",name,temp)
    tp = ""

def voc(b):
    global long
    long = b
    try:
        if sort[b] == "coucou": pass
    except:
        print(b,"depassé")
        sort.insert(0,"a")

def acr():
    done = False
    for b in range(len(sort)+1):
        voc(b)
        for a in range(len(car)):
            if sort[b] == car[a]:
                try:
                    sort[b] = car[a+1]
                    done = True
                    break
                except:
                    sort[b] = car[0]
                    break
        if done: break

    
while long <= max_long:
    acr()
    test=""
    for a in sort: test += a
    tp += str(sunbreaker(test)) + "\n" + str(test) + "\n"
    dp += 1
    if dp == 1000:
        save()
        dp = 0

save()
input("fin ^^")