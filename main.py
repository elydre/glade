import mod.cytron as cy
import mod.ColorPrint as cprint

class init:
    def lsprog():
        cprint.colorprint("\nQuel programme voullez vous convertir: ",color=cprint.Colors.blanc)
        ls_liste = cy.ls("/conteneur")
        for element in ls_liste:
            ext = element.split(".")[len(element.split("."))-1]
            cprint.colorprint("  ",color=cprint.Colors.none,end=False)
            if ext == "py": cprint.colorprint(element,color=cprint.Colors.bleu,end=False)
            elif ext == "txt": cprint.colorprint(element,color=cprint.Colors.jaune,end=False)
            elif ext == "cpp": cprint.colorprint(element,color=cprint.Colors.magenta,end=False)
            else: cprint.colorprint(element,color=cprint.Colors.blanc,end=False)
        return(input("\n~} "))

    def main():
        global todo
        no_done = True
        while no_done:
            todo = init.lsprog()
            if cy.rfil_rela("/conteneur",todo) != None: no_done = False
            else: cprint.colorprint("ERREUR: fichier inexistant ou illisible",color=cprint.Colors.rouge)


class converter:
    def main():
        fichier = cy.rfil_rela("/conteneur",todo)
        ligues = fichier.split("\n")

        for l in ligues:
            
        
init.main()
converter.main()