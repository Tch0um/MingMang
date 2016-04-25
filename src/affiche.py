#GORON Nathan 21503237

from main import *
from deplacement import *

##
# Cree la grille
# @param taille: défini la dimension du plateau
# @return: La grille de jeu
def creegrille(taille):
    global g
    g=[0]*taille
    for i in range(taille):
        g[i]=[0]*taille
    for x in range(taille):
        g[0][x]="2"
    for x in range(taille):
        g[x][0]="1"
    for x in range(taille):
        g[(taille)-1][x]="1"
    for x in range(taille):
        g[x][taille-1]="2"




##
# Affiche la grille g dans la console
# @return :La grille g en mode console
def affiche():
    res=""
    for i in g:
        for j in i:
            res+=str(j)+" "
        res+="\n"
    print (res)
        


    
