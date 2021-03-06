'''    _             _
  ___ | | _   _   __| | _ __   ___
 / _ \| || | | | / _` || '__| / _ |
|  __/| || |_| || (_| || |   |  __/
 \___||_| \__, | \__,_||_|    \___|
          |___/
___________________________________

 - codé en : UTF-8
 - langage : python3
 - GitHub  : github.com/elydre
 - Licence : GNU GPL v3
'''       

import system.glade.Tools as gt

version = "0.5.2b"

def add_to_include(element):
    if element not in to_include:
        to_include.append(element)

def auto_main(settings,liste):
    for ei in range(len(EYES)):
        e = EYES[ei]
        if e[1] == 0 and e[2] not in liste:
            if settings.debug_print: MSG.append(["dev","création de la fonction main automatique"])
            EYES.insert(ei,['', 0, 'def', 'main()'])
            EYES.insert(ei+1,['', 0, '{'])
            try:
                for ei2 in range(ei+2,len(EYES)):
                    e2 = EYES[ei2]
                    e2[0] = f"/main{e2[0]}"
                    e2[1] += 1
            except Exception:
                MSG.append(["gen_err","42"])

            EYES.append(['', 0, '}'])
            for v in VAR:
                if v[0] == "":
                    v[0] = "/main"
            break

def auto_include(settings):
    for ti in to_include:
        if ti == "print":
            if settings.debug_print: MSG.append(["dev","importation de print automatique"])
            EYES.insert(1,['',0, "include", "<iostream>"])
        elif ti == "std":
            if settings.debug_print: MSG.append(["dev","namespace std automatique"])
            EYES.insert(1,['',0, "using", "namespace std;"])
        else:
            MSG.append(["gen_err",f"element a auto importer inconnu, ici -> {ti}","?"])

def init_var(settings):
    def varitype(var,cont,nb):
        m, vt = gt.varitype(var,cont,settings,VAR)
        if m[0] != None: MSG.append(m[0]+[nb])
        if m[1] != None: MSG.append(m[1])
        var, typ = vt[0], vt[1]
        if typ == "string":
            add_to_include("std")
            add_to_include("print")
        return([var,typ])

    for iv in range(len(VAR)):
        v = VAR[iv]
        for ie in range(len(EYES)):
            e = EYES[ie]
            if e[0] == v[0]:
                vtype = varitype(v[1],v[2],v[3])
                EYES.insert(ie+iv,[str(e[0]),1, "vari", vtype])
                VAR[iv][4] = vtype[1]
                break

def kc(l,start,end=":"):  # keep center
    return(gt.del_end(l.split(start)[1],end))


