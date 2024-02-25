import json


class Network:
    def __init__(self, name, file_name, settings: dict = None) -> None:
        self.name = name
        self.file_name = file_name
        self.settings = settings

    def __str__(self) -> str:
        return f"{self.name}"

    def load_settings(self) -> None:
        # Cargar los datos desde el archivo JSON
        with open(self.file_name, "r") as archivo:
            self.settings = json.load(archivo)

    def set_settings(self) -> None:
        # Guardar los datos en un archivo JSON
        with open(self.name, 'w') as archivo:
            json.dump(self.settings, archivo, indent=4)

    def get_settings(self) -> dict:
        return self.settings
