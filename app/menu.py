from .page import Page
from . import functions


class Menu:
    def __init__(self) -> None:
        self.load_pages()
        self.current_page: object = self.main_page
        self.before_page: object = None
        self.add_switch = getattr(functions, "add_switch", None)
        self.clear_screen = getattr(functions, "clear_screen", None)

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
                    print("\t", ", ".join(keys))
                    input("Enter para continuar!")

    def call_menu(self, option: str) -> None:
        # Intenta obtener la función correspondiente por su nombre
        func = getattr(self, option, None)
        # func = getattr(option)
        if func:
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
            options_display=["Nueva Red", "Cargar Red"],
            options={
                "1": "new_network_page",
                "2": "load_network_page",
                "q": "exit",
            },
            bottom="(q) Cerrar aplicación",
        )
        self.new_network_page = Page(
            func_name=None,
            menu_name="sub_menu_1",
            head="Nueva Red",
            options_display=[
                "Test Network",
                "Agregar servidor DHCP",
                "Conectar Dispositivos",
                "Desconectar Dispositivos",
            ],
            options={
                "1": "add_switch",
                "r": "return",
            },
            bottom="(r) Regresar",
        )
        self.load_network_page = Page(
            func_name=None,
            menu_name="sub_menu_2",
            head="Cargar Red",
            options_display=[
                "Abrir Red",
                "Borrar Red",
            ],
            options={
                "r": "return",
            },
            bottom="(r) Regresar",
        )

