import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5003))
elements=input("Enter the array:(1 2 4 5 3 9)")
data=list(map(int,elements.split()))
print("List:",data)
client.sendall(elements.encode())
response=client.recv(4096).decode()

print(response)