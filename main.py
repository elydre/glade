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
.v       : 0.0.9
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
        nb = 4 #number of spaces in a tablature
        while l.startswith(" "*t): t += nb
        return(int((t - nb)/nb))

    def edit_l(l):

        l = str(l)

        print(compiler.tab_c(l))

        if l.startswith("if "):
            cont = l.split("if ")[1] #we remove the 'if '
            cont = cont.split(":")[len(cont.split(":"))-2] #we remove the ':'
            EXIT.append("if (" + cont + ")")
            EXIT.append("{")


    def main():
        fichier = cy.rfil_rela("/container",todo)
        ligues = fichier.split("\n")

        global EXIT, COMP
        EXIT = [] # list of 'compiled' code
        COMP = [] # list of structure

        for l in ligues:
            compiler.edit_l(l)
        


init.main()
sys.info("initialization")
compiler.main()
sys.info("compilation")
maker.main()
sys.info("writing")