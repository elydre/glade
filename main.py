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
 - v       : 0.2.1b
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

import sys.mod.cytron as cy
import sys.mod.ColorPrint as cprint

class init:
    #### parametres ####
    global todo

    # fichier a compiler par defaut (None)
    todo = None

    # print de debug (True)
    debug_print = True

    # espace dans une tablature python (4)
    space_in_tabs = 4

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

class inter:
    def lsprog(defaut):
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
        if defaut == None or defaut == "":
            return(input("~} "))
        else:
            cprint.colorprint("(",color=cprint.Colors.blanc, end=False)
            cprint.colorprint(defaut,color=cprint.Colors.cyan, end=False)
            cprint.colorprint(")",color=cprint.Colors.blanc, end=False)
            ipt = input(" ~} ")
            return(defaut if ipt == "" else ipt)
             

    def main():
        global todo
        no_done = True
        while no_done:
            todo = inter.lsprog(todo)
            if cy.rfil_rela("/container",todo) != None: no_done = False
            else: sys.gen_err("non-existent or unreadable file")

class teyes:

    def varitype(var,cont):
        if len(cont.split('"')) > 1 or len(cont.split("'")) > 1:
            typ = "string"
            int_val = '""'
        elif cont == "True" or cont == "False":
            typ = "bool"
            int_val = "false"
        else:
            try:
                int(cont)
                typ = "long int"
                int_val = 0
            except:
                try:
                    float(cont)
                    typ = "float"
                    int_val = 0.0
                except:
                    typ = "long int"
                    int_val = 0
        return([var,typ,int_val])

    def edit_l(l,nb,len_tot):
        global ATOC
        def tab_c(l):
            t = 0
            while l.startswith(" "*t): t += init.space_in_tabs
            return(int((t - init.space_in_tabs)/init.space_in_tabs))

        def del_end(cont,to_del):
            cont , to_del = str(cont) , str(to_del)
            return(cont.split(to_del)[len(cont.split(to_del))-2])

        def contient(var,cont):
            cont, var = str(cont), str(var)
            return(len(var.split(cont))-1)

        l = str(l)

        TAB.append(tab_c(l))

        l = l.strip()

        if l != "" or nb == len_tot-1:
            for loop in range(1,TAB[nb-1]-TAB[nb]+1):
                temp = ""
                for a in range(len(ATOC.split("/"))-1):
                    if a != 0: temp += "/" + ATOC.split("/")[a]
                ATOC = temp
                EYES.append([ATOC,TAB[nb-1]-1*loop,"}"])
                
                
        
        if nb == 0:
            EYES.append([ATOC,TAB[nb],"comm","interpreted and compiled by GLADE"])

        if l.startswith("if "):
            cont = l.split("if ")[1]
            cont = del_end(cont,":")
            EYES.append([ATOC,TAB[nb],"if",cont])
            EYES.append([ATOC,TAB[nb],"{"])
            ATOC += "/if"

        elif l.startswith("elif "):
            cont = l.split("elif ")[1]
            cont = del_end(cont,":")
            EYES.append([ATOC,TAB[nb],"elif",cont])
            EYES.append([ATOC,TAB[nb],"{"])
            ATOC += "/elif"

        elif l.startswith("else "):
            cont = l.split("else ")[1]
            cont = del_end(cont,":")
            EYES.append([ATOC,TAB[nb],"else",cont])
            EYES.append([ATOC,TAB[nb],"{"])
            ATOC += "/else"

        elif l.startswith("while "):
            cont = l.split("while ")[1]
            cont = del_end(cont,":")
            EYES.append([ATOC,TAB[nb],"while",cont])
            EYES.append([ATOC,TAB[nb],"{"])
            ATOC += "/while"

        elif l.startswith("def "):
            cont = l.split("def ")[1]
            cont = del_end(cont,":")
            EYES.append([ATOC,TAB[nb],"def",cont])
            EYES.append([ATOC,TAB[nb],"{"])
            ATOC += "/" + cont.split("(")[0]

        elif l.startswith("for "):
            cont = l.split("for ")[1]
            cont = del_end(cont,"):")
            var_name = cont.split(" in range(")[0]
            arg = cont.split(" in range(")[1].split(",")
            pas , min , max = "1", "0", "0"
            if len(arg) == 1:
                max = arg[0]
            elif len(arg) >= 2:
                min = arg[0]
                max = arg[1]
            elif len(arg) == 3:
                pas = arg[2]

            EYES.append([ATOC,TAB[nb],"for",[var_name,min,max,pas]])
            EYES.append([ATOC,TAB[nb],"{"])
            ATOC += "/for"

        elif l.startswith("print("):
            cont = l.split("print(")[1]
            cont = del_end(cont,")")
            EYES.append([ATOC,TAB[nb],"print",cont])

        elif l.startswith("return("):
            cont = l.split("return(")[1]
            cont = del_end(cont,")")
            EYES.append([ATOC,TAB[nb],"return",cont])

        elif l.startswith("#"):
            lb = l.split("#")[1].strip()
            if lb.startswith("include "):
                cont = lb.split("include ")[1]
                EYES.append([ATOC,TAB[nb],"include",cont])
            elif lb.startswith("!"):
                cont = lb.split("!")[1].strip()
                EYES.append([ATOC,TAB[nb],"lnb",cont])
            else:
                EYES.append([ATOC,TAB[nb],"comm",lb])

        elif contient(l,"=") == 1:
            nom = l.split("=")[0].strip()
            cont = l.split("=")[1].strip()
            EYES.append([ATOC,TAB[nb],"vare",[nom,cont]])
            VAR.append([("" if len(ATOC.split("/")) == 0 else "/" + ATOC.split("/")[1]),nom,cont])

        elif l.strip() != "":
            EYES.append([ATOC,TAB[nb],"unknown",l])

    def main():
        pprint = False
        fichier = cy.rfil_rela("/container",todo)
        ligues = fichier.split("\n")
        ligues.append("")
        global EYES, TAB, VAR, ATOC
        EYES = [] # liste de code token eyes
        VAR = []  # liste des variables
        TAB = []  # liste des TAB
        ATOC = ""

        for nb in range(len(ligues)):
            l = ligues[nb]
            teyes.edit_l(l,nb,len(ligues))

        # relecture pour auto créé les variables
        for iv in range(len(VAR)):
            v = VAR[iv]
            for ie in range(len(EYES)):
                e = EYES[ie]
                if e[0] == v[0]:
                    EYES.insert(ie+iv,[str(e[0]),1, "vari", teyes.varitype(v[1],v[2])])
                    break
        
        # relecture pour l'importation des modules
        for e in EYES:
            if e[2] == "print" and pprint == False:
                sys.app("importation de print automatique")
                EYES.insert(1,['',0, "include", "<iostream>"])
                EYES.insert(2,['',0, 'unknown', 'using namespace std'])
                pprint = True
    
        # print (dev)
        if init.debug_print:
            sys.app("liste des variables: " + str(VAR))
            for e in EYES:
                sys.dev(str(e))

