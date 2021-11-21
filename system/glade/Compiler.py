import system.glade.Tools as gt

version = "0.5"

def compiler(EYES,settings):  # sourcery no-metrics
    EXIT = []
    
    def add_tab(tab): return(" "*tab*settings.space_in_tabs)

    for e in EYES:
        tab, de = e[1] , e[2]
        try: arg = e[3] #arg
        except: arg = None

        if de == "def":
            EXIT.append(f"{add_tab(tab)}int {arg}")

        elif de == "while":
            EXIT.append(f"{add_tab(tab)}while ({arg})")

        elif de == "for":
            EXIT.append(f"{add_tab(tab)}for ({settings.int_var_type} {arg[0]} = {arg[1]} ; {arg[0]} < {arg[2]} ; {arg[0]} = {arg[0]}  + {arg[3]})")

        elif de == "if":
            EXIT.append(f"{add_tab(tab)}if ({arg})")
        
        elif de == "elif":
            EXIT.append(f"{add_tab(tab)}else if ({arg})")

        elif de == "else":
            EXIT.append(f"{add_tab(tab)}else")

        elif de == "return":
            EXIT.append(f"{add_tab(tab)}return {arg};")

        elif de == "print":
            EXIT.append(f"{add_tab(tab)}cout << {arg[0]}{arg[1]};")

        elif de == "input":
            EXIT.append(f"{add_tab(tab)}cin >> {arg};" )

        elif de == "ignore input":
            EXIT.append(f"{add_tab(tab)}cin.ignore();" )

        elif de == "include":
            EXIT.append(f"{add_tab(tab)}#include {arg}")

        elif de == "using":
            EXIT.append(f"{add_tab(tab)}using {arg}")

        elif de == "try":
            EXIT.append(f"{add_tab(tab)}try")

        elif de == "pass":
            EXIT.append(f"{add_tab(tab)};")

        elif de == "break":
            EXIT.append(f"{add_tab(tab)}break;")

        elif de == "except":
            EXIT.append(f"{add_tab(tab)}catch(...)")

        elif de == "lnb":
            EXIT.append(f"{add_tab(tab)}{arg}")

        elif de == "comm":
            EXIT.append(f"{add_tab(tab)}// {arg}")

        elif de == "vare":
            EXIT.append(f"{add_tab(tab)}{arg[0]}{arg[2]}{arg[1]};")

        elif de == "vari":
            EXIT.append(f"{add_tab(tab)}{arg[1]} {arg[0]};  // auto var")

        elif de == "prelist":
            EXIT.append(f"{add_tab(tab)}{arg[0]} {arg[1]}[] = " + "{" + arg[2] + "};")

        elif de == "unknown":
            EXIT.append(f"{add_tab(tab)}{arg};")

        elif de == "{":
            EXIT.append(add_tab(tab)+"{")

        elif de == "}":
            EXIT.append(add_tab(tab)+"}")

        else:
            gt.gen_err(f"élément retourné inconnu par le compilateur: '{de}'\n      ici -> {str(e)}")

    return(EXIT)