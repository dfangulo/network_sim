from app.net_components import IPAddress, Netmask, MacAddress
import random


class DHCP:
    def __init__(
        self,
        network_ip: list[int],
        subnet_mask: int,
        ip_range_start: list[int],
        ip_range_end: list[int],
        gateway: list[int],
        dns1: list[int],
        dns2: list[int],
    ) -> None:
        self.network_ip = IPAddress(network_ip)
        self.subnet_mask = Netmask(subnet_mask)
        self.ip_range_start = IPAddress(ip_range_start)
        self.ip_range_end = IPAddress(ip_range_end)
        self.gateway = IPAddress(gateway)
        self.dns1 = IPAddress(dns1)
        self.dns2 = IPAddress(dns2)
        self.leased_ips = {}

    def __str__(self) -> str:
        return f""

    def offer_ip(self) -> str:
        # Convertir las direcciones IP de inicio y fin del rango en listas de números enteros
        start_ip_octets = [
            int(octeto) for octeto in str(self.ip_range_start).split(".")
        ]
        end_ip_octets = [int(octeto) for octeto in str(self.ip_range_end).split(".")]

        # Generar números aleatorios para cada octeto dentro del rango especificado
        random_ip_octets = [
            random.randint(start_octeto, end_octeto)
            for start_octeto, end_octeto in zip(start_ip_octets, end_ip_octets)
        ]

        # Convertir los octetos aleatorios de nuevo a una dirección IP en formato de cadena
        random_ip_str = ".".join(map(str, random_ip_octets))

        return random_ip_str

    def request_ip(self, mac_address: str) -> str:
        # Si la dirección MAC ya está asignada, retorna la IP asignada previamente
        if mac_address in self.leased_ips:
            return self.leased_ips[mac_address]

        # Si no, ofrece una IP disponible y la marca como asignada
        ip_address = self.offer_ip()
        self.leased_ips[mac_address] = ip_address
        return ip_address

