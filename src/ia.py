#GORON Nathan 21503237

from deplacement import *
from affiche import *
import affiche

essais=0

#IA = PIONS N°2

##
# définis quelle logique doit adopter l'IA en fonction du tour
# @param taille: dimension du plateau
# @param tour: détermine qui doit jouer
# @param nbtour: définis le numero du tour actuel
def touria(tour,taille,nbtour):
    print(nbtour)
    print("                  Au tour de l'IA!")
    print()
    aleatour=0
    if taille==9:
        aleatour=30
    elif taille==19:
        aleatour=35
    elif taille<=29:
        aleatour=40
    if nbtour <=aleatour:
        coord=mvmaleatoiredebut(taille)
        affiche.g[coord[0][0]][coord[0][1]]=0
        affiche.g[coord[1][0]][coord[1][1]]=2
        print("l'ia a déplacé le pion en",coord[0],"jusqu'en",coord[1])
        main.toursuivant(3,tour,taille,nbtour)
    else:
        dodgeorrand=randint(1,2)
        if dodgeorrand==1:
            dodge(taille)
        else:
            coord=mvmaleatoire(taille)
            affiche.g[coord[0][0]][coord[0][1]]=0
            affiche.g[coord[1][0]][coord[1][1]]=2
            if coord[0][0]<=2:
                coord=dodge(taille)
                affiche.g[coord[0][0]][coord[0][1]]=0
                affiche.g[coord[1][0]][coord[1][1]]=2
                
        
            
        
        
    
        
        

##
# fonction de mouvement aléatoire
# @param taille:définis la dimension du plateau
# @return : une paire de coordonées indiquant a l'IA le déplacement a appliquer
def mvmaleatoiredebut(taille):
    choixligne=randint(1,2)
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
                return[[x1,y1],[x2,y2]]
                
##
# fonctions de défense , permet a l'IA de protéger un pion en le déplacant hors de danger
# @param taille: dimension du plateau
# @return : une paire de coordonées indiquant a l'IA le déplacement a appliquer
def dodge(taille):
    listedodge=[]
    for i in range(1,taille-1):
        for j in range(1,taille-1):
            if affiche.g[i][j]==2:
                if affiche.g[i-1][j]==1:
                    if affiche.g[i+1][j]==0:
                        return[[i,j],[i+1,j]]
                    if affiche.g[i][j+1]==0:
                        return [[i,j],[i,j+1]]
                    if affiche.g[i][j-1]==0:
                        return [[i,j],[i,j-1]]
                                
                        
                if affiche.g[i+1][j]==1:
                    
                    if affiche.g[i-1][j]==0:   
                        return[[i,j],[i-1,j]]
                    if affiche.g[i][j+1]==0:
                        return [[i,j],[i,j+1]]
                    if affiche.g[i][j-1]==0:
                        return [[i,j],[i,j-1]]

                if affiche.g[i][j+1]==1:
                                
                    if affiche.g[i+1][j]==0:
                        return [[i,j],[i+1,j]]
                    if affiche.g[i][j-1]==0:
                        return [[i,j],[i,j+1]]
                    if affiche.g[i][j-1]==0:
                        return [[i,j],[i,j-1]]
                
                        
##
# fonctions d'offense , permet a l'IA de capturer un pion
# @param taille: dimension du plateau
# @return : une paire de coordonées indiquant a l'IA le déplacement a appliquer
def mvmcapture(taille):
     for i in range(taille):
        for j in range(1,taille-1):
            if affiche.g[i][j]==2:
                for h in range(1,taille-1):
                    if affiche.g[i+h][j]==1:#selection hasard d'un pion n°2 sur la ligne du haut
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
                            y1=taille
                return[[0],[x1,y1],[x2,y2]]
                for h in range(taille):
                    if affiche.g[i+h][j]==1:#selection hasard d'un pion n°2 sur la ligne du gauche
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
                            y1=taille
                return[[0],[x1,y1],[x2,y2]]           
                for h in range(1,taille+1):
                    if affiche.g[i+h][j]==1:#selection hasard d'un pion n°2 sur la ligne du bas
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
                            y1=taille
                return[[0],[x1,y1],[x2,y2]]            
                for h in range(taille-2*taille):
                    if affiche.g[i+h][j]==1:#selection hasard d'un pion n°2 sur la ligne du droite
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
                            y1=taille
                return[[0],[x1,y1],[x2,y2]]
        
            
            
                                
    
    
    
    
                

        
        




    
    
