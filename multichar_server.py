import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()
clients = []
print("Chat Server Started...")
def broadcast(message, sender):
 for client in clients:
    if client != sender:
        try:
            client.send(message)
        except:
            clients.remove(client)
def handle_client(client):
 while True:
    try:
        message = client.recv(1024)
        if not message:
            break
        broadcast(message, client)
    except:
        break
 clients.remove(client)
 client.close()
 print("A client disconnected")
while True:
 client, addr = server.accept()
 clients.append(client)
 print("Connected:", addr)
 thread = threading.Thread(
 target=handle_client,
 args=(client,)
 )
 thread.start()