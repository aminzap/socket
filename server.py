import socket
import pickle

HEADERSIZE = 10
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

while True:
    clientsocket, address = server.accept()
    print(f'connection from {address} was established')
    # header: notify how long is your message and some informations about it
    msg = {'a': 'amin',
           'b': 'babak',
           'c': 'cyndi'}
    msg=pickle.dumps(msg)
    msg=bytes(f'{len(msg):<{HEADERSIZE}}','utf-8')+msg

    clientsocket.send(msg)

