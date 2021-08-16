from multiprocessing import Pool
from time import time


liste = []
liste2 = []

debut = time()

for x in range(10000):
    liste.append(x)

def f(x):
    return x**84415

if __name__ == '__main__':
    nbc = int(input("entrez le nombre de pool (conseillé comme le nombre de thread sur votre machine)\n-> "))
    with Pool(nbc) as p:
        liste2 = (p.map(f, liste))
    r = 0
    for n in liste2:
        r += n

    tps = round(time()-debut,3)
    print(n,"\nfait en",tps,"s")
    input("fin")