from main import *
from random import randint
from affiche import *
import deplacement

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
    choixadversaire()

def choixadversaire():
    #premier joueur n'es pas éxecutée si adversaire =2
    #mode :   jcj=1   jciafacile=2    jciadifficile=3     jcjr=4
    adversaire=0
    adversaire=int(input("choisissez votre adversaire: IA , 2éme joueur humain , 2éme joueur humain en réseau [1,2,3]"))
    if adversaire==1:
        niveauia=int(input("Choisissez le niveau de l'IA : Facile , Difficile [1/2]"))
    if adversaire==2:
        tour=0
        mode=1
        debutjeu(mode,tour)
    else:
        premierjoueur(adversaire,niveauia)
         
def premierjoueur(adversaire,niveauia):
    #  0=joueur local  1=IA ou joueur en réseau
    tour=randint(0,1) # determine le premier joueur , on prédifinit avant a l'oral qui sera 1 et 2
    if tour==0:
        if adversaire==3:
            print("Vous commencez a jouer avec les pions blancs! L'adversaire jouera les pions noirs")
            mode=4
            debutjeu(mode,tour)
        elif adversaire==1:
            print("Vous commencez a jouer avec les pions blancs! L'IA jouera les pions noirs")
            if niveauia==1:
                mode=2
                debutjeu(mode,tour)
            elif niveauia==2:
                mode=3
                debutjeu(mode,tour)
    if tour==1:
        if adversaire==3:
            print("Votre adversaire commence a jouer avec les pions blancs ! Vous jouerez les pions noirs")
            mode=4
            debutjeu(mode,tour)
        elif adversaire==1:
            print("L'IA commence a jouer avec les pions blancs! Vous jouerez les pions noirs")
            if niveauia==1:
                mode=2
                debutjeu(mode,tour)
            elif niveauia==2:
                mode=3
                debutjeu(mode,tour)


def debutjeu(mode,tour):
    if mode==1:
        deplacement.jcj(tour)
    elif mode==2:
        deplacement.jciafacile(tour)
    elif mode==3:
        deplacement.jciadifficile(tour)
    elif mode==4:
        deplacement.jcjr(tour)

def entreecoord():


