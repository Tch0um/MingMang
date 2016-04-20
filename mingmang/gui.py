import main
from random import randint
from affiche import *
import deplacement


global taille

def choixtaille():
    taille=0
    choixtaille=input("choisissez la taille du plateau : petit(9x9) , classique(19x19) ou grand(29x29) [P/C/G]")
    if choixtaille=="P":
        taille=9
    elif choixtaille=="C":
        taille=19
    elif choixtaille=="G":
        taille=29
    elif choixtaille=="T":
        taille=input("taille ?")
    creegrille(taille)
    choixadversaire(taille)

def choixadversaire(taille):
    nbtour=0
    adversaire=int(input("Choisissez votre mode de jeu : joueur contre joueur local , joueur contre joueur en réseau , joueur contre IA[1,2,3]"))
    if adversaire==1:
        tour=1
        mode=1
        main.debutjeu(mode,tour,taille,0)
    elif adversaire==2:
        tour=randint(1,2)
        mode=2
        main.debutjeu(mode,tour,taille,nbtour)
    elif adversaire==3:
        tour=randint(1,2)
        mode=3
        main.debutjeu(mode,tour,taille,nbtour)
    
         

def entreecoord1():
    return int((input("ligne ?")))
            
def entreecoord2():
    return int((input("colonne?")))
    



    


