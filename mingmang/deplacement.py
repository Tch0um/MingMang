from main import *
from gui import *
from affiche import *
import affiche



#0=vide 1=blanc 2=noir
#LES NOIRS COMMENCENT TOUJOURS
#tour=0-> joueur 1 propriétaire        tour=1-> joueur 2 invité (ou ia)
################################ VERIFICATIONS VICTOIRE ###############################
def verifvictoirepions():
    noirs=0
    blancs=0
    for i in affiche.g:
        for j in i:
            if j==1:
                blanc+=1
            if j==2:
                noirs+=1
    if blancs==0:
        print("victoire des noirs")
    elif noirs==0:
        print("victoire des blancs")
    else:
        verifarea()

def verifdeplacement(coord1,coord2,tour):
    if int(coord1[0])-int(coord2[0])!=0 and int(coord1[1])-int(coord2[1])!=0 :
        print("déplacement invalide : vous ne pouvez bouger qu'en ligne ou colonne")
        return False
    
    if affiche.g[(coord2[0])][(coord2[1])]!=0:
        print("vous ne pouvez pas déplacer votre pion sur un autre pion")
        return False

    if abs(((coord1[0])-(coord2[0]))) >1 or abs(((coord1[1])-(coord2[1]))) >1:
        if ((coord1[0])-(coord2[0])) !=0:
            print ("déplacement en colonne")
            if (coord1[0])>(coord2[0]):#déplacement vers le haut ,on compte donc de coord2->coord1
                for i in range (1,(coord1[0])-(coord2[0])):
                    print("deplacement vers le haut")
                    print("case",i,"=",affiche.g[coord1[0]][coord1[1]+i])
                    if affiche.g[coord2[0]+i][coord2[1]] !=0:
                        return False
                    else:
                        return True
            if (coord2[0])>(coord1[0]):#déplacement vers le bas , on compte donc de coord1->coord2
                for i in range (((coord2[0])-(coord1[0]))-1):
                    print("deplacement vers le bas")
                    print("case",i,"=",affiche.g[coord1[0]][coord1[1]+i])
                    if affiche.g[coord1[0]][coord1[1]+i] !=0:
                        return False
                    else:
                        return True
        if ((coord1[1])-(coord2[1])) !=0:
            print ("déplacement en ligne")
            if (coord1[1])>(coord2[1]):#déplacement vers la gauche ,on compte donc de coord2->coord1
                for i in range (1,(coord1[1])-(coord2[1])):
                    print("deplacement vers la gauche")
                    print("case",i,"=",affiche.g[coord1[0]][coord1[1]+i])
                    if affiche.g[coord2[0]][coord2[1]+i] !=0:
                        return False
                    else :
                        return True
            if (coord2[1])>(coord1[1]):#déplacement vers la droite , on compte donc de coord1->coord2
                for i in range (((coord2[1])-(coord1[1]))-1):
                    print("deplacment vers la droite")
                    print("case",i,"=",affiche.g[coord1[0]][coord1[1]+i])
                    if affiche.g[coord1[0]+i][coord1[1]] !=0:
                        return False
                    else :
                        return True






    else:
        return True
    
    
    

        



        
#doit verifier que le déplacement se fait en ligne ou en colonne et aps les deux en meme temps
#doit verifier si on ne traverse pas uen autre piece,
#occupée par un autre pion , deplacement sur la meme case






                
############################ JOUEUR CONTRE JOUEUR EN LOCAL ############################



