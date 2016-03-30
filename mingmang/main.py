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
    adversaire=0
    adversaire=input("Contre qui souhaitez vous jouer : IA , 2éme joueur humain , 2éme joueur humain en réseau [1,2,3]")
    if adversaire==1:
        global niveauIA=input("Choisissez votre adversaire IA : Jean-Kevin(Facile) , Satan(Difficile) [1/2]")
    if adversaire==2:
        tourjoueurlocal():
    else:
        definecouleur(adversaire)
    
def definecouleur(adversaire,niveauIA):
    #doit dire qui prendra les pions blanc
    #les pions blanc commence toujours
    #1=joueur local   2= 2éme joueur local ou IA
    #premier : 1=IA 2=deux joueurs local 3=deux joueurs en réseau
    
    
    

    
                   
    

    
        
    
        
        
    
    
    
    
    







                          

