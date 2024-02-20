class Packet:
    def __init__(self, source_mac, destination_mac, source_ip, destination_ip, payload):
        self.source_mac = source_mac
        self.destination_mac = destination_mac
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.payload = payload
    
    def __str__(self):
        return f"Packet: Source MAC={self.source_mac}, Destination MAC={self.destination_mac}, Source IP={self.source_ip}, Destination IP={self.destination_ip}, Payload={self.payload}"

# Ejemplo de uso:
packet1 = Packet("00:11:22:33:44:55", "66:77:88:99:AA:BB", "192.168.1.10", "192.168.1.20", "DHCP Discover")
print(packet1)
