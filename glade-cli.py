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
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

import system.mod.Cytron as cy
import system.glade.Tools as gt
import system.glade.TEyes as te
import system.glade.Compiler as gc

cy.clear()
print(f"GLADE cli v{te.version}\nCopyright (C) pf4. Tous droits réservés.\n")
gt.info("initialisation")
settings = gt.request(gt.init())

while True:
    debut = gt.tm()
    EYES, MSG = te.main(fichier = cy.rfil_rela("/container",settings.todo),settings=settings)
    gt.printlog(MSG)
    if settings.sys_print: gt.info(f"fin du token eyes ({gt.timer(debut)}ms)")
    debut = gt.tm()
    gt.maker(settings,gc.compiler(EYES,settings))
    if settings.sys_print: gt.info(f"fin de la compilation ({gt.timer(debut)}ms)")
    if not settings.loop_compil: settings = gt.request(settings)