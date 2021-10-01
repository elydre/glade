# GLADE
GLADE est un compilateur python vers c++ pour accéléré grandement la vitesse du python tout en gardant sa syntaxe\
fonctionne avec [cytron](https://github.com/pf4-DEV/cytron) et [colorprint](https://github.com/pf4-DEV/sun-breaker).

## Élément pris en charge

 - importation `include`
 - `print`
 - fonction
 - `return`
 - boucle `while` / `for`
 - `if` / `elif` / `else`
 - commentaires *(de # à //)*
 - code brut
 - auto initialisation avec type de variable

## Éléments en développement

 - traitement des variables `True` -> `true`...
 - auto main
 - liste
 - classe
 - str *?*

## Syntaxe particulière
-  ***`#!`* ligne brute:** le texte de cette ligne a la suite de cette marque ne serra par interprété et serra laissé brut