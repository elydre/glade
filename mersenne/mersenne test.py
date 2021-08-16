liste1 = []
a = int(input("merci d entrer x pour rechercher tout les nombres de 2^0 a 2^x (ne pas trop abuser :) )>>> "))

for x in range(a):
    entree = x
    nombre_s = entree - 2
    mers_entree = ( 2 ** entree ) - 1
    s = 4
    for i in range(nombre_s):
        s = ( ( s ** 2 ) - 2 ) % mers_entree
    if s == 0:
        print("2 ^", entree, "-1 est premier")
        liste1.append(entree)
    else:
        print("2 ^", entree, "-1 est non premier")

print(liste1, "premiers")
print("2^", liste1[len(liste1) - 1] ,"-1  est le plus grand nombre premier trouvé par le programme")