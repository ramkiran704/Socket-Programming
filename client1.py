import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",5102))
client.send("Hello Server".encode())
reply=client.recv(1024).decode()
print("Server says:",reply)
client.close()