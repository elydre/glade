'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
.codé en : UTF-8
.langage : python 3
.v       : 0.0.11
--|~|--|~|--|~|--|~|--|~|--|~|--
'''
import mod.cytron as cy
import mod.ColorPrint as cprint

class sys:
    def info(msg):
        cprint.colorprint("|end| ",color=cprint.Colors.cyan,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

    def gen_err(msg):
        cprint.colorprint("|err| ",color=cprint.Colors.rouge,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

class init:
    def lsprog():
        cprint.colorprint("\nWhich program to convert: ",color=cprint.Colors.blanc)
        ls_liste = cy.ls("/container")
        for element in ls_liste:
            ext = element.split(".")[len(element.split("."))-1]
            cprint.colorprint(" ",color=cprint.Colors.none,end=False)
            if ext == "py": cprint.colorprint(element,color=cprint.Colors.bleu)
            elif ext == "txt": cprint.colorprint(element,color=cprint.Colors.jaune)
            elif ext == "gld": cprint.colorprint(element,color=cprint.Colors.vert)
            elif ext == "cpp": cprint.colorprint(element,color=cprint.Colors.magenta)
            else: cprint.colorprint(element,color=cprint.Colors.blanc)
        return(input("~} "))

    def main():
        global todo
        no_done = True
        while no_done:
            todo = init.lsprog()
            if cy.rfil_rela("/container",todo) != None: no_done = False
            else: sys.gen_err("non-existent or unreadable file")

class maker:
    def main():
        name = str(todo.split(".")[len(todo.split("."))-2]) + ".cpp"
        cy.mkfil("/container",name,"".join((l+"\n") for l in EXIT))

class compiler:

    def tab_c(l):
        t = 0
        nb_tab = 4 #number of spaces in a tablature
        while l.startswith(" "*t): t += nb_tab
        return(int((t - nb_tab)/nb_tab))

    def del_tab(l):
        sortie = ""
        for x in range(len(list(l))):
            if list(l)[x] != " ": break
        for y in range(x,len(list(l))): sortie += list(l)[y]
        return(sortie)
        
    def add_tab(nb):
        return(" "*TAB[nb]*4)

    def edit_l(l,nb):

        l = str(l)

        TAB.append(compiler.tab_c(l))

        l = compiler.del_tab(l)

        for loop in range(TAB[nb-1]-TAB[nb]): EXIT.append(compiler.add_tab(nb) + "}")

        if l.startswith("if "):
            cont = l.split("if ")[1]                        #we remove the 'if '
            cont = cont.split(":")[len(cont.split(":"))-2]  #we remove the ':'
            EXIT.append(compiler.add_tab(nb) + "if (" + cont + ")")
            EXIT.append(compiler.add_tab(nb) + "{")

        elif l.startswith("while "):
            cont = l.split("while ")[1]                     #we remove the 'while '
            cont = cont.split(":")[len(cont.split(":"))-2]  #we remove the ':'
            EXIT.append(compiler.add_tab(nb) + "while (" + cont + ")")
            EXIT.append(compiler.add_tab(nb) + "{")

        elif l.startswith("def "):
            cont = l.split("def ")[1]                       #we remove the 'while '
            cont = cont.split(":")[len(cont.split(":"))-2]  #we remove the ':'
            EXIT.append(compiler.add_tab(nb) + "int " + cont)
            EXIT.append(compiler.add_tab(nb) + "{")

        else:
            EXIT.append(compiler.add_tab(nb) + l + ";")


    def main():
        fichier = cy.rfil_rela("/container",todo)
        ligues = fichier.split("\n")

        global EXIT, TAB
        EXIT = [] # list of 'compiled' code
        TAB = []  # list of TAB

        for nb in range(len(ligues)):
            l = ligues[nb]
            compiler.edit_l(l,nb)

        


init.main()
sys.info("initialization")
compiler.main()
sys.info("compilation")
maker.main()
sys.info("writing")