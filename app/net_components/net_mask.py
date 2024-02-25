class Netmask:
    def __init__(self, netmask: int) -> None:
        self.netmask = netmask
        self.subnet_ips = self.show_subnet()
        self._netmask = self.show_netmask()

    def __str__(self) -> list[int, int, int, int]:
        """AI is creating summary for __str__

        Returns:
            list[int, int, int, int]: [description]
        """
        return ".".join(map(str, self._netmask))

    def show_netmask(self) -> str:
        """AI is creating summary for calcular_netmask

        Args:
            subred (int): [description]

        Returns:
            str: [description]
        """

        # Validar que subred esté en el rango correcto
        if self.netmask < 0 or self.netmask > 32:
            return "Subred inválida. Debe estar entre 0 y 32."

        # Calcular los octetos de la máscara de subred en notación binaria
        binary_mask = "1" * self.netmask + "0" * (32 - self.netmask)

        # Convierte los octetos binarios en notación decimal
        decimal_mask = [int(binary_mask[i : i + 8], 2) for i in range(0, 32, 8)]

        return decimal_mask

    def show_subnet(self):
        pass
