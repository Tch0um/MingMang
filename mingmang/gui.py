import main
from random import randint
from affiche import *
import deplacement
from tkinter import *


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
    #premier joueur n'es pas éxecutée si adversaire =2
    #mode :   jcj=1   jciafacile=2    jciadifficile=3     jcjr=4
    adversaire=0
    adversaire=int(input("Choisissez votre mode de jeu : joueur contre joueur local , joueur contre joueur en réseau[1,2]"))
    if adversaire==1:
        tour=1
        mode=1
        main.debutjeu(mode,tour,taille)
    elif adversaire==2:
        tour=1
        mode=randint(1,2)
        main.debutjeu(mode,tour,taille)
    
         

def entreecoord1():
    return int((input("ligne ?")))
            
def entreecoord2():
    return int((input("colonne?")))
    


mingmang=tk()


    


