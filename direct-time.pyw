import tkinter as tk
import system.glade.Tools as gt
import system.glade.TEyes as te
import system.glade.Compiler as gc
import time

global settings, py, cpp, err
settings = gt.init(edit=False, todo = None, debug_print = False, sys_print = False, make_log = False, loop_compil = True)

fenetre = tk.Tk()
fenetre.geometry('1050x700')
fenetre.title("direct time")
fenetre.configure(background="#000000")

def get_size():
    return fenetre.winfo_width(), fenetre.winfo_height()

def place():
    l, h = get_size()
    sqrt = round(h**0.5*6)

    py.place(x = 10 ,y = 10, width = l/2-25, height = h-20)
    cpp.place(x = l/2-5 ,y = 10, width = l/2-5, height = h - sqrt - 10)
    err.place(x = l/2-5 ,y = h - sqrt + 10, width = l/2-5, height = sqrt - 20)

py = tk.Text(fenetre, width=30,background="#212338",foreground="#b1e1f0",insertbackground="#00ffff",font=("consolas", 12))
cpp = tk.Text(fenetre, width=30, background="#212338",foreground="#b1e1f0",font=("consolas", 12))
err = tk.Text(fenetre, width=30, background="#212338",foreground="#b1e1f0",font=("consolas", 12))



cpp.configure(state='disabled')
err.configure(state='disabled')

def py_actu():
    debut = time.time()
    global cont, old_dim, reac_time
    temp = py.get("0.0","end")
    
    while "	" in temp: temp = temp.replace("	","    ")
    
    err.configure(state='normal')
    err.delete("0.0","1.20")
    
    if temp != cont:
        cont = temp
        sortie, msg = te.main(fichier = temp,settings=settings)
        cpp.configure(state='normal')
        cpp.delete ("0.0", "end")
        err.delete ("0.0", "end")

        py.tag_delete("err", "1.0", "end")
        py.tag_delete("war", "1.0", "end")

        for e in msg:
            err.insert(0.0,f"|{e[0]}| {e[1]}\n")
            if e[0] == "c_war":
                py.tag_add("war", f"{e[2]+1}.0", f"{e[2]+1}.100")
                py.tag_config("war", foreground="#CDDC39")
            elif e[0] == "gen_err":
                py.tag_add("err", f"{e[2]+1}.0", f"{e[2]+1}.100")
                py.tag_config("err", foreground="red")
        err.insert(0.0,"\n")
        cpp.insert(0.0,"".join((l+"\n") for l in gc.compiler(sortie,settings)))
        cpp.configure(state='disabled')

    while len(reac_time) < 5:
        reac_time += "0"
        
    err.insert(0.0,f"rafraichi en {reac_time}s")
    err.configure(state='disabled')
    
    l, h = get_size()
    temp = f"{l}x{h}"
    if temp != old_dim:
        old_dim = temp
        place()

    reac_time = str(round(time.time() - debut,3))

    py.after(250,py_actu)

cont, old_dim, reac_time = "", "", "0.000"
py_actu()

fenetre.mainloop()