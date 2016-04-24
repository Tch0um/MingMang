import socket


def affiche():
    res=""
    for i in g:
        for j in i:
            res+=str(j)+" "
        res+="\n"
    print (res)
