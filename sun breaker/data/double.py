from cytron import *
from time import time

fichier = None
try: cy_mkdir("/","data")
except: pass
cy_mkfil("/data","double.txt","")
cy_mkfil("/data","exploa.txt","")
name = "b2.txt"
debut = time()
print(round(time()-debut,1),"s - lecture...")
fichier = cy_rfil_rela("/",name)
print(round(time()-debut,1),"s - decoupage...")
lignes = str(fichier).split("\n")
print(round(time()-debut,1),"s - fin,",len(lignes),"lignes!")
print(round(time()-debut,1),"s - optimisation...")
fichier = "" #on gagne de la ram
print(round(time()-debut,1),"s - apprentisage...")
todo = []
for l in range(0,len(lignes)-1,2):
    todo.append(int(lignes[l]))
print(round(time()-debut,1),"s - fin,",len(todo),"break a tester!")

for l in todo:
    jam = 0
    for m in todo:
        if l == m: jam += 1      
    if jam > 1:
        cy_mkfil("/data","exploa.txt",cy_rfil_rela("/data","exploa.txt")+str(l)+";")
        cy_mkfil("/data","double.txt",cy_rfil_rela("/data","double.txt")+str(jam)+" - "+str(l)+"\n")
    print(l)