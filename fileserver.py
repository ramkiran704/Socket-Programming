import socket
import threading
import os

def handle_client(conn,addr):
    print("Client connected,addr")
    filename=conn.recv(1024).decode()
    pid=os.ggetpid()
    try:
        file=open(filename,"r")
        content=file.read()
        file.close()

        message="Server PID :"+str(pid)+"\n"
        message+="\n"+content
    except FileNotFoundError:
        message="server PID:"+str(pid)+"\n"
        message_="file not found:"+filename
    conn.send(message.encode())
    conn.close()
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5000))
server.listen(1)
print("Server is Listening.......")
print("Waiting for Clients.......")
while True:
    conn,addr=server.accept()
    thread=threading.Thread(target=handle_client,args=(conn,addr))
    thread.start()
    