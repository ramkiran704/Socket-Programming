import threading
import socket
def handle_client(client_socket,client_address):
    print(f"Connected to {client_address}")
    try:
        while(True):
            data=client_socket.recv(1024)
            if not data:
                break

            message=data.decode()
            print(f"{message} from {client_address}")
            response=f"{message} recieved Successfully"
            client_socket.send(response.encode())
    except ConnectionResetError:
        print(f"Connection Disconnected {client_address}")
    finally:
        client_socket.close()
        print(f"Connection Failed{client_address}\n ")
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',5555))
server.listen(5)
print(f"Server is listening to the {5555} Port")
while(True):
    client_socket,client_address=server.accept()
    thread=threading.Thread(target=handle_client,args=(client_socket,client_address))
    thread.start()
    print(f"Active Clients:{threading.active_count()-1}")