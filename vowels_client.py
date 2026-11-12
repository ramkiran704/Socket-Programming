import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',5000))
inp=input("Enter the word:")
client.send(inp.encode())
response=client.recv(1024).decode()
print(response)