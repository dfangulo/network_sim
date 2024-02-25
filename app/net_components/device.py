from app.net_components import IPAddress, Netmask, MacAddress


class Device:
    def __init__(
        self,
        brand: str,
        model: str,
    ) -> None:
        self.brand = brand
        self.model = model
        self.mac_address = MacAddress()
