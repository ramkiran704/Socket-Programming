import socket
import threading
import os
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)
print("File Server Started...")
pid = os.getpid()
def handle_client(client):
    filename = client.recv(1024).decode()
    if os.path.exists(filename):
        file = open(filename, 'r')
        content = file.read()
        file.close()
        response = "PID: " + str(pid) + "\nFile Contents:\n" + content
    else:
        response = "PID: " + str(pid) + "\nFile not found!"
    client.send(response.encode())
    client.close()
while True:
 client, addr = server.accept()
 print("Client connected:", addr)
 thread = threading.Thread(target=handle_client, args=(client,))
 thread.start()
