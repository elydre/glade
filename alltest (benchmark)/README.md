# <b>EXPLICATION DES TESTS</b>

### <b>ad test:</b>
<i>plus c’est haut mieux c’est!</i><br>
L’add test doit additionner le plus de nombres en partant de 0 en 10 sec.

### <b>rd test:</b>
<i>plus c’est haut mieux c’est!</i><br>
Le random test doit choisir le plus de nombres entre 0 et 109 en 10 sec.

### <b>ip test:</b>
<i>plus c’est haut mieux c’est!</i><br>
L’ip test et le test de performance d’I-python avec un principe similaire a d’ad test.

### <b>th test:</b>
<i>plus c’est haut mieux c’est!</i><br>
Le thread test mesure le niveau de performance de l’exécution des thread en en créant en grande quantité.

### <b>mp test:</b>
<i>plus c’est bas mieux c’est!</i><br>
Le multiprocessing test calcule la somme de tout les nombre de 0 a 1000015000 sur un nombre de cœur cpu donné, dans un première partie 1 seul puis sur tous

### <b>bc test:</b>
<i>plus c’est bas mieux c’est!</i><br>
Le test de boucle permet de comparé les nombre de seconde pour faire 10G boucle entre for et while

# <b>SCORES</b>
## <b>SYSTEME99: </b>x2 xeon 2670v3 (48@2.6GHz)
### <b>WINDOWS 10</b>
ad test: 164.91 pts <br>
rd test: 9.53 pts <br>
ip test: 26.1 pts <br>
th test: 76 pts <br>
mp test 1 core:  31.884 s. <br>
mp test 48 core:  1.805 s. <br>
bc test while:  0.565 s. les 10G boucles <br>
bc test for:    0.222 s. les 10G boucles <br>
### <b>WLS ubuntu</b>
ad test: 187.78 pts <br>
rd test: 10.88 pts <br>
ip test: 21.2 pts <br>
th test: 15 pts <br>
mp test 1 core:  24.463 s. <br>
mp test 48 core:  1.377 s. <br>
bc test while:  0.571 s. les 10G boucles <br>
bc test for:    0.220 s. les 10G boucles <br>
## <b>RPI4: </b>arm cortex a72 (4@1.5GHz)
### <b>UBUNTU aarch64</b>
ad test: 69.45 pts <br>
rd test: 4.02 pts <br>
ip test: 9.1 pts <br>
th test: 2 pts <br>
mp test 1 core:  50.080 s. <br>
mp test 4 core:  13.644 s. <br>
bc test while:  1.419 s. les 10G boucles <br>
bc test for:    0.561 s. les 10G boucles <br>
## <b>RPI3: </b>arm cortex a53 (4@1.4GHz)
### <b>RPI os</b>
ad test: 8.22 pts <br>
rd test: 0.47 pts <br>
ip test: 1.1 pts <br>
th test: -199 pts <br>
bc test while:  13.417 s. les 10G boucles <br>
bc test for:    4.666 s. les 10G boucles <br>
## <b>ROUGE: </b>celeron n4120 (4@2.5GHz)
### <b>KALI linux</b>
ad test: 147.34 pts <br>
rd test: 8.16 pts <br>
th test: 23 pts <br>
bc test while:  0.709 s. les 10G boucles <br>
bc test for:    0.300 s. les 10G boucles <br>