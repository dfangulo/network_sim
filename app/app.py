from app.network.dhcp_server import DHCP, MacAddress
from .menu import Menu


class App:
    def __init__(self) -> None:
        self.menu = Menu()
        self.view()

    def view(self) -> None:
        while True:
            sub_menu = self.menu.input_menu()
            if sub_menu == "exit":
                print("Saliendo del programa!")
                break
            else:
                print(sub_menu)
                self.menu.call_menu(option=sub_menu)
                input("Presiona Enter para continuar!")


    def run(self) -> None:
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
        except ValueError as e:
            print("Error:", e)
