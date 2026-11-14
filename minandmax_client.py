import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",5000))
inp=input("Enter teh list:(1 2 3 4 5):")
client.sendall(inp.encode())
response=client.recv(1024).decode()

print(response)