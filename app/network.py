import json


class Network:
    def __init__(self, name, file_name, settings: dict = {}) -> None:
        self.name = name
        self.file_name = file_name
        self.settings = {
            "data": {"name": name, "file_name": file_name},
            "network": settings,
        }

    def __str__(self) -> str:
        return f"Network: {self.name}"

    def set_settings(self, key, value) -> None:
        self.settings["network"][key] = value

    def load_settings(self) -> None:
        # Cargar los datos desde el archivo JSON
        with open(self.file_name, "r") as archivo:
            self.settings = json.load(archivo)
        data = self.settings.get("data")
        self.name = data.get("name")
        self.file_name = data.get("file_name")

    def save_settings(self) -> None:
        # Guardar los datos en un archivo JSON
        with open(self.file_name, "w") as archivo:
            json.dump(self.settings, archivo, indent=4)

    def get_settings(self) -> dict:
        self.settings.get("data", None)
        self.settings.get("network", None)
        return self.settings

    @classmethod
    def from_file(cls, name: str = "temp", file_name: str = None):
        # Crear una instancia de la clase Network
        instancia = cls(name, file_name)
        # Cargar los datos desde el archivo JSON
        instancia.load_settings()
        return instancia
