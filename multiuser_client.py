import socket
import threading

username = input("Enter your username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

def receive():
    """Continuously receives messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("An error occurred! Disconnecting...")
            client.close()
            break

def write():
    """Continuously takes user input and sends it to the server."""
    while True:
        message = f"{username}: {input('')}"
        try:
            client.send(message.encode())
        except:
            break
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()