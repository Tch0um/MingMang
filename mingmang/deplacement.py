from main import *
from gui import *
from affiche import *
from serveur import *
import affiche
import gui
import math




#0=vide 1=blanc 2=noir
#LES NOIRS COMMENCENT TOUJOURS
#tour=0-> joueur 1 propriétaire        tour=1-> joueur 2 invité (ou ia)
################################ VERIFICATIONS VICTOIRE ###############################
def victoirepions(taille):
    noir=0
    blanc=0
    for i in range(taille):
        for j in range(taille):
            if j==1:
                blanc+=1
            if j==2:
                noir+=1
    return (blanc,noir)

def verifdeplacement(coord1,coord2,tour):
    if int(coord1[0])-int(coord2[0])!=0 and int(coord1[1])-int(coord2[1])!=0 :
        print("déplacement invalide : vous ne pouvez bouger qu'en ligne ou colonne")
        return False
    
    if affiche.g[(coord2[0])][(coord2[1])]!=0:
        print("déplacement invalide : vous ne pouvez pas déplacer votre pion sur un autre pion")
        return False
    
    
    nbmvm=0
    sens=0
    if ((coord1[0])-(coord2[0])) >= 1:
        sens=1
        nbmvm=((coord1[0])-(coord2[0]))
    if ((coord1[1])-(coord2[1])) >= 1:
        sens=2
        nbmvm=((coord1[1])-(coord2[1]))
    if ((coord2[0])-(coord1[0])) >= 1:
        sens=3
        nbmvm=((coord2[0])-(coord1[0]))
    if ((coord2[1])-(coord1[1])) >= 1:
        sens=4
        nbmvm=((coord2[1])-(coord1[1]))

    if nbmvm>=1:
        if sens==4:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]][coord1[1]+i] !=0:
                    return False
            return True
        if sens==3:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]+i][coord1[1]] !=0:
                    return False
            return True
        if sens==2:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]][coord1[1]-i] !=0:
                      return False
            return True
        if sens==1:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]-i][coord1[1]] !=0:
                      return False
            return True

    else:
        return True


def captured(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,taille-coord2[1]):#droite
        if affiche.g[coord2[0]][coord2[1]+i]==tour:
            for x in range(i):
                affiche.g[coord2[0]][coord2[1]+x]=tour
            captureb(coord2,tour,taille)
            break
        if affiche.g[coord2[0]][coord2[1]+i]==0:
            captureb(coord2,tour,taille)
            break

def captureb(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,taille-coord2[0]):#bas
        if affiche.g[coord2[0]+i][coord2[1]]==tour:
            for x in range(i):
                affiche.g[coord2[0]+x][coord2[1]]=tour
            captureg(coord2,tour,taille)
            break
        if affiche.g[coord2[0]][coord2[1]+i]==0:
            captureg(coord2,tour,taille)
            break

def captureg(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,coord2[0]):
        if affiche.g[coord2[0]][coord2[1]-i]==tour:
            for x in range(i):
                affiche.g[coord2[0]][coord2[1]-x]=tour
            captureh(coord2,tour,taille)
            break
        if affiche.g[coord2[0]][coord2[1]-i]==0:
            captureh(coord2,tour,taille)
            break
        
def captureh(coord2,tour,taille):   
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,taille-coord2[0]):
        if affiche.g[coord2[0]-i][coord2[1]]==tour:
            for x in range(i):
                affiche.g[coord2[0]-x][coord2[1]]=tour
            break
        if affiche.g[coord2[0]-i][coord2[1]]==0:
            break


