import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = []


def handle_client(client, address):
    print("Client connected:", address)

    name = client.recv(1024).decode()
    print(name, "joined the chat")

    clients.append(client)

    while True:
        message = client.recv(1024).decode()

        if message == "exit":
            clients.remove(client)
            client.close()
            print(name, "left the chat")
            break

        message = name + ": " + message

        for c in clients:
            if c != client:
                c.send(message.encode())


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))
server.listen(5)

print("Chat Server Started...")
print("Waiting for clients...")

while True:
    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()