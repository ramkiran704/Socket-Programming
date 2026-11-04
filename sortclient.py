import socket 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5000))
element=input("Enter the array:(1 2 4 5 3 9)")
data=list(map(int,element.split()))

client.sendall(element.encode())
response=client.recv(4096).decode()
sorted_list=list(map(int,response.split()))

print(sorted_list)