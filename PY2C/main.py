import mod.cytron as cy
import mod.ColorPrint as cprint

class init:
    def lsprog():
        cprint.colorprint("quel programme voullez vous convertir: ",color=cprint.Colors.blanc)
        ls_liste = cy.ls("/conteneur")
        for element in ls_liste:
            ext = element.split(".")[len(element.split("."))-1]
            if ext == "py": cprint.colorprint(element,color=cprint.Colors.bleu,end=False)
            elif ext == "txt": cprint.colorprint(element,color=cprint.Colors.jaune,end=False)
            elif ext == "cpp": cprint.colorprint(element,color=cprint.Colors.rouge,end=False)
            else: cprint.colorprint(element,color=cprint.Colors.blanc,end=False)
            cprint.colorprint("  ",color=cprint.Colors.none,end=False)
        return(input("~} "))

init.lsprog()