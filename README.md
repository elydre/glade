# GLADE

![](https://zupimages.net/up/21/39/i59m.png)

GLADE est un compilateur python vers c++ pour accéléré grandement la vitesse du python tout en gardant sa syntaxe.\
fonctionne avec [cytron](https://github.com/pf4-DEV/cytron) et [colorprint](https://github.com/pf4-DEV/Color-Printer).

## Syntaxe particulière
- ***`#!`* ligne brute:** le texte de cette ligne a la suite de cette marque ne serra par interprété et serra laissé brut

## Paramètres
les paramètres sont éditable depuis le fichier ***system/settings.txt***<br>
les valeur entre parenthèse a la fin de chaque description correspond au valeur par défaut.

- **todo**: fichier compilé par défaut *None* pour auqun ou nom du fichier. (*t.py*)
- **space in tabs**: nombre d'espace dans une tablature. (*4*)
- **debug print**: *True* pour les print de debug *False* pour désactiver. (*True*)
- **auto main**: *True* pour la création de la fonction main automatique *False* pour désactiver. (*True*)
- **init var**: *True* pour l'initialisation des variables *False* pour désactiver. (*True*)
- **auto include**: *True* pour les include automatiques *False* pour désactiver. (*True*)
- **int var type**: Type de variable pour les entier. *int* (8bit) pour un programme légé vers *long long int* (64bit) pour des variables gigantesques. [en savoir plus](https://fr.wikipedia.org/wiki/Types_de_donnée_du_langage_C)

## Élément pris en charge

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

## Éléments en développement

- try
- traitement des variables: *`True`* -> *`true`*
- liste

## Éléments a venir

- interpretation une ligne:<br>
    *`print('non' if test = False else "oui")`*
- traitement des operation: *`**`* -> *`pow()`*
- str *?*
- classe & programmation acces objet