from sunbreaker import sunbreaker

def verif(tc):
    global find
    if sunbreaker(tc) == tf:
        print("\ntrouvé! -> "+str(tc))
        find = True

def voc(b):
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

def init():
    while True:
        global sort, car, tf, find

        while True:
            try:
                tf = int(input("\nquel break voulez vous trouver -> "))
                break
            except: print(" c'est pas un nombre!\n")
        
        doprint = input("\nvoulez vous les prints [ o / n ] -> ")

        while True:
            temp = input("\nquel jeu de caractère voulez vous [ s (simple) / l (lourd) / c (custom) ] -> ")
            if temp == "s":
                car = list("-abcdefghijklmnopqrstuvwxyz0123456789")
                break
            elif temp == "l":
                car = list("-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,;:!?./§ù*$%µ£&é'(è_çà)=+<> ")
                break
            elif temp == "c":
                car = "-" + input("rentez les caractères que vous voulez utilisé -> ")
                break
            else:
                print("entré inconue")

        sort = [""]
        find = False
    
        while find == False:
            acr()
            test=""
            for a in sort: test += a
            if doprint == "o":
                print(test)
            verif(test)

init()