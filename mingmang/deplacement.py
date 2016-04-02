from main import *
from gui import *

#pj=0-> joueur 1 propriétaire        pj=1-> joueur 2 invité (ou ia)
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

def verifarea(g)
    
                
############################ JOUEUR CONTRE JOUEUR EN LOCAL ############################
def jcj(tour):
    












############################ JOUEUR CONTRE IA FACILE############################

def jciafacile():





############################ JOUEUR CONTRE IA DIFFICILE############################


def jciadifficile():


############################ JOUEUR CONTRE JOUEUR EN RESEAU ############################


def jcjr():















