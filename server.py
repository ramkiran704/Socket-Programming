import socket

HOST = '10.248.243.64'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Waiting for your Oppo A57 to connect...")

    client_socket, client_address = server_socket.accept()
    print(f"Connected to phone: {client_address}")
    print("--- Chat Started (Type 'exit' to quit) ---")

    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            message = data.decode('utf-8').strip()
            print(f"Oppo: {message}")
            if message.lower() == 'exit':
                break
            reply = input("Laptop: ")
            client_socket.sendall((reply + '\n').encode('utf-8'))
            if reply.lower() == 'exit':
                break