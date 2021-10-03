# GLADE

![](https://zupimages.net/up/21/39/i59m.png)

GLADE est un compilateur python vers c++ pour accéléré grandement la vitesse du python tout en gardant sa syntaxe.\
fonctionne avec [cytron](https://github.com/pf4-DEV/cytron) et [colorprint](https://github.com/pf4-DEV/Color-Printer).

## Syntaxe particulière
- ***`#!`* ligne brute:** le texte de cette ligne a la suite de cette marque ne serra par interprété et serra laissé brut

## Paramètres
les paramètres sont éditable depuis le fichier ***system/settings.txt***
- **todo**: fichier compilé par défaut *None* pour auqun ou nom du fichier
- **space in tabs**: nombre d'espace dans une tablature, par défaut 4
- **debug print**: *True* pour les print de debug *False* pour désactiver
- **auto main**: *True* pour la création de la fonction main automatique *False* pour désactiver
- **init var**: *True* pour l'initialisation des variables' *False* pour désactiver
- **auto include**: *True* pour les include automatiques *False* pour désactiver

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