import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=input("Enter teh number:")
client.sendto(n.encode(),("127.0.0.1",5010))
response,server_address=client.recvfrom(1024)
print(response.decode())