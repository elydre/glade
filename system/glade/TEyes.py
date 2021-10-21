import system.glade.Tools as gt

version = "0.4.7"

def add_to_include(element):
        if not(element in to_include):
            to_include.append(element)

def auto_main(settings,liste):
    for ei in range(len(EYES)):
        e = EYES[ei]
        if e[1] == 0 and not(e[2] in liste):
            if settings.debug_print: MSG.append(["dev","création de la fonction main automatique"])
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

def auto_include(settings):
    for ti in to_include:
        if ti == "print":
            if settings.debug_print: MSG.append(["dev","importation de print automatique"])
            EYES.insert(1,['',0, "include", "<iostream>"])
        elif ti == "std":
            if settings.debug_print: MSG.append(["dev","namespace std automatique"])
            EYES.insert(1,['',0, "using", "namespace std;"])
        else:
            MSG.append(["gen_err",f"element a auto importer inconnu, ici -> {ti}"])

def init_var(settings):
    def varitype(var,cont,nb):
        m, vt = gt.varitype(var,cont,settings)
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
                EYES.insert(ie+iv,[str(e[0]),1, "vari", varitype(v[1],v[2],v[3])])
                break

def edit_l(settings,l,nb,len_tot):
    global ATOC, AFON
    
    l = str(l)
    TAB.append(gt.tab_c(settings.space_in_tabs,l))
    l = l.strip()
    l = (l.replace("True", "true")).replace("False","false")

    if l != "" or nb == len_tot-1:
        for loop in range(1,TAB[nb-1]-TAB[nb]+1):
            temp = ""
            for a in range(len(ATOC.split("/"))-1):
                if a != 0: temp += "/" + ATOC.split("/")[a]
            ATOC = temp
            if not(ATOC.startswith(AFON)): AFON = ""
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
        cont = gt.del_end(cont,":")
        EYES.append([ATOC,TAB[nb],"if",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/if"

    elif l.startswith("elif "):
        cont = l.split("elif ")[1]
        cont = gt.del_end(cont,":")
        EYES.append([ATOC,TAB[nb],"elif",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/elif"

    elif l.startswith("else"):
        EYES.append([ATOC,TAB[nb],"else"])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/else"

    elif l.startswith("while "):
        cont = l.split("while ")[1]
        cont = gt.del_end(cont,":")
        EYES.append([ATOC,TAB[nb],"while",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/while"

    elif l.startswith("def "):
        cont = l.split("def ")[1]
        cont = gt.del_end(cont,":")
        EYES.append([ATOC,TAB[nb],"def",cont])
        EYES.append([ATOC,TAB[nb],"{"])
        ATOC += "/" + cont.split("(")[0]
        AFON = "/" + cont.split("(")[0]

    elif l.startswith("for "):
        if "in range" in l:
            try:
                cont = l.split("for ")[1]
                cont = gt.del_end(cont,"):")
                var_name = cont.split(" in range(")[0]
                arg = cont.split(" in range(")[1].split(",")
                pas , min , max = "1", "0", "0"
                if len(arg) == 1:
                    max = arg[0]
                if len(arg) >= 2:
                    min = arg[0]
                    max = arg[1]
                if len(arg) == 3:
                    pas = arg[2]

                EYES.append([ATOC,TAB[nb],"for",[var_name,min,max,pas]])
                EYES.append([ATOC,TAB[nb],"{"])
                ATOC += "/for"
            except:
                MSG.append(["gen_err",f"boucle for non valide ici -> {l}",nb])
            
        else:
            MSG.append(["c_war",f"les boucle de liste ne sont pas implémenter ici -> {l}",nb])
            EYES.append([ATOC,TAB[nb],"comm",l])
            EYES.append([ATOC,TAB[nb],"{"])

    elif l.startswith("print("):
        cont = ""
        end = "endl"
        for e in gt.del_end(l.split("print(")[1],")").split(","):
            e = e.strip()
            if e.startswith("end=") or e.startswith("end ="):
                end = e.split("=")[1].strip()
            else:
                cont += e + " << "

        EYES.append([ATOC,TAB[nb],"print",[cont,end]])
        add_to_include("std")
        add_to_include("print")

    elif l.startswith("return("):
        cont = l.split("return(")[1]
        cont = gt.del_end(cont,")")
        EYES.append([ATOC,TAB[nb],"return",cont])

    elif l.startswith("try:"):
        EYES.append([ATOC,TAB[nb],"try"])
        EYES.append([ATOC,TAB[nb],"{"])

    elif l.startswith("except"):
        EYES.append([ATOC,TAB[nb],"except"])
        EYES.append([ATOC,TAB[nb],"{"])
    
    elif l.startswith("pass"):
        EYES.append([ATOC,TAB[nb],"pass"])

    elif l.startswith("break"):
        EYES.append([ATOC,TAB[nb],"break"])

    elif l.startswith("#"):
        lb = l.replace("#", "")
        if lb.startswith("include "):
            cont = lb.split("include ")[1]
            EYES.append([ATOC,TAB[nb],"include",cont])
        else:
            EYES.append([ATOC,TAB[nb],"comm",lb])

    elif "=" in l:
        nom = l.split("=")[0].strip()
        cont = l.split("=")[1].strip()
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
            EYES.append([ATOC,TAB[nb],"vare",[nom,cont]])
        if not(gt.iic(VAR, nom, 1)): VAR.append([AFON,nom,cont,nb])

    elif l.strip() != "":
        EYES.append([ATOC,TAB[nb],"unknown",l,nb])

def main(settings,fichier):
    ligues = str(fichier).split("\n")
    while "" in ligues:
        ligues.remove("")
    ligues.append("")
    global EYES, TAB, VAR, ATOC, AFON, MSG, to_include
    EYES = [] # liste de code token eyes
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