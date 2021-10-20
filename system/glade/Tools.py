import system.mod.ColorPrint as cprint
import system.mod.Cytron as cy
from time import time as tm

# init

class init:
    def __init__(self):
        # valleur par defaut
        todo = None
        debug_print = True
        sys_print = True
        auto_main = True
        init_var = True
        auto_include = True
        make_log = True
        loop_compil = True
        space_in_tabs = 4
        int_var_type = "long int"

        para_edit = 0
        #lecture du fichier de paramètres
        if cy.rfil_rela("/system","settings.txt") == None: war("fichier de paramètres non trouvé")
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
                        else: war("valleur non bool pour debug print (False par defaut)\n      ici -> " + str(atr))

                    elif var == "sys print":
                        if atr == "False" or atr == "false": sys_print = False
                        elif atr == "True" or atr == "true": sys_print = True
                        else: war("valleur non bool pour debug print (True par defaut)\n      ici -> " + str(atr))

                    elif var == "make log":
                        if atr == "False" or atr == "false": make_log = False
                        elif atr == "True" or atr == "true": make_log = True
                        else: war("valleur non bool pour make log (True par defaut)\n      ici -> " + str(atr))

                    elif var == "init var":
                        if atr == "False" or atr == "false": init_var = False
                        elif atr == "True" or atr == "true": init_var = True
                        else: war("valleur non bool pour init var (True par defaut)\n      ici -> " + str(atr))

                    elif var == "auto main":
                        if atr == "False" or atr == "false": auto_main = False
                        elif atr == "True" or atr == "true": auto_main = True
                        else: war("valleur non bool pour auto main (True par defaut)\n      ici -> " + str(atr))

                    elif var == "loop compil":
                        if atr == "False" or atr == "false": loop_compil = False
                        elif atr == "True" or atr == "true": loop_compil = True
                        else: war("valleur non bool pour loop compil (False par defaut)\n      ici -> " + str(atr))

                    elif var == "auto include":
                        if atr == "False" or atr == "false": auto_include = False
                        elif atr == "True" or atr == "true": auto_include = True
                        else: war("valleur non bool pour auto include (True par defaut)\n      ici -> " + str(atr))
                    
                    elif var == "space in tabs":
                        try: space_in_tabs = int(atr)
                        except: war("valleur non int pour space in tabs (4 par defaut)\n      ici -> " + str(atr))
                    
                    else:
                        para_edit -= 1
                        gen_err("paramètres inconnu\n      ici -> " + str(p))

            info(str(para_edit)+" paramètres édités")
            
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
        if settings.todo == None or settings.todo == "":
            inp = input("~} ")
        else:
            cprint.colorprint("(",color=cprint.Colors.blanc, end=False)
            cprint.colorprint(settings.todo,color=cprint.Colors.cyan, end=False)
            cprint.colorprint(")",color=cprint.Colors.blanc, end=False)
            ipt = input(" ~} ")
            inp = settings.todo if ipt == "" else ipt

        if not(inp.startswith("!")):
            settings.todo = inp
            if cy.rfil_rela("/container",settings.todo) != None: no_done = False
            else: gen_err("fichier non existent ou illisible")
        else:
            if inp == "!r":
                settings = init()
                info("paramètres rechargé")

            elif inp == "!c":
                cy.clear()

            else: gen_err("commande existente")
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
    for e in EYES:
        log += str(e) + "\n"
        if e[2] == "unknown":
            war(f"ligne inconnu laissé brut ici -> {e[3]}")
    if settings.make_log:
        cy.cy_mkfil("/system","latest.log",log)

# maker

def maker(settings,EXIT):
    name = str(settings.todo.split(".")[len(settings.todo.split("."))-2]) + ".cpp"
    cy.mkfil("/container",name,"".join((l+"\n") for l in EXIT))

# édition de ligne

def del_end(cont,to_del):
    return(cont.split(to_del)[len(cont.split(to_del))-2])

def iic(liste, e, p):
    return(True if e in [v[p] for v in liste] else False)

def tab_c(space_in_tabs,l):
    t = 0
    while l.startswith(" "*t): t += space_in_tabs
    return(int((t - space_in_tabs)/space_in_tabs))

# analyser

def varitype(var,cont,settings):
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
                    war(f"type inconnu ici -> {cont}")
    
    if settings.debug_print: dev(f"création de variable automatique: '{var}' de type '{typ}'")
    return([var,typ])