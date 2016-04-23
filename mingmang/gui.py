import main
from random import randint
from affiche import *
import deplacement
import affiche


global taille

def choixtaille():
    taille=0
    choixtaille=input("choisissez la taille du plateau : petit(9x9) , classique(19x19) , grand(29x29) ou éditer votre propre plateau [P/C/G/E]")
    if choixtaille=="P":
        taille=9
    elif choixtaille=="C":
        taille=19
    elif choixtaille=="G":
        taille=29
    if choixtaille=="E":
        print()
        print("                   Editeur de plateau")
        print()
        editplateau()
    else:  
        creegrille(taille)
        choixadversaire(taille)
    
def editplateau():
    print("Choisissez la taille de votre plateau")
    taille=int(input('>>'))
    creegrille(taille)
    coordo=[0,0]
    couleur=1
    for i in range (taille):
        for j in range (taille):
            affiche.g[i][j]=0
    while couleur!=0:
        affiche.affiche()
        print("entrez la couleur du pion a placer (1 ou 2) ou taper 0 pour lancer la partie")
        couleur=int(input(">>"))
        if couleur==0:
            choixadversaire(taille)
        else:
            print("entrez les coordonnées du pion a placer sous la forme suivante :[x,y] ")
            coordo[0]=int(input("ligne ? \n >>"))
            coordo[1]=int(input("colonne ? \n >>"))
            print(couleur)
            print(coordo)
            affiche.g[coordo[0]][coordo[1]]=couleur
                      
        
    
    
    
    
    
def choixadversaire(taille):
    nbtour=0
    adversaire=int(input("Choisissez votre mode de jeu : joueur contre joueur local , joueur contre joueur en réseau , joueur contre IA[1,2,3]"))
    if adversaire==1:
        tour=1
        mode=1
        main.debutjeu(mode,tour,taille,0)
    while adversaire==2:
        print("\n Navré , Le mode joueur contre joueur en réseau n'est pas fonctionnel \n")
        choixadversaire(taille)
        """tour=randint(1,2)
        mode=2
        main.debutjeu(mode,tour,taille,nbtour)"""
    if adversaire==3:
        if taille==9 or taille==19 or taille==29:
            tour=randint(1,2)
            mode=3
            main.debutjeu(mode,tour,taille,nbtour)
        else:
            print("\n Le mode IA n'est aps compatible avec un plateau personnalis \n")
            choixadversaire(taille)
        
    
         

def entreecoord1():
    ligne=input("ligne?")
    if ligne=='save':
        print("sauvegarde de la partie")
        return ligne
    elif ligne=='load':
        print("chargement de la partie")
        return ligne
    else:
        return int(ligne)
            
def entreecoord2():
    return int((input("colonne?")))
    



    


