import os
import json
from app.net_components.dhcp_server import DHCP, MacAddress
from .network import Network


def clear_screen():
    sistema_operativo = os.name
    if sistema_operativo == "posix":  # Linux, Unix o macOS
        os.system("clear")
    elif sistema_operativo == "nt":  # Windows
        os.system("cls")
    else:
        # Si el sistema operativo no es reconocido, no se realiza ninguna acción
        pass


def new_network(self) -> None:
    pass


def load_network(self) -> None:
    pass


def add_dhcp() -> None:
    pass


def add_switch() -> None:
    try:
        # Ejemplo de uso
        ip = [192, 168, 1, 1]
        netmask = 30
        ip_start = [192, 168, 1, 20]
        ip_end = [192, 168, 1, 50]
        gateway = [192, 168, 1, 7]
        dns1 = [192, 168, 1, 1]
        dns2 = [80, 80, 81, 81]

        dhcp_server = DHCP(
            network_ip=ip,
            subnet_mask=netmask,
            ip_range_start=ip_start,
            ip_range_end=ip_end,
            gateway=gateway,
            dns1=dns1,
            dns2=dns2,
        )

        # Simular una solicitud de IP para una nueva máquina con una dirección MAC específica
        mac_address = MacAddress("00:11:22:33:44:55")
        mac_address1 = MacAddress()
        print(mac_address)
        ip_address = dhcp_server.request_ip(str(mac_address))
        ip_address1 = dhcp_server.request_ip(str(mac_address1))
        print(dhcp_server)
        print(
            "Dirección IP asignada a la máquina con MAC",
            mac_address,
            ":",
            ip_address,
            dhcp_server.subnet_mask,
            dhcp_server.gateway,
            dhcp_server.dns1,
            dhcp_server.dns2,
        )
        print(
            "Dirección IP asignada a la máquina con MAC",
            mac_address1,
            ":",
            ip_address1,
            dhcp_server.subnet_mask,
            dhcp_server.gateway,
            dhcp_server.dns1,
            dhcp_server.dns2,
        )
        print(dhcp_server.leased_ips)
        input("Enter Para continuar!.")
    except ValueError as e:
        print("Error:", e)
