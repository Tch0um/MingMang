import deplacement
from gui import *
from random import randint
from affiche import *

##
# Fonction de lancement du jeu
def init():
    choixtaille()

##
# fonction définissant le mode de jeu a lancer
# @param mode: désigne l'un des trois mode de jeu par un nombre
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau 
def debutjeu(mode,tour,taille,nbtour):
    if mode==1:
        deplacement.jcj(tour,taille,nbtour)
    elif mode==2:
        deplacement.jcjr(tour,taille,nbtour)
    elif mode==3:
        deplacement.jcia(tour,taille,nbtour)

##
# fonction lancant le tour suivant
# @param mode: désigne l'un des trois mode de jeu par un nombre
# @param tour: détermine qui doit jouer
# @param taille: définis la dimension du plateau 
def toursuivant(mode,tour,taille,nbtour):
    nbtour+=1
    if tour==1:
        tour=2
    elif tour==2:
        tour=1
    debutjeu(mode,tour,taille,nbtour)
    
    
    
    

