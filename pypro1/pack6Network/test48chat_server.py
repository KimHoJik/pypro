# 멀티 채팅 서버 : socket, thread

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 5555))
ss.listen(5)
print('채팅 서버 서비스 시작 ...')

users = []  # 채팅 접속 컴의 소켓 저장

def chatUser(conn):
    name = conn.recv(1024)
    data = '^i^' + name.decode('UTF_8') + '님 입장 ^^'
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('UTF_8'))    #모든 접속자에게 채팅명을 전송
        
        while True: # 수다 떨기 메세지를 받아 모든 접속자에게 수다 메세지를 전송
            msg = conn.recv(1024)
            data = name.decode('UTF_8') + '님 메세지:' + msg.decode('UTF_8')
            print(data)
            for p in users:
                p.send(data.encode('UTF_8'))
            
    except:
        users.remove(conn)  # 채팅을 종료한 클라이언트 소켓을 삭제
        data = '~~ ' + name.decode('UTF_8') + '님 퇴장 ~~'
        print(data)
        
        if users:
            for p in users:
                p.send(data.encode('UTF_8'))
        else:
            print('exit')
    
while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target = chatUser, args =(conn,))
    th.start()