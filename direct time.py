import tkinter as tk
import system.mod.Cytron as cy

fenetre = tk.Tk()
fenetre.geometry('950x700')
fenetre.resizable(width=0, height=0)
fenetre.title("direct time")
fenetre.configure(background="#000000")

cont = ""

py = tk.Text(fenetre, width=30,background="#212338",foreground="#b1e1f0",insertbackground="#00ffff")
py.place(x= 10 ,y=10,width= 460,height=680)

cpp = tk.Text(fenetre, width=30, background="#212338",foreground="#b1e1f0")
cpp.place(x= 480 ,y=10,width= 460,height=680)
cpp.configure(state='disabled')

def py_actu():
    global cont
    if py.get("0.0","end") != cont:
        cont = py.get("0.0","end")
        cy.mkfil("/container","DirectTime.py",cont)
    py.after(500,py_actu)

def cpp_actu():
    temp = cy.rfil_rela("/container","DirectTime.cpp")
    if temp == None: temp = "None"
    if temp != cpp.get("0.0","end") and temp.strip() != "":
        cpp.configure(state='normal')
        cpp.delete ("0.0", "end")
        cpp.insert(0.0, (temp if temp != "None" else "merci de lancer glade"))
        cpp.configure(state='disabled')
    cpp.after(500,cpp_actu)

cpp_actu()
py_actu()

fenetre.mainloop()