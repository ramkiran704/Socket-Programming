import socket
SERVER_HOST = '10.248.243.64'
SERVER_PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"Connecting to Laptop ({SERVER_HOST}:{SERVER_PORT})...")
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected! --- Chat Started (Type 'exit' to quit) ---")

    while True:
        message = input("Oppo: ")
        client_socket.sendall(message.encode('utf-8'))
        if message.strip().lower() == 'exit':
            print("Closing connection...")
            break
        data = client_socket.recv(1024)
        if not data:
            print("Laptop disconnected.")
            break

        reply = data.decode('utf-8').strip()
        print(f"Laptop: {reply}")
        if reply.lower() == 'exit':
            print("Laptop ended the chat.")
            break

except ConnectionRefusedError:
    print("Error: Could not connect to the server. Make sure the server script is running on the laptop.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client_socket.close()
    print("Disconnected.")