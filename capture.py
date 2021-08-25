import socket
from emoji import demojize

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'and3ru'
token = 'oauth:y047vzp3ac09vm3r6p49rkuk4bip8z'
channel = '#pimpimenta'

sock = socket.socket()

class CaptureText():
    def __init__(self):
        sock.connect((server, port))
        sock.send(f"PASS {token}\r\n".encode('utf-8'))
        sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
        sock.send(f"JOIN {channel}\r\n".encode('utf-8'))
    def get_text(self, serv = sock):
        try:
            while True:
                resp = serv.recv(2048).decode('utf-8')
                if resp.startswith('PING'):
                    sock.send("PONG\n".encode('utf-8'))
                elif len(resp) > 0:
                    print(demojize(resp))
                    return demojize(resp)
        except KeyboardInterrupt:
            sock.close()
            exit()
