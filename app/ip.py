
class IPAddress:
    def __init__(self, ip_str, subnet_mask_str):
        self.ip = ip_str
        self.subnet_mask = subnet_mask_str
        self.network = ip_str
        self.hosts = list(self.ip)
        # Crea una lista de octetos de 8 bits para representar la dirección de broadcast
        self.net_mask = ["1".join(["" for _ in range(8)]) for _ in range(4)]

    def calcular_netmask(self, subred: int) -> str:
        # Validar que subred esté en el rango correcto
        if subred < 0 or subred > 32:
            return "Subred inválida. Debe estar entre 0 y 32."

        # Calcular los octetos de la máscara de subred en notación binaria
        binary_mask = "1" * subred + "0" * (32 - subred)
        print(f"\t{binary_mask}")

        # Convertir los octetos binarios en notación decimal
        decimal_mask = [str(int(binary_mask[i:i+8], 2))
                        for i in range(0, 32, 8)]
        print(f"\t{decimal_mask}")
        total = 1
        for oct in decimal_mask:
            total += (255-int(oct))
        print(f"\t{total}")

        # Unir los octetos en una cadena separada por puntos para obtener la máscara de subred en notación decimal
        netmask = ".".join(decimal_mask)

        return netmask


if __name__ == "__main__":
    ip = IPAddress('', '')
    for net in range(32):
        netmask = ip.calcular_netmask(32 - net)
        print(netmask)
