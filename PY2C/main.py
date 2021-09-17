import mod.cytron as cy
import mod.ColorPrint as cprint

cprint.colorprint("quel programme voullez vous convertir: ",color=cprint.Colors.blanc)
ls_liste = cy.ls("/conteneur")
for element in ls_liste:
    ext = element.split(".")[len(element.split("."))-1]
    if ext == "py": cprint.colorprint(element,color=cprint.Colors.bleu)
    elif ext == "txt": cprint.colorprint(element,color=cprint.Colors.jaune)
    elif ext == "cpp": cprint.colorprint(element,color=cprint.Colors.rouge)
    else: cprint.colorprint(element,color=cprint.Colors.blanc)