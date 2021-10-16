import system.glade.Tools as gt
def compiler(EYES,settings):
    EXIT = []

    for e in EYES:

        def add_tab(tab): return(" "*tab*settings.space_in_tabs)
        
        de = e[2]       #element detecte
        tab = e[1]      #nb de tab
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

        elif de == "print":
            EXIT.append(add_tab(tab) + "cout << " + arg[0] + arg[1] + ";")

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

        elif de == "break":
            EXIT.append(add_tab(tab) + "break;")

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
            gt.gen_err("élément retourné inconnu par le compilateur: '" + de + "'\n      ici -> " + str(e))

    return(EXIT)