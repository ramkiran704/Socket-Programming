import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",5003))
inp=input ("Enter the string:")
print("Input string is :",inp)
client.send(inp.encode())
response=client.recv(1024).decode()
print("Output:",response)