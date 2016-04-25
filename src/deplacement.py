#GORON Nathan 21503237

from main import *
from gui import *
from affiche import *
from serveur import *
import affiche
import gui
import math
import pickle as pic
from ia import *




################################ VERIFICATIONS VICTOIRE ###############################

##
# compte les pions de chaque joueur sur le plateau
# @param taille: dimension du plateau
# #return: Un tuple avec le nombre de pions noirs et blancs
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
##
# Verifie toutes les modalitées de déplacement
# @param coord1: coordonées du pion a déplacer
# @param coord2: coordonées cible du pion sélectionné
# @return: True si le mouvement est autorisé False sinon
def verifdeplacement(coord1,coord2,tour):
    if int(coord1[0])-int(coord2[0])!=0 and int(coord1[1])-int(coord2[1])!=0 :
        print("déplacement invalide : vous ne pouvez bouger qu'en ligne ou colonne")
        return False
    
    if affiche.g[(coord2[0])][(coord2[1])]!=0:
        print("déplacement invalide : vous ne pouvez pas déplacer votre pion sur un autre pion ni revenir sur un position précedente")
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
                    print("déplacement invalide , vous ne pouvez pas déplacer un pion par dessus un autre")
                    return False
            return True
        if sens==3:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]+i][coord1[1]] !=0:
                    print("déplacement invalide , vous ne pouvez pas déplacer un pion par dessus un autre")
                    return False
            return True
        if sens==2:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]][coord1[1]-i] !=0:
                    print("déplacement invalide , vous ne pouvez pas déplacer un pion par dessus un autre")
                    return False
            return True
        if sens==1:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]-i][coord1[1]] !=0:
                    print("déplacement invalide , vous ne pouvez pas déplacer un pion par dessus un autre")
                    return False
            return True

    else:
        return True

