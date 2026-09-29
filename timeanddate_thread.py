import os
import socket
from datetime import datetime
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 6000))
print("Time Server is running...")
print("Waiting for client request...")
while True:
    data, address = server_socket.recvfrom(1024)
    pid = os.fork()
    if pid == 0:
        child_pid = os.getpid()
        print(f"Child PID {child_pid} handling client: {address}")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        server_socket.sendto(current_time.encode(), address)
        os._exit(0)