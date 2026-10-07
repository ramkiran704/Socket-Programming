import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5010))
print("Client Sarted.")
while True:
    message=input("Enter Message:")
    if message.lower()=="exit":
        break
    else:
        client.send(message.encode())
        data=client.recv(1024)
        print("Server says:",data.decode())
client.close()