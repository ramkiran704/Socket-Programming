import socket
import multiprocessing
import time


HOST = "127.0.0.1"
PORT = 5000


def handle_client(data, address):
    print("Client connected:", address)

    if data == b"TIME":
        current_time = time.ctime()

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        sock.sendto(
            current_time.encode(),
            address
        )

        sock.close()


if __name__ == "__main__":

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    server_socket.bind((HOST, PORT))

    print("Server is Listening.......")

    while True:

        print("Waiting for Client........")

        data, address = server_socket.recvfrom(1024)

        process = multiprocessing.Process(
            target=handle_client,
            args=(data, address)
        )

        process.start()