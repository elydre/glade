#! bool True = true;
for x in range(0,50):
    print("")
print("   Bonjour et bienvenu sur TIP4")
print("   le terminal d’interprétation personnalisé de pf4 -")
while True:
    ipt = input("~} ")
    ###  INFO  ###
    if ipt == "info" or ipt == "INFO":
        print("   dev: PF4-")
        print("   run by PYTHON 3")
        print("")
    if ipt == "aide" or ipt == "AIDE":
        print("   aide:         affiche l’aide")
        print("   info:         affiche des infos")
        print("   erreur_liste: affiche la liste d’erreur")
        print("")
    if ipt == "erreur_liste" or ipt == "ERREUR_LISTE":
        print("   ERRUER 001 -> commande inconnu")
        print("")
    else:
        print("-ERREUR 001")
        print("-commande inconnu")