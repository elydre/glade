import _thread

def mers(entree):
    nombre_s = entree - 2
    mers_entree = ( 2 ** entree ) - 1
    s = 4
    for i in range(nombre_s):
        s = ( ( s ** 2 ) - 2 ) % mers_entree
    if s == 0:
        print("2^", entree, "-1 est premier")

a = int(input("merci d entrer x pour rechercher tout les nombres de 2^0 a 2^x ~} "))
for loop in range(a):
    _thread.start_new_thread( mers,(loop, ))

while 1:
    pass