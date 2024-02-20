import random

class MacAddress:
    def __init__(self, address=None):
        if address:
            self.address = address
        else:
            self.generate_random_address()

    def generate_random_address(self):
        # Genera una dirección MAC aleatoria
        mac = [random.randint(0x00, 0xff) for _ in range(6)]
        print(mac)
        self.address = ':'.join(map(lambda x: "%02x" % x, mac))

    def __str__(self):
        return self.address