##
# Effectue la capture des pions vers la droite
# @param coord2: coordonée d'arrivée du pion
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
def captured(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1
    for i in range(1,taille-coord2[1]):
        if affiche.g[coord2[0]][coord2[1]+i]==tour:
            for x in range(i):
                affiche.g[coord2[0]][coord2[1]+x]=tour
            captureb(coord2,tour,taille)
            break
        if affiche.g[coord2[0]][coord2[1]+i]==0:
            captureb(coord2,tour,taille)
            break

##
# Effectue la capture des pions vers le bas
# @param coord2: coordonée d'arrivée du pion
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
def captureb(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1
    for i in range(1,taille-coord2[0]):
        if affiche.g[coord2[0]+i][coord2[1]]==tour:
            for x in range(i):
                affiche.g[coord2[0]+x][coord2[1]]=tour
            captureg(coord2,tour,taille)
            break
        if affiche.g[coord2[0]+i][coord2[1]]==0:
            captureg(coord2,tour,taille)
            break
        
##
# Effectue la capture des pions vers la gauche
# @param coord2: coordonée d'arrivée du pion
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
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

##
# Effectue la capture des pions vers le haut
# @param coord2: coordonée d'arrivée du pion
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau   
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

##
# @param taille:définis la dimension du plateau
# @return :renvoie un tuple(blanc,noir) ou a correspond a la zone détenue par le joueur 1 et b a la zone détenue par le joueur 2
def calculzone(taille):
    a=0
    b=0
    for i in range(taille):
        for j in range(taille):
            if affiche.g[i][j]!=0:
                case=[0,0,0,0]
                for k in range(1,taille-j):
                    if affiche.g[i][j+k]!=0:
                          case[0]=affiche.g[i][j+k]
                          
                for k in range(1,j):
                    if affiche.g[i][j-k]!=0:
                          case[1]=affiche.g[i][j-k]
                          
                for k in range(1,taille-i):
                    if affiche.g[i+k][j]!=0:
                          case[2]=affiche.g[i+k][j]
                          
                for k in range(1,i):
                    if affiche.g[i-k][j]!=0:
                          case[3]=affiche.g[i-k][j]
                          
            if 1 in case == True and 2 in case == False:
                    a+=1
            if 2 in case == True and 2 in case == False:
                    b+=1
    return (a,b)
                

##
# verifie si un joueur n'effectue pas un déplacement non-autorisé en revenant sur une case d'un tour prédecent
# @param tour: détermine qui doit jouer
# @param coord1: coordonée d'un pion a déplacer
# @param coord2: coordonée d'arrivée du pion
# @param nbtour: définis le numero du tour actuel
# @return :True si le déplacement est illégal False sinon
def veriftour (tour,nbtour,coord1,coord2):
    if nbtour <=2 and tour==1:
        precoord1j1=coord1
        preccord2j1=coord2
        return True
    if nbtour <=2 and tour==2:
        precoord1j2=coord1
        precoord2j2=coord2
        return True

    if nbtour >=3 and tour==1:
        if coord1==precoord2j1 and coord2==precoord1j1:
            return False
        else:
            precoord1j1=coord1
            precoord2j1=coord2
            return True
    if nbtour >=3 and tour==2:
        if coord1==precoord2j2 and coord2==precoord1j2:
            return False
        else:
            precoord1j2=coord1
            precoord2j2=coord2
            return True
        
    

                
############################ JOUEUR CONTRE JOUEUR EN LOCAL ############################


##
# gére le tour d'un joueur en mode joueur contre joueur
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
# @param nbtour: définis le numero du tour actuel
def jcj(tour,taille,nbtour):
    affiche.affiche()
    zonevictoire=(taille*taille)
    zone=calculzone(taille)
    nbpions=victoirepions(taille) 
    coord1=[0,0]
    coord2=[0,0]
    mode=1
    print("                 Au tour du joueur ",tour )
    print("Choisissez un pion a déplacer")
    coord1[0]=entreecoord1()
    if coord1[0]=='save':
        sauvegarde(tour,taille,nbtour)
        return True
    if coord1[0]=='load':
        chargement(tour,taille,nbtour)
        return True
    coord1[1]=entreecoord2()
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != int(tour):
        print("selection invalide , vous devez choisir un de vos pions")
        jcj(tour,taille,nbtour)
    print("choisissez ou déplacer votre pion")
    coord2[0]=entreecoord1()
    while coord2[0]>=taille:
        print("coordonée trop grande")
        coord2[0]=entreecoord1()
    coord2[1]=entreecoord2()
    while coord2[0]>=taille:
        print("coordonée trop grande")
        coord2[1]=entreecoord2()
    if coord1[0]==coord2[0] and coord1[1]==coord2[1]:
        print("Le joueur",tour,"passe son tour")
        toursuivant(mode,tour,taille,nbtour)
    elif verifdeplacement(coord1,coord2,tour): 
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
            main.toursuivant(mode,tour,taille,nbtour)
    else:
        jcj(tour,taille,nbtour)

##
# sauvegarde la partie en cours
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
# @param nbtour: définis le numero du tour actuel
def sauvegarde(tour,taille,nbtour):
    saveg=[affiche.g,tour,nbtour,taille]
    save=open('save.txt','wb')
    pic.dump(saveg,save)
    save.close()
    jcj(tour,taille,nbtour)


##
# charge la partie sauvegardée dans le fichier  save.txt
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
# @param nbtour: définis le numero du tour actuel
def chargement(tour,taille,nbtour):
    global g
    load=open('save.txt','rb')
    charge=pic.load(load)
    affiche.g=charge[0]
    tourcharge=charge[1]
    nbtourcharge=charge[2]
    taillecharge=charge[3]
    load.close()
    jcj(tourcharge,nbtourcharge,taillecharge)
    
    
    
    
        

############################ JOUEUR CONTRE JOUEUR EN RESEAU ############################

##
# définit qui doit jouer en fonction de la variable tour
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
# @param nbtour: définis le numero du tour actuel
def jcia(tour,taille,nbtour):
    if tour==1:
        tourjoueur(tour,taille,nbtour)
    else:
        tourclient(tour,taille,nbtour)
        
##
# gére le tour d'un joueur en mode joueur contre joueur en réseau
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
def jcjr(tour,taille):
    zonevictoire=(taille*taille)
    zone=calculzone(taille)
    nbpions=victoirepions(taille) 
    coord1=[0,0]
    coord2=[0,0]
    mode=2
    print("                 Au tour du joueur",tour,"!")
    print()
    print("Choisissez un pion a déplacer")
    coord1[0]=entreecoord1()
    coord1[1]=entreecoord2()
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != int(tour):
        print("selection invalide , vous devez choisir un de vos pions")
        jcj(tour,taille)
    print("choisissez ou déplacer votre pion")
    coord2[0]=entreecoord1()
    coord2[1]=entreecoord2()
    if coord1[0]==coord2[0] and coord1[1]==coord2[1]:
        print("le joueur",tour,"passe son tour")
        toursuivant(mode,tour,taille)
    elif verifdeplacement(coord1,coord2,tour) and veriftour(tour,nbtour,coord1,coord2):
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
            main.toursuivant(mode,tour,taille)
    else:
        jcjr(tour,taille)



############################ JOUEUR CONTRE IA ############################


##
# définit qui doit jouer en fonction de la variable tour
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
# @param nbtour: définis le numero du tour actuel
def jcia(tour,taille,nbtour):
    if tour==1:
        tourjoueur(tour,taille,nbtour)
    else:
        touria(tour,taille,nbtour)
        
##
# gére le tour d'un joueur en mode joueur contre joueur en réseau
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau
# @param nbtour: définis le numero du tour actuel
def tourjoueur(tour,taille,nbtour):
    affiche.affiche()
    zonevictoire=(taille*taille)
    zone=calculzone(taille)
    nbpions=victoirepions(taille) 
    coord1=[0,0]
    coord2=[0,0]
    mode=3
    print("                  A votre tour!")
    print()
    print("Choisissez un pion a déplacer")
    coord1[0]=entreecoord1()
    coord1[1]=entreecoord2()
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != int(tour):
        print("Selection invalide , vous devez choisir un de vos pions")
        tourjoueur(tour,taille,nbtour)
    print("Choisissez ou déplacer votre pion")
    coord2[0]=entreecoord1()
    coord2[1]=entreecoord2()
    if coord1[0]==coord2[0] and coord1[1]==coord2[1]:
        print("Le joueur passe son tour")
        toursuivant(mode,tour,taille,nbtour)
    elif verifdeplacement(coord1,coord2,tour):
        (affiche.g[coord1[0]][coord1[1]])=0
        (affiche.g[coord2[0]][coord2[1]])=int (tour)
        captured(coord2,tour,taille)
        if zone[0]==(zonevictoire):
            print("territoire des blancs superieur a la moitié du plateau , victoire du joueur")
        if zone[1]==(zonevictoire):
            print("territoire des noirs superieur a la moitié du plateau , victoire de l'ia")
        if nbpions[0]==0:
            print("plus de pions blancs , victoire de l'ia")
        if nbpions[1]==0:
            print("plus de piosn noirs , victoire du joueur")
        else:
            main.toursuivant(mode,tour,taille,nbtour)
    else:
        tourjoueur(tour,taille,nbtour)




