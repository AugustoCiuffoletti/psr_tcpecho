import socket
host = input('Scegli un host: ')
port = input('Scegli una porta: ')
buflen = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creazione del socket 
s.connect((host,int(port)))                            # Connessione (3-way handsake)
msg = input('Stringa da spedire: ')
s.send(msg.encode('utf8'))                                            # Spedizione messaggio
data = s.recv(buflen).decode('utf8')                                  # Attesa risposta
print('Stringa ricevuta: '+data)
s.close()                                              # Chiusura socket
