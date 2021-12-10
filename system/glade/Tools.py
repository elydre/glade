import system.mod.ColorPrint as cprint
import system.mod.Cytron as cy
from system.glade.TEyes import version as TEversion
from system.glade.Compiler import version as GCversion
from time import time as tm

version = "0.12b"

# init -> settings

class init:
    def __init__(self, edit = 1, todo = None, debug_print = True, sys_print = True, auto_main = True, init_var = True, auto_include = True, make_log = True, loop_compil = False, space_in_tabs = 4, int_var_type = "long int"): # sourcery no-metrics skip: de-morgan
        para_edit = 0
        #lecture du fichier de paramètres
        if cy.rfil_rela("/system", "settings.txt") is None: war("fichier de paramètres non trouvé")
        elif edit == 1:
            for p in cy.rfil_rela("/system","settings.txt").split("\n"):
                if not(p.startswith("#")) and len(p.split("=")) > 1:
                    para_edit += 1
                    var = p.split("=")[0].strip()
                    atr = p.split("=")[1].strip()

                    if var == "todo":
                        todo = None if atr == "None" else atr

                    elif var == "int var type":
                        int_var_type = atr

                    elif var == "debug print":
                        if atr in ["False", "false", "f"]: debug_print = False
                        elif atr in ["True", "true", "t"]: debug_print = True
                        else: war("valeur non bool pour debug print (False par defaut)\n      ici -> " + str(atr))

                    elif var == "sys print":
                        if atr in ["False", "false", "f"]: sys_print = False
                        elif atr in ["True", "true", "t"]: sys_print = True
                        else: war("valeur non bool pour debug print (True par defaut)\n      ici -> " + str(atr))

                    elif var == "make log":
                        if atr in ["False", "false", "f"]: make_log = False
                        elif atr in ["True", "true", "t"]: make_log = True
                        else: war("valeur non bool pour make log (True par defaut)\n      ici -> " + str(atr))

                    elif var == "init var":
                        if atr in ["False", "false", "f"]: init_var = False
                        elif atr in ["True", "true", "t"]: init_var = True
                        else: war("valleur non bool pour init var (True par defaut)\n      ici -> " + str(atr))

                    elif var == "auto main":
                        if atr in ["False", "false", "f"]: auto_main = False
                        elif atr in ["True", "true", "t"]: auto_main = True
                        else: war("valeur non bool pour auto main (True par defaut)\n      ici -> " + str(atr))

                    elif var == "loop compil":
                        if atr in ["False", "false", "f"]: loop_compil = False
                        elif atr in ["True", "true", "t"]: loop_compil = True
                        else: war("valeur non bool pour loop compil (False par defaut)\n      ici -> " + str(atr))

                    elif var == "auto include":
                        if atr in ["False", "false", "f"]: auto_include = False
                        elif atr in ["True", "true", "t"]: auto_include = True
                        else: war("valeur non bool pour auto include (True par defaut)\n      ici -> " + str(atr))

                    elif var == "space in tabs":
                        try: space_in_tabs = int(atr)
                        except: war("valeur non int pour space in tabs (4 par defaut)\n      ici -> " + str(atr))

                    else:
                        para_edit -= 1
                        gen_err("paramètres inconnu\n      ici -> " + str(p))

            info(str(para_edit)+" paramètres édités")

        elif edit == 2:
            def send(defaut, texte):
                cprint.colorprint("(", color=cprint.Colors.blanc, end=False)
                cprint.colorprint(defaut, color=cprint.Colors.cyan, end=False)
                cprint.colorprint(") ", color=cprint.Colors.blanc, end=False)
                cprint.colorprint(texte, color=cprint.Colors.blanc, end=False)
                user = cprint.colorinput(" -> ", color=cprint.Colors.blanc)
                return defaut if user == "" else user

            cont = f"todo = {send('t.py', 'todo')}\n"
            cont += f"space in tabs = {send('4', 'space in tabs')}\n"
            cont += f"int var type = {send('long int', 'int var type')}\n"
            cont += f"loop compil = {send('False', 'loop compil')}\n\n"
            cont += f"debug print = {send('False', 'debug print')}\n"
            cont += f"sys print = {send('True', 'sys print')}\n"
            cont += f"auto main = {send('True', 'auto main')}\n"
            cont += f"init var = {send('True', 'init var')}\n"
            cont += f"auto include = {send('True', 'auto include')}\n"
            cont += f"make log = {send('True', 'make log')}"

            cy.mkfil("/system","settings.txt",cont)

        self.todo = todo
        self.debug_print = debug_print
        self.space_in_tabs = space_in_tabs
        self.auto_main = auto_main
        self.init_var = init_var
        self.auto_include = auto_include
        self.int_var_type = int_var_type
        self.make_log = make_log
        self.loop_compil = loop_compil
        self.sys_print = sys_print

