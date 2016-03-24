from affiche import *
from deplacement import *
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

def debutdeplacement():
    premierjoueur=0
    choixpremierjoueur=0
    choixpremierjoueur=input("Quel joueur commence : Blanc , Noir , Aléatoire  [B/N/A]")
    if choixpremierjoueur=="A":
        premierjoueur=randint(1,2)
    elif choixpremierjoueur=="N":
        premierjoueur=1
    elif choixpremierjoueur=="B":
        premierjoueur=2
    deplacement(premierjoueur)

    
        
    
        
        
    
    
    
    
    







                          

