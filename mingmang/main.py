import deplacement
from gui import *
from random import randint
from affiche import *


def init():
    choixtaille()


def debutjeu(mode,tour,taille,nbtour):
    if mode==1:
        deplacement.jcj(tour,taille,nbtour)
    elif mode==2:
        deplacement.jcjr(tour,taille,nbtour)
    elif mode==3:
        deplacement.jcia(tour,taille,nbtour)

def toursuivant(mode,tour,taille,nbtour):
    nbtour+=1
    if tour==1:
        tour=2
    elif tour==2:
        tour=1
    debutjeu(mode,tour,taille,nbtour)
    
    
    
    

