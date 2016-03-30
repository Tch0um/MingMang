from affiche import *
#from deplacement import *
from gui import *
from random import randint


#A FAIRE: changer init pour une fonction de type menu ou
#le joueur choisiras entre commencer une nouvelle partie ou charger
#interface avec les régles
def init():
    """interface console , l'utilisateur choisit la taille de son plateau, la
       taille du plateau est ensuite envoyé a la fonction creegrille dans
       le module affiche et genere le plateu dans la console """
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
    adversaire=input("choisissez votre adversaire: IA , 2éme joueur humain , 2éme joueur humain en réseau [1,2,3]")
    if adversaire=="1":
        niveauia=input("Choisissez le niveau de l'IA : Facile , Difficile [1/2]")
    if adversaire=="2":
        jcj1()
    else:
        premierjoueur(adversaire,niveauia)
    
def premierjoueur(adversaire):
    #  1=joueur local  2=IA ou jouer en réseau
    pj=randint(1,2)
    if pj==1:
        if adversaire=="3":
            print("Vous commencez a jouer avec les pions blancs! L'adversaire jouera les pions noirs")
            jcjr1()
        else:
            print("Vous commencez a jouer avec les pions blancs! L'IA jouera les pions noirs")
            jcia()
    else:
        if adversaire=="1":
            print("Votre adversaire commence a jouer avec les pions noirs ! Vous jouerez les pions blancs")
            
        else:
            print("L'IA commence a jouer avec les pions blancs! Vous jouerez les pions noirs")
    
    

    
                   
    

    
        
    
        
        
    
    
    
    
    







                          

