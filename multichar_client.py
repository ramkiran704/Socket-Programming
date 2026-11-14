import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
name = input("Enter your name: ")
def receive():
 while True:
    try:
        message = client.recv(1024).decode()
        print("\n" + message)
    except:
        break
def send():
 while True:
    message = input()
    if message.lower() == "exit":
        client.close()
    break
    client.send((name + ": " + message).encode())
thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()
send()
