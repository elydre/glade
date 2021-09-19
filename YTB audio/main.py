from __future__ import unicode_literals
import youtube_dl
import mod.cytron as cy

print("lecture de la basse de donné 'todo.txt'")
try:
    todo = cy.rfil_rela("/","todo.txt").split("\n")
    print(len(todo),end=" ")
    print("fichier a convertir")
except: print("ERREUR: lecture de la basse de donné impossible\n")

try:
    print("téléchargement")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': cy.path() + "/audio/"+ "%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(todo)
except: print("ERREUR: téléchargement impossible\n")

input("fin, pressez entrer pour quitter")