# request

def request(settings):
    no_done = True
    while no_done:
        cprint.colorprint("\nprogramme dans le dossier '/container'",color=cprint.Colors.blanc)
        ls_liste = cy.ls("/container")
        for element in ls_liste:
            ext = element.split(".")[-1]
            cprint.colorprint(" ",color=cprint.Colors.none,end=False)
            if ext == "py": cprint.colorprint(element,color=cprint.Colors.jaune,end=False,ligne=True)
            elif ext == "cpp": cprint.colorprint(element,color=cprint.Colors.magenta,ligne=True,end=False)
            else: cprint.colorprint(element,color=cprint.Colors.blanc,end=False)
        print("\n")
        if settings.todo is None or settings.todo == "": inp = input("~} ")
        else:
            cprint.colorprint("(",color=cprint.Colors.blanc, end=False)
            cprint.colorprint(settings.todo,color=cprint.Colors.cyan, end=False)
            cprint.colorprint(")",color=cprint.Colors.blanc, end=False)
            ipt = input(" ~} ")
            inp = settings.todo if ipt == "" else ipt

        if not(inp.startswith("!")):
            settings.todo = inp
            if cy.rfil_rela("/container", settings.todo) is None: gen_err("fichier non existent ou illisible")
            else: no_done = False
        elif inp == "!r":
            settings = init()
            info("paramètres rechargé")

        elif inp == "!e":
            settings = init(edit = 2)
            settings = init()


        elif inp == "!c":
            cy.clear()

        elif inp == "!v":
            print(f"version de Cytron:            {cy.version()}")
            print(f"version de la boite à outils: {version}")
            print(f"version du TokenEyes:         {TEversion}")
            print(f"version du compilateur:       {GCversion}")

        else: gen_err("commande non existente")
    return(settings)

# print

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

# timer

def time():
    return(tm())

def timer(debut):
    return(round((time() - debut)*1000,1))

# log

def log(EYES, settings):
    log = ""
    sortie = []
    for e in EYES:
        log += str(e) + "\n"
        if e[2] == "unknown":
            sortie.append(["c_war",f"ligne inconnu laissée brute ici -> {e[3]}",e[4]])
    if settings.make_log:
        cy.cy_mkfil("/system","latest.log",log)
    return(sortie)

def printlog(MSG):
    for e in MSG:
        if e[0] == "info": info(e[1])
        elif e[0] == "dev": dev(e[1])
        elif e[0] == "gen_err":gen_err(f"l.{e[2]}: {e[1]}")
        elif e[0] in ["war", "c_war"]: war(f"l.{e[2]}: {e[1]}")
        else: war(f"printlog inconnu -> {e}")
# maker

def maker(settings,EXIT):
    name = str(settings.todo.split(".")[len(settings.todo.split("."))-2]) + ".cpp"
    cy.mkfil("/container",name,"".join((l+"\n") for l in EXIT))

# édition de ligne

def del_end(cont,to_del):
    return cont[:-len(to_del)] if to_del in cont else cont

def iic(liste, e, p):
    return e in [v[p] for v in liste]

def tab_c(space_in_tabs,l):
    t = 0
    while l.startswith(" "*t): t += space_in_tabs
    return(int((t - space_in_tabs)/space_in_tabs))

# analyser

def varitype(var,cont,settings,allvar):
    m = [None,None]
    typ = None
    for v in allvar:
        if cont == v[1]:
            typ = v[4]
    if typ is None:
        if cont.startswith("#"):
            if cont == "#int": typ = settings.int_var_type
            elif cont == "#bool": typ = "bool"
            elif cont == "#float": typ = "float"
            else: typ = "string"
        elif len(cont.split('"')) > 1 or len(cont.split("'")) > 1: typ = "string"
        elif cont in ["true", "false"]: typ = "bool"
        else:
            try: int(cont) ; typ = settings.int_var_type
            except:
                try: float(cont) ; typ = "float"
                except:
                    typ = "long int"
                    m[0] = ["c_war", f"type inconnu ici -> {cont}"]

    if settings.debug_print: m[1] = ["dev", f"'{cont}' est de type '{typ}'"]
    return(m,[var,typ])