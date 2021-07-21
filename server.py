import socket

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
    msg='welcome to server'
    msg=f'{len(msg):<{HEADERSIZE}}'+msg

    clientsocket.send(bytes(msg, 'utf-8'))
    clientsocket.close()
