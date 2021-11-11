# GLADE

![](https://zupimages.net/up/21/39/i59m.png)

GLADE est un compilateur python vers c++ pour accéléré grandement la vitesse du python tout en gardant sa syntaxe.\
fonctionne avec [cytron](https://github.com/pf4-DEV/cytron) et [colorprint](https://github.com/pf4-DEV/Color-Printer).

# Compilation

## Limitation

Glade supporte uniquement python3:
```py
print("coucou") # bien
print "coucou"  # mauvais
```
Il ne supporte pas le typage dynamique (une variable int doit rester int par exemple):
```py
a = 1
a = 4          # bien
a = "texte"    # mauvais
```
Il ne supporte pas les librairies python:
```py
import math    # mauvais
```

## Syntaxe particulière
#### *`#1!`* ligne blanche:
Le texte après cette marque serra interprété comme un commentaire par python mais normalement par glade
```py
#1! if i%2 != 0:
-GLADE->
if (i%2 != 0)
```
#### *`#2!`* ligne noire:
Le texte avant de cette marque ne serra par interprété et n'apparaîtra pas dans le fichier sortie
```py
max = int(i ** 0.5 + 1) #2!
-GLADE->

```
#### *`#3!`* ligne brute:
Le texte après cette marque ne serra par interprété et serra laissé brut
```py
#3! int myints[] = {16,2,77,29};
-GLADE->
int myints[] = {16,2,77,29};
```

## Paramètres
Les paramètres sont éditables depuis le fichier ***system/settings.txt***\
les valeurs entre parenthèses à la fin de chaque description correspond au valeur par défaut.

- **todo**: fichier compilé par défaut *None* pour auqun ou nom du fichier. (*t.py*)
- **space in tabs**: nombre d'espaces dans une tablature. (*4*)
- **debug print**: *True* pour les prints de debug *False* pour désactiver. (*False*)
- **sys print**: *True* pour les prints systeme *False* pour désactiver. (*True*)
- **make log**: *True* pour les logs automatiques *False* pour désactiver. (*True*)
- **loop compil**: *True* pour compiler en boucle *False* pour désactiver. (*False*)
- **auto main**: *True* pour la création de la fonction main automatique *False* pour désactiver. (*True*)
- **init var**: *True* pour l'initialisation des variables *False* pour désactiver. (*True*)
- **auto include**: *True* pour les includes automatiques *False* pour désactiver. (*True*)
- **int var type**: Type de variable pour les entiers. *int* (8bit) pour un programme légé vers *long long int* (64bit) pour des variables gigantesques. [en savoir plus](https://fr.wikipedia.org/wiki/Types_de_donnée_du_langage_C)

## Commandes

Les commandes sont accessibles dans la console de glade en tapent !{*commande*}. Les commandes disponibles sont les suivantes:
- **r**: recharge les paramètres
- **c**: clear la console
- **v**: affiche les versions des modules
- **e**: lance l'éditeur de paramètres

# Avancement du compilateur
## Éléments pris en charge

- importation *`include`*
- *`print()`*
- fonction
- *`return()`*
- boucle *`while`* / *`for`* + break
- *`if`* / *`elif`* / *`else`*
- commentaires *(de # à //)*
- code brut
- auto initialisation avec type de variable
- auto main
- input avec type de variable auto
- traitement des variables: *`True`* -> *`true`*
- gestion des str
- try / except
- pass

## Éléments en développement

Disponible sur [GitHub projet](https://github.com/users/pf4-DEV/projects/2)

## Historique des versions

### v0.5

|**TEyes** |Tools|Compiler|Statut|
|----------|-----|--------|------|
|...       |...  |...     |...   |

### v0.4

|**TEyes** |Tools|Compiler|Statut|
|----------|-----|--------|------|
|**0.4.9b**|0.10b|0.4     |[*stable*](https://github.com/pf4-DEV/glade/releases/tag/0.4.9b)|
|**0.4.9** |0.10 |0.3     |*dev* |
|**0.4.8b**|0.9  |0.3     |*dev* |
|**0.4.8** |0.9  |0.3     |*dev* |
|**0.4.7** |0.8  |0.2     |*dev* |
|**0.4.6** |0.6  |0.2     |*dev* |

# auteurs

- pf4 ([@pf4-DEV](https://github.com/pf4-DEV))
- Loris ([@Lorisredstone](https://github.com/Lorisredstone))