import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5555))
client.send("Hi".encode())
reply=client.recv(1024).decode()
print(reply)
client.close()
