import socket
import threading
def thread_handle(client_socket,client_address):
    print("Client Connected:",client_address)
    try:
        while True:
            data=client_socket.recv(1024)
            if not data:
                break
            else:
                message=data.decode()
                print("Client Message:",message)
                response=f"Server recevied :{message}"
                client_socket.send(response.encode())
    except ConnectionResetError:
        print("client Disconnected")
    finally:
        client_socket.close()
        print("Connection closed")
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',5010))
server.listen(5)
print("Server is Listening ........")
while True:
    client_socket,client_address=server.accept()
    thread=threading.Thread(target=thread_handle,args=(client_socket,client_address))
    thread.start()
    print("Active Clients:",threading.active_count()-1)
