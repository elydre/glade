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
 - GitHub  : github.com/pf4-DEV/glade
 - v       : 0.3.3
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

import system.mod.cytron as cy
import system.mod.ColorPrint as cprint
from time import time


class psys:

    def timer(debut):
        return(round((time() - debut)*1000,1))

    def info(msg):
        cprint.colorprint("|sys| ",color=cprint.Colors.cyan,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

    def dev(msg):
        cprint.colorprint("|dev| ",color=cprint.Colors.vert,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

    def gen_err(msg):
        cprint.colorprint("|err| ",color=cprint.Colors.rouge,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

    def war(msg):
        cprint.colorprint("|war| ",color=cprint.Colors.magenta,end=False)
        cprint.colorprint(msg,color=cprint.Colors.blanc)

class init:
    def __init__(self):
        # valleur par defaut
        todo = None
        debug_print = True
        auto_main = True
        init_var = True
        auto_include = True
        make_log = True
        loop_compil = True
        space_in_tabs = 4
        int_var_type = "long int"

        para_edit = 0
        #lecture du fichier de paramètres
        if cy.rfil_rela("/system","settings.txt") == None: psys.war("fichier de paramètres non trouvé")
        else:
            for p in cy.rfil_rela("/system","settings.txt").split("\n"):
                if not(p.startswith("#")) and len(p.split("=")) > 1:
                    para_edit += 1
                    var = p.split("=")[0].strip()
                    atr = p.split("=")[1].strip()

                    if var == "todo":
                        if atr == "None": todo = None
                        else: todo = atr

                    elif var == "int var type":
                        int_var_type = atr

                    elif var == "debug print":
                        if atr == "False" or atr == "false": debug_print = False
                        elif atr == "True" or atr == "true": debug_print = True
                        else: psys.war("valleur non bool pour debug print (False par defaut)\n      ici -> " + str(atr))

                    elif var == "make log":
                        if atr == "False" or atr == "false": make_log = False
                        elif atr == "True" or atr == "true": make_log = True
                        else: psys.war("valleur non bool pour make log (True par defaut)\n      ici -> " + str(atr))

                    elif var == "init var":
                        if atr == "False" or atr == "false": init_var = False
                        elif atr == "True" or atr == "true": init_var = True
                        else: psys.war("valleur non bool pour init var (True par defaut)\n      ici -> " + str(atr))

                    elif var == "auto main":
                        if atr == "False" or atr == "false": auto_main = False
                        elif atr == "True" or atr == "true": auto_main = True
                        else: psys.war("valleur non bool pour auto main (True par defaut)\n      ici -> " + str(atr))

                    elif var == "loop compil":
                        if atr == "False" or atr == "false": loop_compil = False
                        elif atr == "True" or atr == "true": loop_compil = True
                        else: psys.war("valleur non bool pour loop compil (False par defaut)\n      ici -> " + str(atr))

                    elif var == "auto include":
                        if atr == "False" or atr == "false": auto_include = False
                        elif atr == "True" or atr == "true": auto_include = True
                        else: psys.war("valleur non bool pour auto include (True par defaut)\n      ici -> " + str(atr))
                    
                    elif var == "space in tabs":
                        try: space_in_tabs = int(atr)
                        except: psys.war("valleur non int pour space in tabs (4 par defaut)\n      ici -> " + str(atr))
                    
                    else:
                        para_edit -= 1
                        psys.gen_err("paramètres inconnu\n      ici -> " + str(p))

            psys.info(str(para_edit)+" paramètres édités")
            
        self.todo = todo
        self.debug_print = debug_print
        self.space_in_tabs = space_in_tabs
        self.auto_main = auto_main
        self.init_var = init_var
        self.auto_include = auto_include
        self.int_var_type = int_var_type
        self.make_log = make_log
        self.loop_compil = loop_compil

class inter:
    def lsprog(defaut):
        cprint.colorprint("\nQuel programme voulez vous compiler: ",color=cprint.Colors.blanc)
        ls_liste = cy.ls("/container")
        for element in ls_liste:
            ext = element.split(".")[len(element.split("."))-1]
            cprint.colorprint(" ",color=cprint.Colors.none,end=False)
            if ext == "py": cprint.colorprint(element,color=cprint.Colors.jaune)
            elif ext == "cpp": cprint.colorprint(element,color=cprint.Colors.vert)
            else: cprint.colorprint(element,color=cprint.Colors.blanc)
        print()
        if defaut == None or defaut == "":
            return(input("~} "))
        else:
            cprint.colorprint("(",color=cprint.Colors.blanc, end=False)
            cprint.colorprint(defaut,color=cprint.Colors.cyan, end=False)
            cprint.colorprint(")",color=cprint.Colors.blanc, end=False)
            ipt = input(" ~} ")
            return(defaut if ipt == "" else ipt)
             

    def main():
        global settings
        no_done = True
        while no_done:
            else: psys.gen_err("fichier non existent oui illisible")
            inp = inter.lsprog(settings.todo)
            if not(inp.startswith("!")):
                settings.todo = inp
                if cy.rfil_rela("/container",settings.todo) != None: no_done = False
                else: psys.gen_err("fichier non existent ou illisible")
            else:
                if inp == "!r":
                    settings = init()
                    psys.info("paramètres rechargé")

class teyes:
    
    def add_to_include(element):
            if not(element in to_include):
                to_include.append(element)
    
    def auto_main(liste):
        for ei in range(len(EYES)):
            e = EYES[ei]
            if e[1] == 0 and not(e[2] in liste):
                if settings.debug_print: psys.dev("création de la fonction main automatique")
                EYES.insert(ei,['', 0, 'def', 'main()'])
                EYES.insert(ei+1,['', 0, '{'])
                for ei2 in range(ei+2,len(EYES)):
                    e2 = EYES[ei2]
                    e2[0] = "/main" + e2[0]
                    e2[1] += 1
                EYES.append(['', 0, '}'])
                for v in VAR:
                    if v[0] == "":
                        v[0] = "/main"
                break

    def auto_include():
        for ti in to_include:
            if ti == "print":
                if settings.debug_print: psys.dev("importation de print automatique")
                EYES.insert(1,['',0, "include", "<iostream>"])
            elif ti == "std":
                if settings.debug_print: psys.dev("namespace std automatique")
                EYES.insert(1,['',0, "using", "namespace std;"])
            else:
                psys.gen_err(f"element a auto importer inconnu, ici -> {ti}")

    def init_var():
        def varitype(var,cont):
            if cont.startswith("#"):
                if cont == "#int": typ = settings.int_var_type
                elif cont == "#bool": typ = "bool"
                elif cont == "#float": typ = "float"
                else: typ = "string"
            else:
                if len(cont.split('"')) > 1 or len(cont.split("'")) > 1: typ = "string"
                elif cont == "true" or cont == "false": typ = "bool"
                else:
                    try: int(cont) ; typ = settings.int_var_type
                    except:
                        try: float(cont) ; typ = "float"
                        except:
                            typ = settings.int_var_type
                            psys.war(f"type inconnu ici -> {cont}")
            if typ == "string":
                teyes.add_to_include("std")
                teyes.add_to_include("print")
            return([var,typ])

        for iv in range(len(VAR)):
            v = VAR[iv]
            for ie in range(len(EYES)):
                e = EYES[ie]
                if e[0] == v[0]:
                    EYES.insert(ie+iv,[str(e[0]),1, "vari", varitype(v[1],v[2])])
                    break

    def edit_l(l,nb,len_tot):
        global ATOC, AFON
        def tab_c(l):
            t = 0
            while l.startswith(" "*t): t += settings.space_in_tabs
            return(int((t - settings.space_in_tabs)/settings.space_in_tabs))

        def del_end(cont,to_del):
            cont , to_del = str(cont) , str(to_del)
            return(cont.split(to_del)[len(cont.split(to_del))-2])

        def contient(var,cont):
            cont, var = str(cont), str(var)
            return(len(var.split(cont))-1)

        def iic(liste, e, p):
            atr = []
            for v in liste: atr.append(v[p])
            return(True if e in atr else False)

        l = str(l)
        TAB.append(tab_c(l))
        l = l.strip()
        l = (l.replace("True", "true")).replace("False","false")

        if l != "" or nb == len_tot-1:
            for loop in range(1,TAB[nb-1]-TAB[nb]+1):
                temp = ""
                for a in range(len(ATOC.split("/"))-1):
                    if a != 0: temp += "/" + ATOC.split("/")[a]
                ATOC = temp
                if not(ATOC.startswith(AFON)):
                    AFON = ""
                EYES.append([ATOC,TAB[nb-1]-1*loop,"}"])

        if nb == 0:
            EYES.append([ATOC,TAB[nb],"comm","interpreted and compiled by GLADE"])

        while l.startswith("#1!"):
            l = l.split("#1!")[1].strip()

        if l.endswith("#2!"):
            pass #ligne non interprétée

        elif l.startswith("#3!"):
            cont = l.split("#3!")[1].strip()
            EYES.append([ATOC,TAB[nb],"lnb",cont])

        elif l.startswith("if "):
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

        elif l.startswith("else"):
            EYES.append([ATOC,TAB[nb],"else"])
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
            AFON = "/" + cont.split("(")[0]

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
            teyes.add_to_include("std")
            teyes.add_to_include("print")

        elif l.startswith("return("):
            cont = l.split("return(")[1]
            cont = del_end(cont,")")
            EYES.append([ATOC,TAB[nb],"return",cont])

        elif l.startswith("try:"):
            EYES.append([ATOC,TAB[nb],"try"])
            EYES.append([ATOC,TAB[nb],"{"])

        elif l.startswith("except"):
            EYES.append([ATOC,TAB[nb],"except"])
            EYES.append([ATOC,TAB[nb],"{"])
        
        elif l.startswith("pass"):
            EYES.append([ATOC,TAB[nb],"pass"])

        elif l.startswith("#"):
            lb = l.replace("#", "")
            if lb.startswith("include "):
                cont = lb.split("include ")[1]
                EYES.append([ATOC,TAB[nb],"include",cont])
            else:
                EYES.append([ATOC,TAB[nb],"comm",lb])

        elif contient(l,"=") == 1:
            nom = l.split("=")[0].strip()
            cont = l.split("=")[1].strip()
            if "input(" in cont:
                teyes.add_to_include("std")
                teyes.add_to_include("print")
                txt = cont.split("input(")[1].split(")")[0]
                if txt.strip() != "":
                    EYES.append([ATOC,TAB[nb],"print end",txt])
                EYES.append([ATOC,TAB[nb],"input",nom])
                EYES.append([ATOC,TAB[nb],"ignore input"])
                if cont.startswith("int("): cont = "#int"
                elif cont.startswith("float("): cont = "#float"
                elif cont.startswith("bool("): cont = "#bool"
                else: cont = "#str"
            else:
                EYES.append([ATOC,TAB[nb],"vare",[nom,cont]])
            if not(iic(VAR, nom, 1)): VAR.append([AFON,nom,cont])

        elif l.strip() != "":
            EYES.append([ATOC,TAB[nb],"unknown",l])

    def main():
        fichier = cy.rfil_rela("/container",settings.todo)
        ligues = fichier.split("\n")
        ligues.append("")
        global EYES, TAB, VAR, ATOC, AFON, to_include
        EYES = [] # liste de code token eyes
        VAR = []  # liste des variables
        TAB = []  # liste des TAB
        ATOC = ""
        AFON = ""
        to_include = []


        # interpretation
        for nb in range(len(ligues)):
            teyes.edit_l(ligues[nb],nb,len(ligues))

        # auto-création du main
        if settings.auto_main:
            teyes.auto_main(["comm","include","using","def","{","}"])

        # auto-création des variables
        if settings.init_var:
            teyes.init_var()
        
        # auto-importation des modules
        if settings.auto_include:
            teyes.auto_include()
    
        # print (dev)
        log = ""
        for e in EYES:
            log += str(e) + "\n"
            if e[2] == "unknown":
                psys.war(f"ligne inconnu laissé brut ici -> {e[3]}")
        if settings.make_log:
            cy.cy_mkfil("/system","latest.log",log)

class compiler:
    def edit_e(e):
        def add_tab(tab): return(" "*tab*settings.space_in_tabs)
        
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
            arg = settings.int_var_type + " " + larg[0] + " = " + larg[1] + "; " + larg[0] + " < " + larg[2] + "; " + larg[0] + " = " + larg[0] + " + " + larg[3]
            EXIT.append(add_tab(tab) + "for (" + arg + ")")

        elif de == "if":
            EXIT.append(add_tab(tab) + "if (" + arg + ")")
        
        elif de == "elif":
            EXIT.append(add_tab(tab) + "else if (" + arg + ")")

        elif de == "else":
            EXIT.append(add_tab(tab) + "else")

        elif de == "return":
            EXIT.append(add_tab(tab) + "return " + arg + ";")

        elif de == "print end":
            EXIT.append(add_tab(tab) + "cout << " + arg + ";" )

        elif de == "print":
            EXIT.append(add_tab(tab) + "cout << " + arg + " << endl;" )

        elif de == "input":
            EXIT.append(add_tab(tab) + "cin >> " + arg + ";" )

        elif de == "ignore input":
            EXIT.append(add_tab(tab) + "cin.ignore();" )

        elif de == "include":
            EXIT.append(add_tab(tab) + "#include " + arg)

        elif de == "using":
            EXIT.append(add_tab(tab) + "using " + arg)

        elif de == "try":
            EXIT.append(add_tab(tab) + "try")

        elif de == "pass":
            EXIT.append(add_tab(tab) + ";")

        elif de == "except":
            EXIT.append(add_tab(tab) + "catch(...)")

        elif de == "lnb":
            EXIT.append(add_tab(tab) + arg)

        elif de == "comm":
            EXIT.append(add_tab(tab) + "// " + arg)

        elif de == "vare":
            EXIT.append(add_tab(tab) + arg[0] + " = " + arg[1] + ";")

        elif de == "vari":
            EXIT.append(add_tab(tab) + arg[1] + " " + arg[0] + ";  // auto var")

        elif de == "unknown":
            EXIT.append(add_tab(tab) + arg + ";")

        elif de == "{":
            EXIT.append(add_tab(tab) + "{")

        elif de == "}":
            EXIT.append(add_tab(tab) + "}")

        else:
            psys.gen_err("élément retourné inconnu par le compilateur: '" + de + "'\n      ici -> " + str(e))

    def main():
        global EXIT
        EXIT = []

        for e in EYES:
            compiler.edit_e(e)

class maker:
    def main():
        name = str(settings.todo.split(".")[len(settings.todo.split("."))-2]) + ".cpp"
        cy.mkfil("/container",name,"".join((l+"\n") for l in EXIT))

psys.info("initialisation")
settings = init()
inter.main()

while True:
    debut = time()
    teyes.main()
    psys.info(f"fin du token eyes ({psys.timer(debut)}ms)")
    debut = time()
    compiler.main()
    psys.info(f"fin de la compilation ({psys.timer(debut)}ms)")
    debut = time()
    maker.main()
    psys.info(f"fin de l'écriture ({psys.timer(debut)}ms)")
    if not settings.loop_compil: inter.main()