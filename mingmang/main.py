import deplacement
from gui import *
from random import randint
from affiche import *


def init():
    choixtaille()


def debutjeu(mode,tour,taille):
    if mode==1:
        deplacement.jcj(tour,taille)
    elif mode==4:
        deplacement.jcjr(tour,taille)

def toursuivant(mode,tour,taille):
    if tour==1:
        tour=2
    elif tour==2:
        tour=1
    affiche()
    debutjeu(mode,tour,taille)
    
    
    
    