def jcj(tour):
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
        jcj(tour)
    print("choisissez ou déplacer votre pion")
    coord2[0]=entreecoord1()
    coord2[1]=entreecoord2()
    print(coord2)
    if coord1[0]==coord2[0] and coord1[1]==coord2[1]:
        print("le joueur",tour,"passe son tour")
        #passetour(mode,tour)
    if verifdeplacement(coord1,coord2,tour):
        (affiche.g[coord1[0]][coord1[1]])=0
        (affiche.g[coord2[0]][coord2[1]])=int (tour)
        toursuivant(mode,tour)
        #capture(coord2)
        #victoirezone()
        #victoirepions()
    else:
        print("déplacement invalide")
        jcj(tour)



    
    """coord1=(0,0)
    coord2=(0,0)
    mode=1
    print("au tour du joueur",tour)
    print("entrez la coordonée y du pion a déplacer")
    coord1[0]=entreecoord()
    for i in range (len(coord1)-1):
        if coord1[i]==" ":
            del coord1[i]
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != int(tour):
        print("selection invalide , vous devez choisir un de vos pions")
        jcj(tour)
    print("entrez les coordonées de la case ou déplacer le pion")
    coord2=entreecoord()
    #for i in range (len(coord2)-1):
        #if coord2[i]==" ":
            #del coord2[i]
    if verifdeplacement(coord1,coord2,tour)==True:
        (affiche.g[coord1[0]][coord1[1]])=0
        (affiche.g[coord2[0]][coord2[1]])=int (tour)
        print("ca marche , cases déplacées")
        #testcapture(coord2)
        #verifvictoirepions()
        toursuivant(mode,tour)
    else:
        print ("déplacement invalide")
        jcj(tour)"""
        
        







############################ JOUEUR CONTRE IA FACILE############################

def jciafacile(tour):
    print("jeuia facile")




############################ JOUEUR CONTRE IA DIFFICILE############################


def jciadifficile(tour):
    print("jeuiadifficile")


############################ JOUEUR CONTRE JOUEUR EN RESEAU ############################


def jcjr(tour):
    print("jcj en réseau")
























"""def verifdeplacement(coord1,coord2,tour):
    coord1[0]= int(coord1[0])
    coord1[1]= int(coord1[1])
    coord2[0]= int(coord2[0])
    coord2[1]= int(coord2[1])
    
    if int(coord1[0])-int(coord2[0])!=0 and int(coord1[1])-int(coord2[1])!=0 :
        print("déplacement invalide : vous ne pouvez bouger qu'en ligne ou colonne")
        return False
    
    if coord1==coord2:
        #déplacement sur la même case
        return False
    
    if affiche.g[int(coord2[0])][int(coord2[1])]!=0:
        print("vous ne pouvez pas déplacer votre pion sur un autre pion")
        return False

    if abs(((coord1[0])-(coord2[0]))) >1 or abs(((coord1[1])-(coord2[1]))) >1:
        if ((coord1[0])-(coord2[0])) !=0:
            print ("déplacement en colonne")
            if (coord1[0])>(coord2[0]):#déplacement vers le haut ,on compte donc de coord2->coord1
                for i in range (1,(coord1[0])-(coord2[0])):
                    if affiche.g[coord2[0]+i][coord2[1]] !=0:
                        return False
                    else:
                        return True
            if (coord2[0])>(coord1[0]):#déplacement vers le bas , on compte donc de coord1->coord2
                for i in range (1,(coord2[0])-(coord1[0])):
                    if affiche.g[coord1[0]][coord1[1]+i] !=0:
                        return False
                    else:
                        return True
        if ((coord1[1])-(coord2[1])) !=0:
            print ("déplacement en ligne")
            if (coord1[1])>(coord2[1]):#déplacement vers la gauche ,on compte donc de coord2->coord1
                for i in range (1,(coord1[1])-(coord2[1])):
                    if affiche.g[coord2[0]][coord2[1]+i] !=0:
                        return False
                    else :
                        return True
            if (coord2[1])>(coord1[1]):#déplacement vers la droite , on compte donc de coord1->coord2
                for i in range (1,(coord2[1])-(coord1[1])):
                    if affiche.g[coord1[0]+i][coord1[1]] !=0:
                        return False
                    else :
                        return True
    else:
            return True"""



