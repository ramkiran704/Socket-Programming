from scapy.all import sniff, Ether

print("Packet Sniffer Started.....")
print("Waiting for packets.......")

def packet_handler(packet):

    if Ether in packet:
        ethernet_header = packet[Ether]

        print("Packet Captured")

        print("Source MAC:", ethernet_header.src)
        print("Destination MAC:", ethernet_header.dst)
        print("Protocol:", hex(ethernet_header.type))
        print("Packet Size:", len(packet))

        print("-------------------------")

sniff(prn=packet_handler)