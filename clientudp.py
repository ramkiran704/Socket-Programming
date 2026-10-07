import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Client Sarted.")
while True:
    message=input("Enter Message:")
    if message.lower()=="exit":
        break
    else:
        client.sendto(message.encode(),('127.0.0.1',5000))
        data,server_address=client.recvfrom(1024)
        print("Server says:",data.decode())
client.close()