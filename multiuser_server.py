import socket
import threading

# List to store connected client sockets
clients = []

def broadcast(msg, sender):
    """Broadcasts a message to all clients except the sender."""
    for c in clients:
        if c != sender:
            try:
                c.send(msg)
            except:
                # Remove client if sending fails
                if c in clients:
                    clients.remove(c)

def handle(c):
    """Handles communication with a single client."""
    while True:
        try:
            msg = c.recv(1024)
            if not msg:
                break
            broadcast(msg, c)
        except:
            break
            
    # Cleanup when client disconnects
    if c in clients:
        clients.remove(c)
    c.close()

# Initialize TCP Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen()
print("Server started...")

while True:
    c, addr = server.accept()
    print("Connected with:", addr)
    clients.append(c)
    
    # Start a thread to handle the new client
    threading.Thread(target=handle, args=(c,)).start()