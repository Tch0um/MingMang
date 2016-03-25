from main import *

"""fonctions de créactions et d'affichage de la grille dans la console"""
def creegrille(taille):
    g=[0]*taille
    for i in range(taille):
        g[i]=[0]*taille
    """puis placement des pions"""   #0=vide   1=noir     2=blanc
    for x in range(taille):
        g[0][x]="1"
    for x in range(taille):
        g[x][0]="2"
    for x in range(taille):
        g[(taille)-1][x]="2"
    for x in range(taille):
        g[x][taille-1]="1"
    affiche(g)
    


def affiche(g):
    for i in g:
        for j in i:
            print(j,sep=' ',end=' ')
        print()


    
