# 단순 Client

import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(('192.168.0.10', 7878))  # acorn 변경 주소
clientSock.sendall('김호직'.encode('UTF_8'))
re_msg = clientSock.recv(1024).decode()
print('수신 자료 : ', re_msg)
clientSock.close()
