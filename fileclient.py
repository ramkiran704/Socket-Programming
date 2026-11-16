import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
filename = input("Enter filename to request: ")
client.send(filename.encode())
response = client.recv(4096).decode()
print("\nServer Response:")
print(response)
client.close()