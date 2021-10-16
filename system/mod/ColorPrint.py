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
.note    :
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

def colorprint(text,color="",background="",gras=False,ligne=False,end=True):
    style = ""
    if gras and ligne:
        print(f"{color}\033[01m\033[04m{background}"+text+f"\033[0m",end="")
    else:
        if not gras and ligne:
            style = "\033[01m"
        elif gras and not ligne:
            style = "\033[04m"
        print(f"{color}{style}{background}"+text+f"\033[0m",end="")
    if end:
        print("")


def colorinput(text,color="",background="",gras=False,ligne=False):
    style = ""
    if gras and ligne:
        temp = input(f"{color}\033[01m\033[04m{background}"+text+f"\033[0m")
    else:
        if not gras and ligne:
            style = "\033[01m"
        elif gras and not ligne:
            style = "\033[04m"
        temp = input(f"{color}{style}{background}"+text+f"\033[0m")
        return(temp)

class Colors:
    none = ""
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    light_blue = "\033[36m"
    white = "\033[37m"
    #rétrocompatibilité
    noir = "\033[30m"
    rouge = "\033[31m"
    vert = "\033[32m"
    jaune = "\033[33m"
    bleu = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    blanc = "\033[37m"

class Background:
    none = ""
    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    yellow = "\033[43m"
    blue = "\033[44m"
    purple = "\033[45m"
    light_blue = "\033[46m"
    white = "\033[47m"
    #rétrocompatibilité
    noir = "\033[40m"
    rouge = "\033[41m"
    vert = "\033[42m"
    jaune = "\033[43m"
    bleu = "\033[44m"
    magenta = "\033[45m"
    cyan = "\033[46m"
    blanc = "\033[47m"