def calculzone(taille):
    #renvoie un tuple(blanc,noir) ou a correspond
    #a la zone détenue par le joueur 1
    #b a la zone détenue par le joueur 2
    #(droite,gauche,haut,bas)
    a=0
    b=0
    for i in range(taille):
        for j in range(taille):
            if affiche.g[i][j]!=0:
                case=[0,0,0,0]
                for k in range(1,taille-j):#droite
                    if affiche.g[i][j+k]!=0:
                          case[0]=affiche.g[i][j+k]
                          
                for k in range(1,j):#gauche
                    if affiche.g[i][j-k]!=0:
                          case[1]=affiche.g[i][j-k]
                          
                for k in range(1,taille-i):#haut
                    if affiche.g[i+k][j]!=0:
                          case[2]=affiche.g[i+k][j]
                          
                for k in range(1,i):#bas
                    if affiche.g[i-k][j]!=0:
                          case[3]=affiche.g[i-k][j]
                          
            if 1 in case == True and 2 in case == False:
                    a+=1
            if 2 in case == True and 2 in case == False:
                    b+=1
    return (a,b)
                
                
            
    

                
############################ JOUEUR CONTRE JOUEUR EN LOCAL ############################



def jcj(tour,taille):
    zonevictoire=(taille*taille)
    print("zone victoire=",zonevictoire)
    zone=calculzone(taille)
    nbpions=victoirepions(taille) 
    coord1=[0,0]
    coord2=[0,0]
    mode=1
    print("au tour du joueur ",tour)
    print("Choisissez un pion a déplacer")
    coord1[0]=entreecoord1()
    coord1[1]=entreecoord2()
    print(coord1)
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != int(tour):
        print("selection invalide , vous devez choisir un de vos pions")
        jcj(tour,taille)
    print("choisissez ou déplacer votre pion")
    coord2[0]=entreecoord1()
    coord2[1]=entreecoord2()
    print(coord2)
    if coord1[0]==coord2[0] and coord1[1]==coord2[1]:
        print("le joueur",tour,"passe son tour")
        toursuivant(mode,tour,taille)
    elif verifdeplacement(coord1,coord2,tour) :#and veriftour(coord1,coord2):
        (affiche.g[coord1[0]][coord1[1]])=0
        (affiche.g[coord2[0]][coord2[1]])=int (tour)
        captured(coord2,tour,taille)
        if zone[0]==(zonevictoire):
            print("territoire des blancs superieure a la moitié du plateau",zone[1]," , victoire des blancs")
        if zone[1]==(zonevictoire):
            print("territoire des noirs superieure a la moitié du plateau ",zone[1],", victoire des noirs")
        if nbpions[0]==0:
            print("victoire des noirs")
        if nbpions[1]==0:
            print("victoire es blancs")
        else:
            toursuivant(mode,tour,taille)
    else:
        jcj(tour,taille)


        
        
############################ JOUEUR CONTRE JOUEUR EN RESEAU ############################


def jcjr(tour,taille):
    zonevictoire=(taille*taille)
    print("zone victoire=",zonevictoire)
    zone=calculzone(taille)
    nbpions=victoirepions(taille) 
    coord1=[0,0]
    coord2=[0,0]
    mode=1
    print("au tour du joueur ",tour)
    print("Choisissez un pion a déplacer")
    coord1[0]=entreecoord1()
    coord1[1]=entreecoord2()
    print(coord1)
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != int(tour):
        print("selection invalide , vous devez choisir un de vos pions")
        jcj(tour,taille)
    print("choisissez ou déplacer votre pion")
    coord2[0]=entreecoord1()
    coord2[1]=entreecoord2()
    print(coord2)
    if coord1[0]==coord2[0] and coord1[1]==coord2[1]:
        print("le joueur",tour,"passe son tour")
        toursuivant(mode,tour,taille)
    elif verifdeplacement(coord1,coord2,tour) :#and veriftour(coord1,coord2):
        (affiche.g[coord1[0]][coord1[1]])=0
        (affiche.g[coord2[0]][coord2[1]])=int (tour)
        captured(coord2,tour,taille)
        if zone[0]==(zonevictoire):
            print("territoire des blancs superieure a la moitié du plateau",zone[1]," , victoire des blancs")
        if zone[1]==(zonevictoire):
            print("territoire des noirs superieure a la moitié du plateau ",zone[1],", victoire des noirs")
        if nbpions[0]==0:
            print("victoire des noirs")
        if nbpions[1]==0:
            print("victoire es blancs")
        else:
            toursuivant(mode,tour,taille)
    else:
        jcj(tour,taille)
    










