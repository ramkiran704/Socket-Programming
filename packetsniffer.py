import socket
import struct
raw_socket=socket.socket(
socket.AF_PACKET,
socket.SOCK_RAW,
socket.ntohs(3)
)
print("Packet Sniffer started...")
print("Waiting for packets...\n")
while True:
    packet,address=raw_socket.recvfrom(655355)
    ethernet_header=packet[:14]
    dest_mac,src_mac,protocol=struct.unpack(
    "!6s6sH",
    ethernet_header
    )
    print("Packet captured")
    print("Source MAC :",":".join(f"b:02x" for b in src_mac))
    print("Destination MAC:",":".join(f"b:02x" for b in dest_mac))
    print("Protocol :",protocol)
    print("Packet Size :",len(packet))
    print("-------------------------")
