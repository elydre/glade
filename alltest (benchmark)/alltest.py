from time import time, sleep
from random import randint
from _thread import start_new_thread
from multiprocessing import Pool
from os import cpu_count
from time import time

def mptestf(x):
    return x**15000

    

def iptest():
    iptest_sc = 0
    iptest_debut = time()
    while time() - iptest_debut < 2: iptest_sc = iptest_sc + 1
    iptest_s = round(iptest_sc / 500000,1)
    return(iptest_s)

def addtest():
    stop = 0
    y = 0
    num = 0
    debut = time()
    while stop == 0:
        for x in range(0,10000): num = num + 1
        y = y + 1
        fin = time()
        temps = fin - debut
        if temps > 10: y = y / 100; stop = 1
    return(y)

def rdtest():
    fin = 0
    stop = 0
    y = 0
    debut = time()
    while stop == 0:
        for x in range(0,10000): num = randint(0, 1000000000)
        y = y + 1
        fin = time()
        temps = fin - debut
        if temps > 10:
            y = y / 100
            stop = 1
    return(y)

def bctest():
    y = 0
    debut = time()
    while y < 10000000: y = y + 1
    bcwhile = round(time() - debut,3)

    print("while: ", bcwhile, "s. les 10G boucles")

    debut = time()
    for y in range(10000000): pass
    bcfor = round(time() - debut,3)

    print("for:   ", bcfor, "s. les 10G boucles")

def thstart():
    global thn
    thn = 10000

    def thtest(nb):
        global thn
        nb ** nb
        thn -= 1

    def thlauncher():
        for x in range(10000): start_new_thread(thtest,(x,))

    start_new_thread(thlauncher,())

    pt = 100
    while thn != 0: sleep(0.05); pt -= 1
    return(pt)

if __name__ == '__main__':
    print("DEBUT DES TESTS")

    print(" ~~~~ ad test ~~~~ ")
    print("->", addtest(),"pts")

    print(" ~~~~ rd test ~~~~ ")
    print("->", rdtest(),"pts")

    print(" ~~~~ ip test ~~~~ ")
    print("->", iptest(),"pts")

    print(" ~~~~ th test ~~~~ ")
    print("->", thstart(),"pts")

    print(" ~~~~ mp test ~~~~ ")

    liste = []
    liste2 = []
    debut = time()
    for x in range(10000): liste.append(x)
    with Pool(1) as p: liste2 = (p.map(mptestf, liste))

    print("1 core: ", round(time()-debut,3) , "s.")
    liste = []
    liste2 = []
    debut = time()
    for x in range(10000): liste.append(x)
    with Pool(cpu_count()) as p: liste2 = (p.map(mptestf, liste))
    print(cpu_count(),"core: ",round(time()-debut,3), "s.")

    print(" ~~~~ bc test ~~~~ ")
    bctest()

    input("FIN DES TESTS")