class compiler:
    def edit_e(e):
        def add_tab(tab): return(" "*tab*init.space_in_tabs)
        
        de = e[2]  #element detecte
        tab = e[1] #nb de tab
        try: arg = e[3] #arg
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
        
        elif de == "elif":
            EXIT.append(add_tab(tab) + "else if (" + arg + ")")

        elif de == "else":
            EXIT.append(add_tab(tab) + "else (" + arg + ")")

        elif de == "return":
            EXIT.append(add_tab(tab) + "return " + arg + ";")

        elif de == "print":
            EXIT.append(add_tab(tab) + "cout << " + arg + " << endl;" )

        elif de == "include":
            EXIT.append(add_tab(tab) + "#include " + arg)

        elif de == "lnb":
            EXIT.append(add_tab(tab) + arg)

        elif de == "comm":
            EXIT.append(add_tab(tab) + "// " + arg)

        elif de == "vare":
            EXIT.append(add_tab(tab) + arg[0] + " = " + arg[1] + ";")

        elif de == "vari":
            EXIT.append(add_tab(tab) + arg[1] + " " + arg[0] + " = " + str(arg[2]) + ";  // auto var")

        elif de == "unknown":
            EXIT.append(add_tab(tab) + arg + ";")

        elif de == "{":
            EXIT.append(add_tab(tab) + "{")

        elif de == "}":
            EXIT.append(add_tab(tab) + "}")

        else:
            sys.gen_err("élément retourné inconnu par le compilateur: '" + de + "'\n      ici -> " + str(e))

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
init()

while True:
    inter.main()
    sys.info("token eyes")
    teyes.main()
    sys.info("compilation")
    compiler.main()
    sys.info("writing")
    maker.main()