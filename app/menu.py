import time
from .page import Page
from . import functions


class Menu:
    def __init__(self) -> None:
        self.load_pages()
        self.load_functions()
        self.current_page: object = self.main_page
        self.before_page: object = None
        self.network: object = None

    def input_menu(self) -> str:
        while True:
            self.clear_screen()  # Limpiar pantalla
            self.current_page.display()
            answer = input("Seleciona una opçión: ").strip().lower()
            if len(answer) > 0:
                if answer in self.current_page.options:
                    return self.current_page.options.get(answer)
                else:
                    """
                    Mostrar la información de las llaves en self.page_menu
                    """
                    keys = []
                    print(
                        f"La opcion:'{answer}', no es valida",
                        "\nSeleciona alguna opcion valida:",
                    )
                    for key in self.current_page.options:
                        keys.append(key)
                    print("  '", ", ".join(keys), "'")
                    input("Enter para continuar!")

    def call_menu(self, option: str) -> None:
        # Intenta obtener la función correspondiente por su nombre
        func = getattr(self, option, None)
        if func:
            if option == "new_network" or option == "load_network":
                self.network = func()
                if self.network:
                    self.update_page_menu(page_menu="network_page")
            else:
                func()  # Llama a la función si se encontró
        else:
            print(f"La opción '{option}' no tiene una función asociada.")
            input("Enter para continuar")

    def update_page_menu(self, page_menu: str) -> None:
        page = getattr(self, page_menu, None)
        if isinstance(page, Page):
            self.before_page = self.current_page
            self.current_page = page
        else:
            print(f"No se pudo encontrar la página '{page_menu}'.")

    def load_pages(self) -> None:
        self.main_page = Page(
            func_name=None,
            menu_name="main_page",
            head="Simulador de Redes",
            options_display=["Nueva Red", "Cargar Red", "Guardar Red","Borrar Red"],
            options={
                "1": "new_network",
                "2": "load_network",
                "3": "save_network",
                "4": "delete_network",
                "q": "exit",
            },
            bottom="(q) Cerrar aplicación",
        )
        self.network_page = Page(
            func_name=None,
            menu_name="sub_menu_1",
            head="Nueva Red",
            options_display=[
                "Info Network",
                "Agregar DHCP",
                "-",
                "-",
            ],
            options={
                "1": "info_network",
                "2": "add_dhcp",
                "3": "add_switch",
                "4": "add_switch",
                "r": "return",
            },
            bottom="(r) Regresar",
        )

    def load_functions(self) -> None:
        self.new_network: function = getattr(functions, "new_network", None)
        self.load_network: function = getattr(functions, "load_network", None)
        self.delete_network: function = getattr(functions, "delete_network", None)
        self.add_switch: function = getattr(functions, "add_switch", None)
        self.clear_screen: function = getattr(functions, "clear_screen", None)

    def info_network(self):
        if self.network:
            functions.info_network(self.network)
            print(self.network.settings.get('data'))
        else:
            print("no existe ninguna red cargada")
            input('@')
    
    def add_dhcp(self):
        if self.network:
            input()
            functions.add_dhcp(self.network)
            input("$: ")
        else:
            print("no existe ninguna red cargada")
            input('@')

    def save_network(self):
        try:
            self.network.save_settings()
            print(f"La red {self.network.name} ha sido guardada exitosamente")
            time.sleep(1.4)
        except Exception as e:
            print(f"Algo sucedio, error {str(e)}")