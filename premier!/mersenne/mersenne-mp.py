from multiprocessing import Pool

def mers(entree):   #fonction de Loris_redsrone pour touvé les nombres de mersenne
    nombre_s = entree - 2
    mers_entree = ( 2 ** entree ) - 1
    s = 4
    for i in range(nombre_s):
        s = ( ( s ** 2 ) - 2 ) % mers_entree
    if s == 0:
        print("2^", entree, "-1 est premier")


if __name__ == '__main__':
    nbc = int(input("entrez le nombre de pool (conseillé comme le nombre de thread sur votre machine)\n-> "))
    a = int(input("entrez x pour rechercher tout les nombres de 2^0 a 2^x\n-> "))

    #liste des nombre a calculé en mp
    ac = []
    for x in range(a):
        ac.append(x)    #on ajoute 1 a 1 tout les nombre

    with Pool(nbc) as p:  # on lance sur 
        liste2 = (p.map(mers, ac))