from time import time

liste2 = []
debut = time()

for x in range(10000):
    liste2.append(x**84415)

r = 0
for n in liste2:
    r += n

tps = round(time()-debut,3)
print(n,"\nfait en",tps,"s")
input("fin")