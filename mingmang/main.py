from affiche import *
#from deplacement import *
from gui import *
from random import randint

def init():
    """interface console , l'utilisateur choisit la taille de son plateau, la
       taille du plateau est ensuite envoyé a la fonction creegrille dans
       le module affiche et genere le plateu dans la console """
    taille=0
    choixtaille=input("choisissez la taille du plateau : petit , classique ou grand [P/C/G]")
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
        niveauIA=input("Choisissez votre adversaire IA : Jean-Kevin(Facile) , Satan(Difficile) [1/2]")
    definejoueurs(adversaire,niveauIA)
    
def definejoueurs(adversaire):
    #doit dire qui prendra les pions blanc
    #les pions blanc commence toujours
    #1=joueur local   2= 2éme joueur local ou IA
    adversaire=int(adversaire)
    choixpremierjoueur=input("Quelle couleur choisissez-vous ? Blanc , Noir , Aléatoire [B/N/A]")
    if choixpremierjoueur=="A":
        premierjoueur=randint(1,2)
    if choixpremierjoueur=="B":
        premierjoueur=1
    if choixpremierjoueur=="N":
        premierjoueur=2
    if adversaire==1 :
        if premierjoueur==1:
            print("Vous jouerez les Blancs et commencerez en premier , l'IA jouera les Noirs")
        elif premierjoueur==2:
            print("L'IA jouera les Blancs et commencera en premiére , vous jouerez les Noirs")
    else:
        if premierjoueur==1:
            print("Vous jouerez les Blancs et commencerez en premier , le second joueur jouera les Noirs")
        elif premierjoueur==2:
            print("Le second joueurs jouera les Blancs et commencera en premier , vous jouerez les Noirs")
    if 

                   
    

    
        
    
        
        
    
    
    
    
    







                          

