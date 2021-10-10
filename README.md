# GLADE

![](https://zupimages.net/up/21/39/i59m.png)

GLADE est un compilateur python vers c++ pour accéléré grandement la vitesse du python tout en gardant sa syntaxe.\
fonctionne avec [cytron](https://github.com/pf4-DEV/cytron) et [colorprint](https://github.com/pf4-DEV/Color-Printer).

# Compilation

## Syntaxe particulière
- ***`#!`* ligne brute:** le texte à la suite de cette marque ne serra par interprété et serra laissé brut jusqu'a la fin de la ligne

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

# Paramètres
Les paramètres sont éditables depuis le fichier ***system/settings.txt***\
les valeurs entre parenthèse à la fin de chaque description correspond au valeur par défaut.

- **todo**: fichier compilé par défaut *None* pour auqun ou nom du fichier. (*t.py*)
- **space in tabs**: nombre d'espaces dans une tablature. (*4*)
- **debug print**: *True* pour les print de debug *False* pour désactiver. (*False*)
- **make log**: *True* pour les logs automatiques *False* pour désactiver. (*True*)
- **loop compil**: *True* pour compiler en boucle *False* pour désactiver. (*False*)
- **auto main**: *True* pour la création de la fonction main automatique *False* pour désactiver. (*True*)
- **init var**: *True* pour l'initialisation des variables *False* pour désactiver. (*True*)
- **auto include**: *True* pour les include automatiques *False* pour désactiver. (*True*)
- **int var type**: Type de variable pour les entier. *int* (8bit) pour un programme légé vers *long long int* (64bit) pour des variables gigantesques. [en savoir plus](https://fr.wikipedia.org/wiki/Types_de_donnée_du_langage_C)

# Avancement du compilateur
## Éléments pris en charge

- importation *`include`*
- *`print()`*
- fonction
- *`return()`*
- boucle *`while`* / *`for`*
- *`if`* / *`elif`* / *`else`*
- commentaires *(de # à //)*
- code brut
- auto initialisation avec type de variable
- auto main
- input avec type de variable auto
- traitement des variables: *`True`* -> *`true`*
- str

## Éléments en développement

- try
- liste
- traitement des operation: *`**`* -> *`pow()`*

## Éléments a venir

- interpretation une ligne:<br>
    *`print('non' if test = False else "oui")`*
- module
- classe & programmation acces objet
- typage dynamique

# auteurs

- pf4 ([@pf4-DEV](https://github.com/pf4-DEV))
- Loris ([@Lorisredstone](https://github.com/Lorisredstone))