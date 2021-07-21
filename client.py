import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname(socket.gethostname()), 5050))
while True:
    fullmsg = ''
    new_msg = True
    while True:
        msg = s.recv(HEADERSIZE + 5)
        if new_msg:
            print(f'new message length is:{msg[:HEADERSIZE]}')
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
        fullmsg += msg.decode('utf-8')
        if len(fullmsg) - HEADERSIZE == msg_len:
            print('full message received!')
            print(f'your message is {fullmsg[HEADERSIZE:]}')
            new_msg = True
            fullmsg=''

    print(message)
