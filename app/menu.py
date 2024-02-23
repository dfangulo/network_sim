from os import system
from .page import Page
from app.network.dhcp_server import DHCP, MacAddress



class Menu:
    def __init__(self) -> None:
        self.load_pages()
        self.current_page: object = self.main_page
        self.before_page: object = None

    def load_pages(self) -> None:
        self.main_page = Page(
            func_name=None,
            menu_name="main_page",
            head="Simulador de Redes",
            options_display=["Nueva Red", "Cargar Red"],
            options={
                "1": "new_network_page",
                "2": "load_network_page",
                "q": "exit",
            },
            bottom="(q) Cerrar aplicación",
        )
        self.new_network_page = Page(
            func_name=None,
            menu_name="sub_menu_1",
            head="Nueva Red",
            options_display=[
                "Test Network",
                "Menu_1_add_DHCP",
                "Menu_1_add_device",
                "Menu_1_remove_device",
            ],
            options={
                "1": "add_switch",
                "r": "return",
            },
            bottom="(r) Regresar",
        )
        self.load_network_page = Page(
            func_name=None,
            menu_name="sub_menu_2",
            head="Cargar Red",
            options_display=[
                "Menu_1_add_Switch",
                "Menu_1_add_DHCP",
                "Menu_1_add_device",
                "Menu_1_remove_device",
            ],
            options={
                "r": "return",
            },
            bottom="(r) Regresar",
        )

    def call_menu(self, option: str) -> None:
        # Intenta obtener la función correspondiente por su nombre
        func = getattr(self, option, None)
        if func:
            func()  # Llama a la función si se encontró
        else:
            print(f"La opción '{option}' no tiene una función asociada.")

    def input_menu(self) -> str:
        while True:
            system("cls")
            self.current_page.display()
            answer = input("Seleciona una opçión: ").strip().lower()
            if len(answer) > 0:
                if answer in self.current_page.options:
                    return self.current_page.options.get(answer)
                else:
                    """
                    Mostrar la información de las llaves en self.page_menu
                    """
                    keys = []
                    print(
                        f"La opcion:'{answer}', no es valida",
                        "\nSeleciona alguna opcion valida:",
                    )
                    for key in self.current_page.options:
                        keys.append(key)
                    print("\t", ", ".join(keys))
                    input("Enter para continuar!")

    def update_page_menu(self, page_menu: str) -> None:
        page = getattr(self, page_menu, None)
        if isinstance(page, Page):
            self.before_page = self.current_page
            self.current_page = page
        else:
            print(f"No se pudo encontrar la página '{page_menu}'.")

    def add_switch(self) ->None:
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