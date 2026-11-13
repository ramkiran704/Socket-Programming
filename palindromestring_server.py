import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",5000))
while True:
    client_socket,client_address=server.recvfrom(1024)
    s=client_socket.decode()
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    if s==s1:
        result="Palindrome"
    else:
        result="Not Palindrome"
    server.sendto(result.encode(),client_address)