from affiche import *

def init():
    taille=0
    choixtaille=input("choisissez la taille du plateau : petit , classique ou grand [P/C/G]")
    if choixtaille=="P":
        taille=9
    if choixtaille=="C":
        taille=19
    if choixtaille=="G":
        taille=29
    if choixtaille=="T":
        taille=input("taille ?")

    creegrille(taille)


                          

