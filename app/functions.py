import os
from app.net_components.dhcp_server import DHCP, MacAddress
from .network import Network

__JSON_PATH = "app/files/"


def clear_screen() -> None:
    sistema_operativo = os.name
    if sistema_operativo == "posix":  # Linux, Unix o macOS
        os.system("clear")
    elif sistema_operativo == "nt":  # Windows
        os.system("cls")
    else:
        # Si el sistema operativo no es reconocido, no se realiza ninguna acción
        pass


def new_network() -> object:
    print("Datos Para crear una RED".center(27))
    print("\nIngresa un nombne para la red:")
    name = input(">:")

    print("Nombre del archivo:")
    file_name = input(">:")
    if not file_name:
        file_name = __JSON_PATH + name + ".json"

    network = Network(name=name, file_name=file_name)
    network.save_settings()
    return network


def load_network() -> None:
    # Lista todos los archivos y directorios en el directorio especificado
    list_files()
    file_name = input("Nombre del archivo a cargar ")
    full_file_name = __JSON_PATH + file_name
    # Verifica si el archivo existe antes de intentar borrarlo
    if os.path.exists(full_file_name):
        # Intenta borrar el archivo
        try:
            network = Network.from_file(file_name=full_file_name)
            print(
                f"El archivo '{network.get_settings()}' ha sido cargado correctamente."
            )
            return network
        except OSError as e:
            print(f"Error al cargar el archivo '{full_file_name}': {e}")
    else:
        print(f"El archivo '{__JSON_PATH + file_name}' no existe.")
        input("Enter para volver!")


def delete_network() -> None:
    list_files()
    file_name = input("Nombre del archivo a borrar: ")
    if not file_name:
        return
    # Verifica si el archivo existe antes de intentar borrarlo
    if os.path.exists(__JSON_PATH + file_name):
        # Intenta borrar el archivo
        try:
            os.remove(__JSON_PATH + file_name)
            print(
                f"El archivo '{__JSON_PATH + file_name}' ha sido eliminado correctamente."
            )
        except OSError as e:
            print(
                f"Error al intentar eliminar el archivo '{__JSON_PATH + file_name}': {e}"
            )
    else:
        print(f"El archivo '{__JSON_PATH + file_name}' no existe.")
    input("Enter para volver!")


def list_files() -> None:
    archivos = os.listdir(__JSON_PATH)

    # Imprime la lista de archivos
    print("Archivos en el directorio:")
    for archivo in archivos:
        print(" - ", archivo)


def add_dhcp(network:object) -> None:
    # Ejemplo de uso
    if network.settings.get(network).get("dhcp"):
        ip_server = [192, 168, 1, 1]
        netmask = 30
        ip_start = [192, 168, 1, 20]
        ip_end = [192, 168, 1, 50]
        gateway = [192, 168, 1, 7]
        dns1 = [192, 168, 1, 1]
        dns2 = [80, 80, 81, 81]
    dhcp_server = DHCP(
        network_ip=ip_server,
        subnet_mask=netmask,
        ip_range_start=ip_start,
        ip_range_end=ip_end,
        gateway=gateway,
        dns1=dns1,
        dns2=dns2,
    )
    json_str = {
        "ip_server" : ip_server,
        "netmask" : netmask,
        "ip_start" : ip_start,
        "ip_end" : ip_end,
        "gateway" : gateway,
        "dns1" : dns1,
        "dns2" : dns2
    }
    network.set_settings(key='dhcp', value=json_str)
    


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


def info_network(network: object = None) -> None:
    print("Info Network")
    print(network.get_settings())
    input("Enter para continuar!")
