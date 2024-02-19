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
        self.address = ':'.join(map(lambda x: "%02x" % x, mac))

    def __str__(self):
        return self.address

if __name__ == '__main__':
    # Ejemplo de uso
    mac1 = MacAddress()
    print("Dirección MAC generada aleatoriamente:", mac1)

    # También puedes especificar una dirección MAC específica al crear el objeto
    mac2 = MacAddress("00:11:22:33:44:55")
    print("Dirección MAC especificada:", mac2)
