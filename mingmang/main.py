import deplacement
from gui import *
from random import randint
from affiche import *

def init():
    choixtaille()


def debutjeu(mode,tour):
    if mode==1:
        deplacement.jcj(tour)
    elif mode==2:
        deplacement.jciafacile(tour)
    elif mode==3:
        deplacement.jciadifficile(tour)
    elif mode==4:
        deplacement.jcjr(tour)

def toursuivant(mode,tour):
    print("changement du tour")
    if tour==1:
        tour=2
    elif tour==2:
        tour=1
    affiche()
    debutjeu(mode,tour)
    
    
    

