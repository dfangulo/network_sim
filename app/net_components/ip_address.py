class IPAddress:
    def __init__(self, ip_address: list[int]) -> None:
        if len(ip_address) != 4:
            raise ValueError("La dirección IP debe tener cuatro octetos")
        self.ip_address = ip_address
        self.ip_validate()

    def __str__(self) -> str:
        return ".".join(map(str, self.ip_address))

    def ip_validate(self) -> None:
        """AI is creating summary for ip_validate

        Raises:
            ValueError: [description]
        """        
        for octeto in self.ip_address:
            if not 0 <= octeto <= 254:
                raise ValueError("La dirección IP es inválida")

