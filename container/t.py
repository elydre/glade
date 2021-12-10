max = 11
f = 0
print("")
m = input("~} ")
try:
    m1 = m[0]
except:      
    m1 = ' '
try:
    m2 = m[1]
except:      
    m2 = ' '
try:
    m3 = m[2]
except:      
    m3 = ' '
f =  1
for idd in range(6):
    for ida in range(6):
        ia = ida
        ajout = idd
        caractere = m1
        code = caractere
        code = ajout + ajout
        n1 = code
        ajout =  ia
        ajout = min(ajout, max)
        caractere = m2
        code = caractere
        n2 = code
        ajout =  ia
        ajout = min(ajout, max)
        caractere = m3
        code = caractere
        n3 = code
        ajout =  ia
        ajout = min(ajout, max)
        print(f,end="")
        print(":","idd=",idd,"ida=",ia, n1,end="")
        print(n2,end="")
        print(n3)