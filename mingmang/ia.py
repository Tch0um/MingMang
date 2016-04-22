from deplacement import *
from affiche import *
import affiche


#IA = PIONS N°2
def touria(tour,taille,nbtour):
    print("lancement de touria")
    aleatour=0
    if taille==9:
        aleatour=5
    elif taille==19:
        aleatour=7
    elif taille<=29:
        aleatour=10
    if nbtour <=aleatour:
        coord=mvmaleatoiredebut(taille)
        affiche.g[[coord[0][0]]]
        ("déplacement aléatoire effectuée , tour suivant")
        main.toursuivant(3,tour,taille,nbtour)
        
        


def mvmaleatoiredebut(taille):
    choixligne=randint(1,2)
    print(choixligne)
    if choixligne==1:#selection hasard d'un pion n°2 sur la ligne du haut
        x1=0
        y1=randint(1,taille-1)
    elif choixligne==2:#ligne de droite
        x1=randint(1,taille-1)
        y1=taille-1
    while affiche.g[x1][y1]==0:
        if choixligne==1:
            x1=0
            y1=randint(1,taille-1)
        elif choixligne==2:
            x1=randint(1,taille-1)
            y1=taille-1
    #notre pion est choisis et peut etre bougé
    print("pion selectionné",x1,y1)
    if choixligne==1:
        for i in range(1,taille):
            if affiche.g[i][y1]!=0:
                x2=randint(1,i)
                y2=y1
                return[[x1,y1],[x2,y2]]
    if choixligne==2:
        for i in range(taille):
            if affiche.g[x1][i]!=0:
                myst=randint(i+1,taille)
                x2=x1
                y2=myst
                return[[x1,y1]][x2,y2]]
                
                
            
    
    
                

        
        
    
    

"""def calculoffense(taille):

def calculdefense(taille):



def modifgrille(coord1,coord2,taille)#modification de la grille aprés attribution des coordonées optimales"""
    
    
