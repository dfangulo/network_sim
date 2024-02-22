from os import system
from .menu_items import menu_options
from .page import Page


class Menu:
    def __init__(self) -> None:
        self.menu_options: dict = menu_options
        self.load_pages()
        self.current_page: str = 'main_menu'

    def load_pages(self) -> None:
        self.main_page = Page(
            name='main_menu',
            head="Simulador de Redes",
            options=["Nueva Red", "Cargar Red"],
            bottom="(q) Cerrar aplicación",
        )
        self.new_network = Page(
            name="sub_menu_1",
            head="Nueva Red",
            options=[
                "Menu_1_add_Switch",
                "Menu_1_add_DHCP",
                "Menu_1_add_device",
                "Menu_1_remove_device",
            ],
            bottom="(r) Regresar",
        )
        self.new_network = Page(
            name="sub_menu_2",
            head="Cargar Red",
            options=[
                "Menu_1_add_Switch",
                "Menu_1_add_DHCP",
                "Menu_1_add_device",
                "Menu_1_remove_device",
            ],
            bottom="(r) Regresar",
        )

    def call_menu(self, option: str) -> None:
        # Intenta obtener la función correspondiente por su nombre
        func = getattr(self, option, None)
        if func:
            func()  # Llama a la función si se encontró
        else:
            print(f"La opción '{option}' no tiene una función asociada.")

    def input_menu(self) -> str:
        while True:
            system("cls")
            self.main_page.display()
            answer = input("Seleciona una opçión: ").strip().lower()
            if len(answer) > 0:
                if answer in self.menu_options.get(self.current_page):
                    return self.menu_options[self.current_page][answer]
                else:
                    """
                    Mostrar la información de las llaves en self.page_menu
                    """
                    keys = []
                    print(
                        f"La opcion:'{answer}', no es valida",
                        "\nSeleciona alguna opcion valida:",
                    )
                    for key in self.menu_options[self.current_page]:
                        keys.append(key)
                    print("\t", ", ".join(keys))
                    input("Enter para continuar!")

    def update_page_menu(self, page_menu: str) -> None:
        self.current_page = page_menu

    def sub_menu_1(self):
        self.update_page_menu("sub_menu_1")
