from main import *
from gui import *
#0=vide 1=blanc 2=noir
#LES NOIRS COMMENCENT TOUJOURS
#tour=0-> joueur 1 propriétaire        tour=1-> joueur 2 invité (ou ia)
################################ VERIFICATIONS VICTOIRE ###############################
def verifpions(g):
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
#def verifdeplacement(coord1,coord2):



                
############################ JOUEUR CONTRE JOUEUR EN LOCAL ############################



def jcj(tour):
    print("debutpartie jcj")
    
    
    
    
    
    
    












############################ JOUEUR CONTRE IA FACILE############################

def jciafacile(tour):
    print("jeuia facile")





############################ JOUEUR CONTRE IA DIFFICILE############################


def jciadifficile(tour):
    print("jeuiadifficile")


############################ JOUEUR CONTRE JOUEUR EN RESEAU ############################


def jcjr(tour):
    print("jcj en réseau")















