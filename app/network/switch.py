from app.network import IPAddress, Netmask, MacAddress


class Switch:
    def __init__(
        self,
        brand: str,
        model: str,
        puertos: int,
    ) -> None:
        self.brand = brand
        self.model = model
        self.puertos = puertos
        self.mac_address = MacAddress()
        self.hosts: dict

    def __str__(self) -> str:
        return f"Marca:{self.brand}, Modelo:{self.model}, Puertos:{self.puertos}, MAC:{self.mac_address}"

    def connect_sw(
        self,
        pto,
    ):
        self.hosts
        pass
