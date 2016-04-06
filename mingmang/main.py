import deplacement
from gui import *
from random import randint
from affiche import *
import affiche

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

def toursuivant(tour):
    if tour==1:
        tour=2
    if tour==2:
        tour=1
    affiche.affiche(g)
    

