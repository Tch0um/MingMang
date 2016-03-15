from main import *

"""fonctions de créactions et d'affichage de la grille dans la console"""
def creegrille(taille):
    g=[0]*taille
    for i in range(taille):
        g[i]=[0]*taille
    affiche(g)


def affiche(g):
    for i in g:
        for j in i:
            print(j,sep=' ',end=' ')
        print()
    
