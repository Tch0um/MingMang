#GORON Nathan 21503237

import socket

socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('',15555))

while True:
    socket.listen(5)
    client, address = socket.accept()

    reponse = client.rcv(255)
    if reponse !="exe":
    socket.listen(1)
        

    
    
    








