from deplacement import *
from gui import *
from random import randint



def init():
    choixtaille()


    


    


























    
    """interface console , l'utilisateur choisit la taille de son plateau, la
       taille du plateau est ensuite envoyé a la fonction creegrille dans
       le module affiche et genere le plateu dans la console 
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
    adversaire=0
    adversaire=int(input("choisissez votre adversaire: IA , 2éme joueur humain , 2éme joueur humain en réseau [1,2,3]"))
    if adversaire==1:
        niveauia=int(input("Choisissez le niveau de l'IA : Facile , Difficile [1/2]"))
    if adversaire==2:
        tour=0
        jcj(tour)
    else:
        premierjoueur(adversaire,niveauia)
        
    
def premierjoueur(adversaire,niveauia):
    #  1=joueur local  2=IA ou joueur en réseau
    pj=randint(0,1) # determine le premier joueur , on prédifinit avant a l'oral qui sera 1 et 2
    if pj==0:
        if adversaire==3:
            print("Vous commencez a jouer avec les pions blancs! L'adversaire jouera les pions noirs")
            jcjr(pj)
        elif adversaire==1:
            print("Vous commencez a jouer avec les pions blancs! L'IA jouera les pions noirs")
            if niveauia==1:
                jciafacile(pj)
            elif niveauia==2:
                jciadifficile(pj)

    if pj==1:
        if adversaire==3:
            print("Votre adversaire commence a jouer avec les pions blancs ! Vous jouerez les pions noirs")
            jcjr(pj)
        elif adversaire==1:
            print("L'IA commence a jouer avec les pions blancs! Vous jouerez les pions noirs")
            if niveauia==1:
                jciafacile(pj)
            elif niveauia==2:
                jciadifficile(pj)
                """
    
    

    
                   
    

    
        
    
        
        
    
    
    
    
    







                          

