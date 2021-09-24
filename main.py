'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
 - codé en : UTF-8
 - langage : python 3
 - v       : 0.1.6
--|~|--|~|--|~|--|~|--|~|--|~|--
'''
import mod.cytron as cy
import mod.ColorPrint as cprint

class sys:
    def info(msg):
        cprint.colorprint("|sys| ",color=cprint.Colors.cyan,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

    def dev(msg):
        cprint.colorprint("|dev| ",color=cprint.Colors.vert,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

    def app(msg):
        cprint.colorprint("|app| ",color=cprint.Colors.jaune,end=False)
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

class teyes:

    def var_type(cont):
        return(type(cont))


    def edit_l(l,nb):
        def tab_c(l):
            t = 0
            nb_tab = 4 #nombre d'espace dans une TAB
            while l.startswith(" "*t): t += nb_tab
            return(int((t - nb_tab)/nb_tab))

        def del_tab(l):
            sortie = ""
            x = 0       #si la ligne est vide
            for x in range(len(list(l))):
                if list(l)[x] != " ": break
            for y in range(x,len(list(l))): sortie += list(l)[y]
            return(sortie)

        def del_end(cont,to_del):
            cont , to_del = str(cont) , str(to_del)
            return(cont.split(to_del)[len(cont.split(to_del))-2])

        l = str(l)

        TAB.append(tab_c(l))

        l = del_tab(l)

        for loop in range(1,TAB[nb-1]-TAB[nb]+1): EYES.append([TAB[nb-1]-1*loop,"}"])
        
        if nb == 0:
            EYES.append([TAB[nb],"comm","interpreted and compiled by GLADE"])

        if l.startswith("if "):
            cont = l.split("if ")[1]
            cont = del_end(cont,":")
            EYES.append([TAB[nb],"if",cont])
            EYES.append([TAB[nb],"{"])

        elif l.startswith("while "):
            cont = l.split("while ")[1]
            cont = del_end(cont,":")
            EYES.append([TAB[nb],"while",cont])
            EYES.append([TAB[nb],"{"])

        elif l.startswith("def "):
            cont = l.split("def ")[1]
            cont = del_end(cont,":")
            EYES.append([TAB[nb],"def",cont])
            EYES.append([TAB[nb],"{"])

        elif l.startswith("for "):
            cont = l.split("for ")[1]
            cont = del_end(cont,"):")
            var_name = cont.split(" in range(")[0]
            arg = cont = cont.split(" in range(")[1].split(",")
            pas , min , max = "1", "0", "0"
            if len(arg) == 1:
                max = arg[0]
            elif len(arg) >= 2:
                min = arg[0]
                max = arg[1]
            elif len(arg) == 3:
                pas = arg[2]

            EYES.append([TAB[nb],"for",[var_name,min,max,pas]])
            EYES.append([TAB[nb],"{"])

        elif l.startswith("print("):
            cont = l.split("print(")[1]
            cont = del_end(cont,")")
            EYES.append([TAB[nb],"print",cont])

        elif l.startswith("return("):
            cont = l.split("return(")[1]
            cont = del_end(cont,")")
            EYES.append([TAB[nb],"return",cont])

        elif l.startswith("#include "):
            cont = l.split("#include ")[1]
            EYES.append([TAB[nb],"include",cont])

        elif l != "":
            EYES.append([TAB[nb],"unknown",l])

    def main():
        pprint = False
        fichier = cy.rfil_rela("/container",todo)
        ligues = fichier.split("\n")
        ligues.append("")
        global EYES, TAB
        EYES = [] # liste de code token eyes
        TAB = []  # liste des TAB

        for nb in range(len(ligues)):
            l = ligues[nb]
            teyes.edit_l(l,nb)
        
        # relecture
        for e in EYES:
            if e[1] == "print" and pprint == False:
                sys.dev("importation de print automatique")
                EYES.insert(1,[0, "include", "<iostream>"])
                EYES.insert(2,[0, 'unknown', 'using namespace std'])
                pprint = True

    
        # print (dev)
        for e in EYES:
            sys.app(str(e))

class compiler:
    def edit_e(e):
        def add_tab(tab): return(" "*tab*4)
        
        de = e[1]  #element detecte
        tab = e[0] #nb de tab
        try: arg = e[2] #arg
        except: arg = None

        if de == "def":
            EXIT.append(add_tab(tab) + "int " + arg)

        elif de == "while":
            EXIT.append(add_tab(tab) + "while (" + arg + ")")

        elif de == "for":
            larg = arg
            arg = "long int " + larg[0] + " = " + larg[1] + "; " + larg[0] + " <= " + larg[2] + "; " + larg[0] + " = " + larg[0] + " + " + larg[3]
            EXIT.append(add_tab(tab) + "for (" + arg + ")")

        elif de == "if":
            EXIT.append(add_tab(tab) + "if (" + arg + ")")

        elif de == "print":
            EXIT.append(add_tab(tab) + "cout << " + arg + " << endl;" )

        elif de == "include":
            EXIT.append(add_tab(tab) + "#include " + arg)

        elif de == "return":
            EXIT.append(add_tab(tab) + "return " + arg + ";")

        elif de == "comm":
            EXIT.append(add_tab(tab) + "// " + arg)

        elif de == "unknown":
            EXIT.append(add_tab(tab) + arg + ";")

        elif de == "{":
            EXIT.append(add_tab(tab) + "{")

        elif de == "}":
            EXIT.append(add_tab(tab) + "}")

        else:
            sys.gen_err("élément retourné inconnu par le compilateur: " + de)

    def main():
        global EXIT
        EXIT = []

        for e in EYES:
            compiler.edit_e(e)

class maker:
    def main():
        name = str(todo.split(".")[len(todo.split("."))-2]) + ".cpp"
        cy.mkfil("/container",name,"".join((l+"\n") for l in EXIT))

sys.info("initialization")
init.main()

sys.info("token eyes")
teyes.main()

sys.info("compilation")
compiler.main()

sys.info("writing")
maker.main()