import time, random
from _thread import start_new_thread

def iptest():
    iptest_sc = 0
    iptest_debut = time.time()
    while time.time() - iptest_debut < 2: iptest_sc = iptest_sc + 1
    iptest_s = round(iptest_sc / 500000,1)
    return(iptest_s)

def addtest():
    stop = 0
    y = 0
    num = 0
    debut = time.time()
    while stop == 0:
        for x in range(0,10000): num = num + 1
        y = y + 1
        fin = time.time()
        temps = fin - debut
        if temps > 10: y = y / 100; stop = 1
    return(y)

def rdtest():
    fin = 0
    stop = 0
    y = 0
    debut = time.time()
    while stop == 0:
        for x in range(0,10000): num = random.randint(0, 1000000000)
        y = y + 1
        fin = time.time()
        temps = fin - debut
        if temps > 10:
            y = y / 100
            stop = 1
    return(y)

def bctest():
    y = 0
    debut = time.time()
    while y < 10000000: y = y + 1
    bcwhile = round(time.time() - debut,3)

    print("while: ", bcwhile, "s. les 10G boucles")

    debut = time.time()
    for y in range(10000000): pass
    bcfor = round(time.time() - debut,3)

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
    while thn != 0: time.sleep(0.05); pt -= 1
    return(pt)

def start():
    print("DEBUT DES TESTS")

    print(" ~~~~ ad test ~~~~ ")
    print("->", addtest(),"pts")

    print(" ~~~~ rd test ~~~~ ")
    print("->", rdtest(),"pts")

    print(" ~~~~ ip test ~~~~ ")
    print("->", iptest(),"pts")

    print(" ~~~~ th test ~~~~ ")
    print("->", thstart(),"pts")

    print(" ~~~~ bc test ~~~~ ")
    bctest()

    input("FIN DES TESTS")

start()