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
            elif ext == "gld": cprint.colorprint(element,color=cprint.Colors.vert,end=False)
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

class maker:
    def main():
        name = str(todo.split(".")[len(todo.split("."))-1]) + ".cpp"
        
        text = ""
        for l in EXIT: text += l
        
        cy.mkfil()

class converter:
    def edit_l(l):

        l = str(l)
        if l.startswith("if "):
            cont = l.split("if ")[1] #on enleve le 'if '
            cont = cont.split(":")[cont.split(":")-1] #on enleve le ':'
            EXIT.append("if(" + cont + ")")
            EXIT.append("{")


    def main():
        fichier = cy.rfil_rela("/conteneur",todo)
        ligues = fichier.split("\n")

        global EXIT
        EXIT = []

        for l in ligues:
            converter.edit_l(l)


init.main()
converter.main()
maker.main()