def edit_l(settings,l,nb,len_tot):  # sourcery no-metrics
    global ATOC, AFON

    l = str(l)
    TAB.append(gt.tab_c(settings.space_in_tabs,l))
    l = l.strip()
    l = (l.replace("True", "true")).replace("False","false")

    sl = lambda text: l.startswith(text) # start of line

    if l != "" or nb == len_tot-1:
        for loop in range(1,TAB[nb-1]-TAB[nb]+1):
                temp = "".join(
                    "/" + ATOC.split("/")[a]
                    for a in range(len(ATOC.split("/")) - 1) if a != 0)
                ATOC = temp
                if not(ATOC.startswith(AFON)): AFON = ""
                EYES.append([ATOC,TAB[nb-1]-1*loop,"}"])

    if nb == 0:
        EYES.append([ATOC,TAB[nb],"comm","interpreted and compiled by GLADE"])

    while sl("#1!"):
        l = l.split("#1!")[1].strip()

    if l.endswith("#2!"):
        pass #ligne non interprétée

    elif sl("#3!"):
        cont = l.split("#3!")[1].strip()
        EYES.append([ATOC,TAB[nb],"lnb",cont])

    elif sl("if "):
        cont = kc(l, "if ")
        EYES.append([ATOC,TAB[nb],"if",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/if"

    elif sl("elif "):
        cont = kc(l, "elif ")
        EYES.append([ATOC,TAB[nb],"elif",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/elif"

    elif sl("else"):
        EYES.append([ATOC,TAB[nb],"else"])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/else"

    elif sl("while "):
        cont = kc(l, "while ")
        EYES.append([ATOC,TAB[nb],"while",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/while"

    elif sl("def "):
        cont = kc(l, "def ")
        EYES.append([ATOC,TAB[nb],"def",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/" + cont.split("(")[0]
        AFON = "/" + cont.split("(")[0]

    elif sl("for "):
        if "in range" in l:
            try:
                cont = kc(l, "for ", "):")
                var_name, arg = cont.split(" in range(")[0], cont.split(" in range(")[1].split(",")
                pas , min , max = "1", "0", "0"
                if len(arg) == 1: max = arg[0]
                if len(arg) >= 2: min, max = arg[0], arg[1]
                if len(arg) == 3: pas = arg[2]

                EYES.append([ATOC,TAB[nb],"for",[var_name,min,max,pas]])
                EYES.append([ATOC,TAB[nb],"{"])
                ATOC += "/for"
            except:
                MSG.append(["gen_err",f"boucle for non valide ici -> {l}",nb])

        else:
            MSG.append(["c_war",f"les boucle de liste ne sont pas implémenter ici -> {l}",nb])
            EYES.append([ATOC,TAB[nb],"comm",l])
            EYES.append([ATOC,TAB[nb],"{"])

    elif sl("print("):
        cont, end = "", "endl"
        for e in gt.del_end(l.split("print(")[1],")").split(","):
            e = e.strip()
            if e.startswith("end=") or e.startswith("end ="): end = e.split("=")[1].strip()
            else: cont += e + " << "

        EYES.append([ATOC,TAB[nb],"print",[cont,end]])
        add_to_include("std")
        add_to_include("print")

    elif sl("return"):
        cont = l.split("return")[1].strip()
        if cont.startswith("(") and cont.endswith(")"):
            cont = cont[1:-1]
        EYES.append([ATOC,TAB[nb],"return",cont])

    elif sl("try:"):
        EYES.append([ATOC,TAB[nb],"try"])
        EYES.append([ATOC,TAB[nb],"{"])

    elif sl("except"):
        EYES.append([ATOC,TAB[nb],"except"])
        EYES.append([ATOC,TAB[nb],"{"])

    elif sl("pass"):
        EYES.append([ATOC,TAB[nb],"pass"])

    elif sl("break"):
        EYES.append([ATOC,TAB[nb],"break"])

    elif sl("#"):
        lb = l.replace("#", "")
        EYES.append(
            [ATOC,TAB[nb],"include",lb.split("include ")[1:]]
            if lb.startswith("include ") else
            EYES.append([ATOC,TAB[nb],"comm",lb]))

    elif "=" in l:
        typ = " = "
        nom, cont = l.split("=")[0].strip(), "".join(l.split("=")[1:]).strip()
        if nom.endswith("-"): typ, nom = " -= ", gt.del_end(nom,"-").strip()
        elif nom.endswith("+"): typ, nom = " += ", gt.del_end(nom,"+").strip()

        if "[" in cont and "]" in cont:
            liste = cont.split("[")[1].split("]")[0].strip()
            m, type = gt.varitype(None,liste.split(",")[0].strip(),settings,VAR)
            if m[0] != None: MSG.append(m[0]+[nb])
            if m[1] != None: MSG.append(m[1])
            EYES.append([ATOC,TAB[nb],"mklist",[type[1],nom,liste]])
        else:
            if "input(" in cont:
                add_to_include("std")
                add_to_include("print")
                txt = cont.split("input(")[1].split(")")[0]
                if txt.strip() != "":
                    EYES.append([ATOC,TAB[nb],"print",[txt,""]])
                EYES.append([ATOC,TAB[nb],"input",nom])
                EYES.append([ATOC,TAB[nb],"ignore input"])
                if cont.startswith("int("): cont = "#int"
                elif cont.startswith("float("): cont = "#float"
                elif cont.startswith("bool("): cont = "#bool"
                else: cont = "#str"
            
            else:
                EYES.append([ATOC,TAB[nb],"vare",[nom,cont,typ]])

            if not(gt.iic(VAR, nom, 1)): VAR.append([AFON,nom,cont,nb,None])

    elif l.strip() != "":
        EYES.append([ATOC,TAB[nb],"unknown",l,nb])

def main(settings,fichier):
    ligues = str(fichier).split("\n")
    while ligues and ligues[-1] == "": ligues.pop(-1)
    ligues.append("")
    global EYES, TAB, VAR, ATOC, AFON, MSG, to_include
    EYES = [] # liste de code token eyes (tokenize)
    VAR = []  # liste des variables
    TAB = []  # liste des TAB
    MSG = []  # msg a print
    ATOC = ""
    AFON = ""
    to_include = []

    # interpretation
    for nb in range(len(ligues)): edit_l(settings,ligues[nb],nb,len(ligues))

    # auto-création du main
    if settings.auto_main: auto_main(settings,["comm","include","using","def","{","}"])

    # auto-création des variables
    if settings.init_var: init_var(settings)

    # auto-importation des modules
    if settings.auto_include: auto_include(settings)

    # print & log
    MSG += gt.log(EYES, settings)

    return(EYES, MSG)