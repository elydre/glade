def mers(x):
    entree = x
    nombre_s = entree - 2
    mers_entree = ( 2 ** entree ) - 1
    s = 4
    for i in range(nombre_s):
        s = ( ( s ** 2 ) - 2 ) % mers_entree
    if s == 0:
        print("2 **", entree, "-1 est premier")
        liste1.append(entree)
    else:
        print("2 **", entree, "-1 est non premier", s )
        liste2.append(entree)

def main():
    def init():
        global liste1, liste2, temp, a
        liste1 = []
        liste2 = []
        temp = ""
        a = int(input("merci d entrer x pour rechercher tout les nombres de 2^0 a 2^x (ne pas trop abuser :) )>>> "))
    init()
    for loop in range(a):
        mers(loop)
    def end():
        print(liste2, "non premiers")
        print(liste1, "premiers")
        len_ = len(liste2)
        len2 = liste2[len_ - 1]
        print(2 ** len2 - 1, end = "")
        print(" est le plus grand nombre premier trouvé par le programme")

    end()
main()