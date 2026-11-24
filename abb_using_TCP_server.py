import socket
abb={
    "BRB": "Be Right Back",
    "IMO": "In My Opinion",
    "FYI": "For Your Information",
    "TTYL": "Talk To You Later",
    "AFK": "Away From Keyboard",
    "IDK": "I Don't Know",
    "OMG": "Oh My God",
    "BTW": "By The Way"
}
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8000))
server.listen(1)
print("Server is Listening...........")
while(True):
    client_socket,client_address=server.accept()
    request=client_socket.recv(1024).decode()
    print(f"Requested from :{client_address} \t Value is {request}")
    response=abb.get(request,"NOt Found")
    client_socket.send(response.encode())