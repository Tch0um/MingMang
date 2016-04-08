from main import *
from gui import *
from affiche import *
import affiche



#0=vide 1=blanc 2=noir
#LES NOIRS COMMENCENT TOUJOURS
#tour=0-> joueur 1 propriétaire        tour=1-> joueur 2 invité (ou ia)
################################ VERIFICATIONS VICTOIRE ###############################
def verifvictoirepions(g):
    noirs=0
    blancs=0
    for i in g:
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
        
#def verifarea(g)     
def verifdeplacement(coord1,coord2,tour):
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
    """if coord1[0]<coord2[0]:
        for i in range ((coord2[0])-(coord1[0])):#1
            if (affiche.g[coord1[0]+i][coord2[0]])!=0:
                return False
    elif coord1[0]>coord2[0]:
        for i in range ((coord1[0])-(coord2[0])):#2
             if (affiche.g[coord1[0]+i][coord2[0]])!=0:
                return False
    if coord1[1]<coord2[1]:
        for i in range ((coord2[1])-(coord1[1])):#3
            if (affiche.g[coord1[0]][coord2[0]+i])!=0:
                return False
    elif coord1[1]>coord2[1]:
        for i in range ((coord1[1])-(coord2[1])):#4
            if (affiche.g[coord1[0]][coord2[0]+i])!=0:
                return False"""
    return True

        
#doit verifier que le déplacement se fait en ligne ou en colonne et aps les deux en meme temps
#doit verifier si on ne traverse pas uen autre piece,
#occupée par un autre pion , deplacement sur la meme case
#





                
############################ JOUEUR CONTRE JOUEUR EN LOCAL ############################



def jcj(tour):
    mode=1
    print("au tou du joueur",tour)
    print("entrez les coordonées du pion a déplacer x y ex : 1 12")
    coord1=entreecoord()
    for i in range (len(coord1)-1):
        if coord1[i]==" ":
            del coord1[i]
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != tour:
        print("vous ne pouvez pas bouger le pion de votre adversaire !")
        jcj(tour)
    print("entrez les coordonées de la case ou déplacer le pion")
    coord2=entreecoord()
    for i in range (len(coord2)-1):
        if coord2[i]==" ":
            del coord2[i]
    if verifdeplacement(coord1,coord2,tour)==True:
        (affiche.g[coord1[0]][coord1[1]])=0
        (affiche.g[coord2[0]][coord2[1]])=int (tour)
        print("ca marche , cases déplacées")
        testcapture(coord2)
    toursuivant(mode,tour)
        
        
        







############################ JOUEUR CONTRE IA FACILE############################

def jciafacile(tour):
    print("jeuia facile")




############################ JOUEUR CONTRE IA DIFFICILE############################


def jciadifficile(tour):
    print("jeuiadifficile")


############################ JOUEUR CONTRE JOUEUR EN RESEAU ############################


def jcjr(tour):
    print("jcj en réseau")















