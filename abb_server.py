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
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",8000))
print("Server is Listening.........")
while( True):
    data,address=server.recvfrom(1024)
    request=data.decode().strip().upper()
    print('Requested from :',address)
    response=abb.get(request,"Not FOund")
    server.sendto(response.encode(),address)