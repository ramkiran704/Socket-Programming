import socket
client_socket=socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client_socket.connect(('127.0.0.1',8000))
inp=input("Enter the Abbreaviation:")
inp1=inp.upper()
client_socket.send(inp1.encode())
reply=client_socket.recv(1024).decode()
print(f"Full Form of {inp} is :",reply)
