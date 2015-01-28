#!/usr/bin/python 
import socket 

port = raw_input('Su quale porta apri il servizio?\n> ') 
queuelen = 5 
buflen = 80 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('',int(port))) 
s.listen(queuelen)
try:
    while True: 
        client, (remhost, remport) = s.accept()
        print ('Servizio attivo con '+remhost)
        data = client.recv(buflen) 
        if data: 
            client.send(data)
        print ('Stringa scambiata: '+data)
        client.close()
        print ('Servizio concluso')
except KeyboardInterrupt:
    print('\n*** Interruzione!')
